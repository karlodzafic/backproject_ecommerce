"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static
from .views import home_page,about_page,contact_page,login_page,register_page
from django.apps import apps
from django.views.generic import TemplateView
from carts.views import cart_home
# from products.views import (ProductListView,
# 	product_list_view,
# 	ProductDetailView,
# 	product_detail_view,
# 	ProductFeaturedListView,
#  	ProductFeaturedDetailView,ProductDetailSlugView)
products_name = apps.get_app_config('products').verbose_name #da bi mi radilo vezano za namespace
urlpatterns = [

	path('',home_page,name='home'),
	path('register/',register_page,name='register'),
	path('bootstrap/',TemplateView.as_view(template_name='bootstrap/example.html')),
	url(r'^products/', include(('products.urls', products_name), namespace='products')),
	url(r'^search/', include(('search.urls', products_name), namespace='search')),
	# path('featured/',ProductFeaturedListView.as_view()),
	# url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
	# path('products/',ProductListView.as_view()),
	# path('products-fbv/',product_list_view),
	# # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
	# url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
	# url(r'^products-fbv/(?P<pk>\d+)/$',product_detail_view),
	path('login/',login_page,name='login'),
	path('cart/',cart_home,name='cart'),
	path('about/',about_page,name='about'),
	path('contact/',contact_page,name='contact'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns=urlpatterns+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)