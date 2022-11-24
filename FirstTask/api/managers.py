from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, mobile, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), mobile=mobile)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile, password=None):

        user = self.create_user(email, password=password, mobile=mobile)
        user.is_admin = True
        user.save(using=self._db)
        return user
