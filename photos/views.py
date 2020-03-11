# from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Group
from .models import Photo
from .serializers import GroupSerializer
from .serializers import PhotoSerializer
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes


class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated)

    def get_queryset(self):
        user = self.request.user
        return Group.objects.filter(user=user)# so only user associated with the group can access the group record


class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        group_id = self.request.query_params.get("group")
        if group_id:
            return Photo.objects.filter(group=group_id)
        else:
            return Photo.objects.filter(group__user=user)# so only user associated with the photos can access the photo record


@permission_classes([IsAuthenticated,])
@api_view(["GET"])
def get_photo_id(self, id):
  
    user = self.user
    print(id)
    photo_list = Photo.objects.filter(group=id)# so only user associated with the photos can access the photo record
    return Response(photo_list.values("id"))
