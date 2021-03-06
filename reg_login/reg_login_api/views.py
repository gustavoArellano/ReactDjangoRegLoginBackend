from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken

@api_view(['GET'])
def current_user(request):
    
    serializer = UserSerializer(request.user)

    return Response(serializer.data)

class UserList(APIView):
    
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format = None):

        serializer = UserSerializerWithToken(data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, print("User created successfully!!!"))
        
        return Response(serializer.errors, print("Something went wrong in create!!!"))

