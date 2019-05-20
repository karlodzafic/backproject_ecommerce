from django.urls import path
from django.conf.urls import url

from django.urls import re_path


from .views import (ProductListView,
 	ProductDetailSlugView)

urlpatterns = [


	path('',ProductListView.as_view(),name='list'),
	url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(),name='detail'),


]

