from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
import views


urlpatterns = patterns('',


    url(r'^register/$',views.register_view),
    url(r'^login/$',views.login_view),
    url(r'^logout/$',views.logout_view),
    url(r'^reset_password/$',views.resetPassword_view),
    url(r'^category/$',views.category_list),
    url(r'^prods/$', views.product_list_for_category),

    url(r'^api/product/$', views.ProductList.as_view()),
    url(r'^api/product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^api/productsForCategory/(?P<category>.+)/$', views.ProductFilter.as_view()),



    url(r'^api/productclass/$', views.CategoryList.as_view()),
    url(r'^api/productclass/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),

    url(r'^api/aisle/$', views.AisleList.as_view()),
    url(r'^api/aisle/(?P<pk>[0-9]+)/$', views.AisleDetail.as_view()),

    url(r'^api/offer/$', views.OfferList.as_view()),
    url(r'^api/offer/(?P<pk>[0-9]+)/$', views.OfferDetail.as_view()),

    url(r'^api/store/$', views.StoreList.as_view()),
    url(r'^api/store/(?P<pk>[0-9]+)/$', views.StoreDetail.as_view()),

    url(r'^api/prod_store/$', views.ProductStoreList.as_view()),
    url(r'^api/prod_store/(?P<pk>[0-9]+)/$', views.ProductStoreDetail.as_view()),

    url(r'^api/customer/$', views.CustomerList.as_view()),
    url(r'^api/customer/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),

    url(r'^api/prod_store/$', views.ProductStoreList.as_view()),
    url(r'^api/prod_store/(?P<pk>[0-9]+)/$', views.ProductStoreDetail.as_view()),

    url(r'^api/sensor/$', views.SensorList.as_view()),
    url(r'^api/sensor/(?P<pk>[0-9]+)/$', views.SensorDetail.as_view()),

    url(r'^api/sales/$', views.SalesFactList.as_view()),
    url(r'^api/sales/(?P<pk>[0-9]+)/$', views.SalesFactList.as_view()),



)


urlpatterns=format_suffix_patterns(urlpatterns)
