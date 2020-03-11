from rest_framework import routers
from django.conf.urls import url
from flicker_user import views


router = routers.SimpleRouter(trailing_slash=False)
urlpatterns = [
    url(r'^load_data$', views.load_data, name='load_data'),
]