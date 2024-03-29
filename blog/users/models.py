from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from PIL import Image


# Create your models here.


class Network(AbstractUser):
    network_name = models.CharField(max_length=100)
    network_pastor = models.CharField(max_length=100)
    network_email = models.EmailField()

    groups = models.ManyToManyField(Group, related_name='network_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='network_user_permissions')

    def __str__(self):
        return self.username  # Display the username when the object is printed

    class Meta:
        verbose_name = "Network"


class Counselee(AbstractUser):
    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    othernames = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    hometown = models.CharField(max_length=50)
    network = models.ForeignKey(Network, on_delete=models.CASCADE, blank=True, null=True)
    registration_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'),
                                                                   ('rejected', 'Rejected')], default='pending')

    groups = models.ManyToManyField(Group, related_name='counselees')
    user_permissions = models.ManyToManyField(Permission, related_name='counselees')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name = "Counselee"
