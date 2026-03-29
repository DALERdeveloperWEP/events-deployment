from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer, LoginSerializer, UserDetailSerializer, TokenRefreshSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            user = User.objects.create_user(
                username=serializers.validated_data['username'],
                email=serializers.validated_data['email'],
                password=serializers.validated_data['password']
            )
            return Response({"message": "User registered successfully."}, status=201)

class LoginView(APIView):
    def post(self, request):
        serializers = LoginSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            user = User.objects.get(username=serializers.validated_data['username'])
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token), 
                }, 
                status=200
            )

class UserDetailView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        user = User.objects.filter(id=request.user.id).first()
        serializers = UserDetailSerializer(user)
        return Response(serializers.data, status=200)

class TokenRefreshView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request):
        serializers = TokenRefreshSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            refresh_token = serializers.validated_data['refresh']
            try:
                refresh = RefreshToken(refresh_token)
                access_token = str(refresh.access_token)
                return Response({"access": access_token}, status=200)
            except Exception as e:
                return Response({"error": "Invalid refresh token."}, status=400)
    

