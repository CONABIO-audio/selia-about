from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(
        r'^about/',
        include(('selia_about.urls', 'selia_about')))
]
