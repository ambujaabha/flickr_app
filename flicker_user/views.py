from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from . serializers import ListUserSerializer
from . models import FlickerUser

import requests

from .serializers import CreateUserSerializer
import code
import json, sys

CLIENT_ID = 'JRJsNQj5KLNge89ogSzdOGcYaL627ThElS25ltm9'
CLIENT_SECRET = 'tLspLYQISe4bMuOQHCqoXA84VEOYFDA2RcOCgOzFkhx2t0NKvSXzJDw9wu73DOxiJG8OZzVLlkehtYUXxKQ7roZ6o0byiPCmuRdGc4Cyc3A7XRVduN7GuwhKrbvYIAbv'


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer 
    serializer = CreateUserSerializer(data=request.data) 
    # Validate the data
    # code.interact(local=dict(globals(), **locals()))
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save() 
        # Then we get a token for the created user.
        # This could be done differentley 
        r = requests.post('http://127.0.0.1:8000/o/token/', 
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        # code.interact(local=dict(globals(), **locals()))
        return Response(r.json())
    return Response(serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post(
    'http://127.0.0.1:8000/o/token/', 
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())



@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
    'http://127.0.0.1:8000/o/token/', 
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://127.0.0.1:8000/o/revoke_token/', 
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    return Response(r.json(), r.status_code)

class ListUsers(generics.ListAPIView):
    queryset = FlickerUser.objects.all()
    serializer_class = ListUserSerializer

class CreateUser(generics.CreateAPIView):
    queryset = FlickerUser.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(CreateUser, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created user.",
                    "result": request.data}
        return Response(response)





