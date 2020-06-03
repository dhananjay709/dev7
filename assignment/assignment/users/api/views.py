from rest_framework.generics import (GenericAPIView,ListAPIView, RetrieveAPIView)

from rest_framework import (generics, mixins,status)
from rest_framework.response import Response
from rest_framework.views import APIView, View

from django.http import HttpResponse, HttpResponseBadRequest

from .serializers import UserSerializer, ActivityPeriodSerializer
from users.models import User, ActivityPeriod

success_status = "success"
error_status = "error"
error_message = " An error occurred, try again in some time"
delete_message = " Deleted successfully"


class UserAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        create = self.create(request,*args,**kwargs)
        return Response(data = {"status":success_status,"message":"user created","data":create.data},status=status.HTTP_201_CREATED)

    
    def get(self, request, *args, **kwargs):
        serialized_object = UserSerializer(User.objects.all(),many=True)
        return Response(data = {"status":success_status,"message":"ok:true","members":serialized_object.data},status=status.HTTP_201_CREATED)


class UserDetailAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):

    queryset= User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        
        return get_call(self)


    def patch(self, request, *args, **kwargs):
        kwargs['partial']= True

        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):

        return delete_call(self)




class ActivityPeriodAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer

    def post(self, request, *args, **kwargs):
        create = self.create(request,*args,**kwargs)
        return Response(data = {"status":success_status,"message":"Activity Period","data":create.data},status=status.HTTP_201_CREATED)



class ActivityPeriodDetailAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):

    queryset= ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        
        return get_call(self)


    def patch(self, request, *args, **kwargs):
        kwargs['partial']= True

        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):

        return delete_call(self)