from cube.models import User, Cube, Content,CubeUser,ContentUser,ContentCube
from cube.serializer import UserSerializer, CubeSerializer, \
    ContentSerializer,ContentCubeSerializer,CubeUserSerializer,ContentUserSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
import json


class UserView(APIView):

    """
    List all users, or create a new users.
    """

    def get(self, request=None, pk=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return HttpResponse(json.dumps(serializer.data))

    def post(self, request, pk=None):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data))
        response_msg = {'error': 'Please check url and user_id'}
        response = HttpResponse(json.dumps(response_msg))
        response.status_code = 208
        return response


class CubeView(APIView):

    """
    List all cubes given user, or create a new cube.
    """
    def get(self, request=None, user_id=None):

        cube12 = Cube.objects.filter(user_id=user_id)
        shar_cube = CubeUser.objects.filter(user_id=user_id)
        lis=[]
        for cu in shar_cube:
            lis.append(cu.cube_id.id)
        for cube1 in cube12:
            lis.append(cube1.id)
        cube = Cube.objects.filter(id__in=lis)
        serializer = CubeSerializer(cube, many=True)
        return HttpResponse(json.dumps(serializer.data))

    def post(self, request,user_id=None):
        request.DATA['user_id'] = user_id

        serializer = CubeSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data))
        response_msg = {'error': 'Please check url and user_id'}
        response = HttpResponse(json.dumps(response_msg))
        response.status_code = 208
        return response

    def delete(self, request, user_id=None, cube_id=None):
        cube = Cube.objects.filter(user_id=user_id, id=cube_id)
        cube.delete()
        response_msg = {'msg': 'delete succesfully'}
        response = HttpResponse(json.dumps(response_msg))
        response.status_code = 200
        return response


class ContentView(APIView):

    """
    List all CONTENT OF GIVEN USER, or create a new content.
    """
    def get(self, request=None, user_id=None):
        cube12 = Content.objects.filter(user_id=user_id)
        shar_cube = ContentUser.objects.filter(user_id=user_id)
        lis=[]
        for cu in shar_cube:
            lis.append(cu.content_id.id)
        for cube1 in cube12:
            lis.append(cube1.id)

        shar_cube2 = ContentCube.objects.filter(user_id=user_id)
        for cu1 in shar_cube2:
            lis.append(cu1.content_id.id)
        content = Content.objects.filter(id__in=lis)
        serializer = ContentSerializer(content, many=True)
        return HttpResponse(json.dumps(serializer.data))

    def post(self, request,user_id=None):
        request.DATA['user_id']=user_id
        serializer = ContentSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data))
        response_msg = {'error': 'Please check url and user_id'}
        response = HttpResponse(json.dumps(response_msg))
        response.status_code = 208
        return response

class AddContentToCubeView(APIView):

    """
    add content to cube and delete.
    """


    def post(self, request, user_id=None, cube_id=None):

        request.DATA['user_id']=user_id
        request.DATA['cube_id']=cube_id
        serializer = ContentCubeSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data))
        response_msg = {'error': 'Please check url and user_id'}
        response = HttpResponse(json.dumps(response_msg))
        response.status_code = 200
        return response

    def delete(self, request, user_id=None, cube_id=None, content_id=None):
        cube = ContentCube.objects.filter(user_id=user_id, cube_id=cube_id, content_id=content_id)
        cube.delete()
        response_msg = {'msg': 'delete succesfully'}
        response = HttpResponse(json.dumps(response_msg))
        response.status_code = 200
        return response

class ShareCubeWithUserView(APIView):

    """
    share cube to user .
    """

    def post(self, request, user_id=None, cube_id=None):
        request.DATA['cube_id'] = cube_id
        serializer = CubeUserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data))
        response_msg = {'error': 'Please check url and cube id'}
        response = HttpResponse(json.dumps(response_msg))
        response.status_code = 208
        return response

class ShareContentWithUserView(APIView):

    """
    share content with users.
    """

    def post(self, request, user_id=None, content_id=None):
        request.DATA['content_id'] = content_id

        serializer = ContentUserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data))
        response_msg = {'error': 'Please check url and cube id'}
        response = HttpResponse(json.dumps(response_msg))
        response.status_code = 208
        return response

