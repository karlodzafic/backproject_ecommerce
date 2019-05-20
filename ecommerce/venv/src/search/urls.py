from django.urls import path
from django.conf.urls import url

from django.urls import re_path


from .views import (SearchProductListView)

urlpatterns = [


	path('',SearchProductListView.as_view(),name='query'),



]
