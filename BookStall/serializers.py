from django.contrib.auth.models import  Group
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from store.models import StoreUser


class AuthicationSerializer(TokenObtainPairSerializer):

      @classmethod
      def get_token(cls,user):
            token = super(AuthicationSerializer,cls).get_token(user)
            token['username']=user.username
            return token


class UserSerializer(serializers.ModelSerializer):
      class Meta:
            model = StoreUser
            fields = ['url','username','password','first_name','last_name','email','role','groups',]
            extra_kwargs = {'password': {'write_only': True}}
            read_only_fields = ['id',]

      def validate_password(self, value: str) -> str:
            return make_password(value)
      