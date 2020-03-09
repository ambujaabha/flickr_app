from .models import Photo
from rest_framework import serializers
class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'user', 'group', 'description', 'date_posted', 'date_taken','date_updated','url_page' ]
