from .models import MyUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer
from django.core.exceptions import ValidationError

# Create your views here.


class createCustomer(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            password = data.get("password")
            if password is None:
                raise ValidationError({"Password": "Please enter password"})
            user = MyUser(
                email=data.get("email"),
                mobile=data.get("mobile"),
                first_name=data.get("first_name", ""),
                last_name=data.get("last_name", ""),
            )
            user.set_password(password)
            print("Going to validate serializer")
            serializer = CustomerSerializer(
                data={"profile_number": data.get("profile_number")}
            )
            if serializer.is_valid():
                user.save()
                serializer.save(user=user)
                return Response({"msg": "Customer Created"})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
