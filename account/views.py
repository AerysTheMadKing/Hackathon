
from django.contrib.auth import get_user_model
import uuid

from rest_framework import permissions
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from account import serializers
from account.models import CustomUser
from account.send_mail import send_confirmation_email, send_password
from account.serializers import ForgotPasswordSerializer

User = get_user_model()


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):

        serializer = serializers.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email(user.email, user.activation_code)
            except:
                return Response({'msg': 'Registered, but troubles with email!', 'data': serializer.data}, status=201)


        return Response(serializer.data, status=201)



class ActivationView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ActivationSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Successfully activated!', status=200)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)



class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ForgotPasswordView(APIView):
    permission_classes = (permissions.AllowAny,)
    @staticmethod
    def post(request):
        email = request.data['email']
        assert '@' in email
        user = CustomUser.objects.get(email=email)
        if user.forgot_password_reset != '':
            return Response({'msg': 'проверьте почту!'}, status=201)
        user.forgot_password_reset = uuid.uuid4()
        user.save()
        send_password(user.email, user.forgot_password_reset)
        return Response({'msg': 'код для сброса отправлен на почту!'}, status=200)


    @staticmethod
    def put(request):
        try:
            serializer = serializers.ForgotPasswordSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        except User.DoesNotExist:
            return Response({'неверный код'}, status=400)
        return Response({'Поздравляю вы успешно поменяли свой пароль'}, status=201)