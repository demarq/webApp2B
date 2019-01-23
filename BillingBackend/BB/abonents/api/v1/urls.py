from django.urls import include, re_path, path

from .views import AbonentsViews

urlpatterns = [
    re_path(r'^(?P<id>[0-9]+)/$', AbonentsViews.as_view(), name='abonents'),

]