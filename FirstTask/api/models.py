from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager
from django.core.validators import MinLengthValidator


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    mobile = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        unique=True,
        verbose_name="Mobile Number",
    )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Customer(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    profile_number = models.CharField(max_length=10)
