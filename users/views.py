from rest_framework.views import APIView
from .serializers import UserSerializer,UserlistSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User

# Create your views here.
class UserViews(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserlistViews(APIView):
    def get(self,request):
        queryset=User.objects.all()
        serializer=UserlistSerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserupdateViews(APIView):
    def put(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserlistSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDeleteView(APIView):
    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            user.delete()  
            return Response({'msg': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
