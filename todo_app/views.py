from rest_framework import generics, permissions,status
from .models import Todo,CustomUser
from .serializers import TodoSerializer,UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Todo.objects.all()
        return Todo.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(expires_at__gt=timezone.now())

    
    
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def  get_queryset(self):
        user=self.request.user
        if user.role=='admin':
            return Todo.objects.all()
        return Todo.objects.filter(owner=user)


class TokenRefreshAPIView(TokenRefreshView):
    pass


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if refresh_token:
                token = RefreshToken(refresh_token) # We won't send the refresh token to the user
                # token.blacklist() ->deprecated
                return Response({"message": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT)
            else:
                return Response({"error": "Missing refresh token"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



def custom_404(request,exception):
    response_data = {
        'error': 'Not found',
        'message': 'The requested resource was not found.'
    }
    return JsonResponse(response_data, status=404)


