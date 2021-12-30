from django.conf                                                import settings
from rest_framework                                             import generics, status
from rest_framework.response                                    import Response
from rest_framework.permissions                                 import IsAuthenticated
from rest_framework_simplejwt.backends                          import TokenBackend

from auth_app.models.user                                       import User
from auth_app.serializers.userSerializer                        import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)