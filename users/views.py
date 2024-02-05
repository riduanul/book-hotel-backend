from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import logout

class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user=user)
            print(token)
            # Token.Objects.create(user=user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
        
        user = authenticate(request, username= username, password= password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            print(token) 
            userInfo = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'password':user.password
            }
            return Response({'token':token.key, 'user':userInfo})
        else:
            return Response({'error': 'Invalid Credential'})

class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        print("Reached the UserLogoutView")
        print(request.headers)
        print(request.auth)
        Token.objects.filter(user=request.user.user).delete()
        logout(request)
        return Response({'detail': 'Logout successful.'}, status=status.HTTP_200_OK)



