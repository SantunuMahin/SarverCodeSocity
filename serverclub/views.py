from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import ClubMember,Post
from .forms import CustomLoginForm, ClubMemberForm
from django.http import HttpResponse
from django.template import loader
from xhtml2pdf import pisa
from .forms import SignUpForm
from django.contrib import messages
from .forms import PostForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



# Helper function to check if user is authenticated
def redirect_authenticated_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect("login_view")


# Index/Home view
def home(request):
    return render(request, 'serverclubs/home.html')

# Login view
def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = CustomLoginForm()

    return render(request, 'serverclubs/login_view.html', {'form': form})
# logout view
def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login_view')

# Sign-up and login view
def signup_view(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)  # Log in the user immediately
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        signup_form = SignUpForm()

    return render(request, 'serverclubs/signup.html', {'signup_form': signup_form})

# Registration view
def register(request):
    if request.method == "POST":
        form = ClubMemberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if ClubMember.objects.filter(email=email).exists():
                return render(request, "serverclubs/register.html", {
                    'form': form, "error": "You are already registered."
                })
            else:
                form.save()
                messages.success(request, "Registration successful! Welcome to the club.")
                return render(request, 'serverclubs/success.html')  # After successful registration
    else:
        form = ClubMemberForm()

    return render(request, "serverclubs/register.html", {'form': form})

# Member list view
def member(request):
    members = ClubMember.objects.all()
    return render(request, 'serverclubs/member.html', {'members': members})

# Render to PDF function
def render_to_pdf(template_src, context_dict={}):
    template = loader.get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="members.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Download PDF view
def download_pdf(request):
    members = ClubMember.objects.all()
    context = {'members': members}
    return render_to_pdf('serverclubs/member_pdf.html', context)

# Problems view
def problems(request):
    return render(request, "serverclubs/problems.html")
# Posts views

def post(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully!")  # Success message
            return redirect('post')
    else:
        form = PostForm()  # Empty form if not a POST request

    return render(request, "serverclubs/post.html", {
        "posts": posts,
        "form": form  # Pass the form to the template
    })


# @login_required
# def post_like(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     post.like += 1
#     post.save()
#     return JsonResponse({'likes': post.like})
@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the post is already liked by the user in their session
    liked_posts = request.session.get('liked_posts', [])

    if pk in liked_posts:
        return JsonResponse({'message': 'You already liked this post', 'likes': post.like}, status=400)

    # Increment the like count
    post.like += 1
    post.save()

    # Add the post to the session's liked posts
    liked_posts.append(pk)
    request.session['liked_posts'] = liked_posts

    return JsonResponse({'likes': post.like})
# Mental support view
def mentalsupport(request):
    return render(request,"serverclubs/mentalsupport.html")