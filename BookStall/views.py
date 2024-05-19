from django.contrib.auth.models import  Group
from rest_framework.views import Response
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from store.models import StoreUser
from .serializers import UserSerializer, AuthicationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API to register New users and show all users"""
    queryset = StoreUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAdminUser,]

    def update(self, request, *args, **kwargs):
        partial = True # Here I change partial to True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
class AuthenticationView(TokenObtainPairView):
    """Authentication view"""
    serializer_class = AuthicationSerializer
    permissions_classes = [permissions.AllowAny,]



