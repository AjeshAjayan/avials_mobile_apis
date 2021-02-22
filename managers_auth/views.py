from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import Managers
import hashlib


# Create your views here.
class ManagerLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Login api"""
        def get_token(manager_user):
            return Token.objects.create(user=manager_user)

        if 'email' and 'password' not in request.data:
            error = {'message': 'Email and Password is required'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        try:
            email = request.data['email']
            password = request.data['password']
            manager = Managers.objects.get(email=email)
            print(hashlib.sha1(password.encode('utf-8')).hexdigest())
            print(manager.password)
            if manager:
                if not manager.is_active:
                    return Response({'message': 'You are blocked please contact admin'},
                                    status=status.HTTP_400_BAD_REQUEST)
                if manager.password is password:
                    token = get_token(manager)
                    response = {
                        'id': manager.id,
                        'email': manager.email,
                        'token': token
                    }
                    return Response(response, status=status.HTTP_200_OK)
                else:
                    return Response({'message': "Invalid username/password"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': "User not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
