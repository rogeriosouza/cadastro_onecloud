from django.conf.urls import include, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.post_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)	