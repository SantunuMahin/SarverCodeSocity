from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.redirect_authenticated_user,name="redirect_authenticated_user"),
    path("home", views.home,name="home"),
   # path("founder/",views.protfolio,name="protfolio"),
    path('logout/', views.logout_view, name='logout'),
    path('login_view/', views.login_view, name='login_view'),
    path("register",views.register,name="register"),
    path('member',views.member, name="member"),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
    path('problems',views.problems,name="problems"),
    path("signup_view",views.signup_view, name="signup_view"),
    path("post", views.post,name="post"),
    path("mentalsupport",views.mentalsupport,name="mentalsupport"),
    path('like/<int:pk>/', views.post_like, name='post_like'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)