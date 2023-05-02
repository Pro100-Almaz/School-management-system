from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

# class BaseContent(models.Model):
#     ACTIVE_CHOICES  = ((0, 'Inactive'), (2, 'Active'),)
#     active          = models.PositiveIntegerField(choices=ACTIVE_CHOICES,default=2)
#     created         = models.DateTimeField(auto_now_add=True)
#     modified        = models.DateTimeField(auto_now=True)
#     class Meta:
#         abstract    = True

from django.core.exceptions import ValidationError
def validate_image(image):
    file_size = image.file.size
    limit = 2
    if file_size > limit * 1024 *1024:
        raise ValidationError("Max size of file is %s MB" % limit)

# GENDER = ((0,'Male'),(1,'Female'),(2,'Other'))
# class UserProfile(BaseContent):
#     user            = models.OneToOneField(User,on_delete=models.CASCADE)
    # birth_date      = models.DateField(null=True, blank=True)
    # profile_pic     = models.ImageField(upload_to='user_pic/%Y/%m/%d', default='user_pic/no-img.jpg', blank=True, null=True, validators=[validate_image]) 
    # contact         = models.CharField(max_length =15, null=True, blank=True)
#     secondary_email = models.EmailField(max_length=150,null=True, blank=True)
    # gender          = models.IntegerField(default=0,choices=GENDER)
#     def __str__(self):
#         return str(self.user.email)    
    
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    birth_date      = models.DateField(null=True, blank=True)
    profile_pic     = models.ImageField(upload_to='user_pic/%Y/%m/%d', default='user_pic/no-img.jpg', blank=True, null=True, validators=[validate_image]) 
    contact         = models.CharField(max_length =15, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name