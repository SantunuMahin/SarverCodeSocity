from django.core.validators import MinLengthValidator
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='posts/',blank=True,null=True)  # Ensure this path is correct
    author = models.CharField(max_length=12)
    like = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

class ClubMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    CITY_CHOICES = [
        ('bagerhat', 'Bagerhat'),
        ('bandarban', 'Bandarban'),
        ('barguna', 'Barguna'),
        ('barisal', 'Barisal'),
        ('bhola', 'Bhola'),
        ('bogura', 'Bogura'),
        ('brahmanbaria', 'Brahmanbaria'),
        ('chandpur', 'Chandpur'),
        ('chattogram', 'Chattogram'),
        ('chuadanga', 'Chuadanga'),
        ('comilla', 'Comilla'),
        ('coxsbazar', 'Cox\'s Bazar'),
        ('dhaka', 'Dhaka'),
        ('dinajpur', 'Dinajpur'),
        ('faridpur', 'Faridpur'),
        ('feni', 'Feni'),
        ('gaibandha', 'Gaibandha'),
        ('gazipur', 'Gazipur'),
        ('gopalganj', 'Gopalganj'),
        ('habiganj', 'Habiganj'),
        ('jamalpur', 'Jamalpur'),
        ('jashore', 'Jashore'),
        ('jhenaidah', 'Jhenaidah'),
        ('joypurhat', 'Joypurhat'),
        ('khagrachari', 'Khagrachari'),
        ('khulna', 'Khulna'),
        ('kishoreganj', 'Kishoreganj'),
        ('kurigram', 'Kurigram'),
        ('kushtia', 'Kushtia'),
        ('lakshmipur', 'Lakshmipur'),
        ('lalmonirhat', 'Lalmonirhat'),
        ('madaripur', 'Madaripur'),
        ('magura', 'Magura'),
        ('manikganj', 'Manikganj'),
        ('meherpur', 'Meherpur'),
        ('moulvibazar', 'Moulvibazar'),
        ('munshiganj', 'Munshiganj'),
        ('mymensingh', 'Mymensingh'),
        ('naogaon', 'Naogaon'),
        ('narail', 'Narail'),
        ('narayanganj', 'Narayanganj'),
        ('narsingdi', 'Narsingdi'),
        ('natore', 'Natore'),
        ('netrokona', 'Netrokona'),
        ('nilphamari', 'Nilphamari'),
        ('noakhali', 'Noakhali'),
        ('pabna', 'Pabna'),
        ('panchagarh', 'Panchagarh'),
        ('patuakhali', 'Patuakhali'),
        ('pirojpur', 'Pirojpur'),
        ('rajbari', 'Rajbari'),
        ('rajshahi', 'Rajshahi'),
        ('rangamati', 'Rangamati'),
        ('rangpur', 'Rangpur'),
        ('satkhira', 'Satkhira'),
        ('shariatpur', 'Shariatpur'),
        ('sherpur', 'Sherpur'),
        ('sirajganj', 'Sirajganj'),
        ('sunamganj', 'Sunamganj'),
        ('sylhet', 'Sylhet'),
        ('tangail', 'Tangail'),
        ('thakurgaon', 'Thakurgaon')
    ]

    city = models.CharField(max_length=20, choices=CITY_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
