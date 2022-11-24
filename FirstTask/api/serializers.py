from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["profile_number"]

    def save(self, **kwargs):
        print(kwargs.get("user"))
        profile_number = self.validated_data.pop("profile_number")
        user = kwargs.get("user")
        return super().save(user=user, profile_number=profile_number)
