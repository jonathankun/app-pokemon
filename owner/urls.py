
from django.urls import path
from . import views

urlpatterns = [
    path('owner_list/', views.owner_list, name='owner_list'),
    path('owner_search/', views.owner_search, name="owner_search"),
    path('owner_details/', views.owner_details, name="owner_detail"),

    path('owner_create/', views.owner_create, name="owner_create"),
    path('owner_delete/(?P<id_owner>[0-9]+)/$', views.owner_delete, name="owner_delete"),
    path('owner_edit/(?P<id_owner>[0-9]+)/$', views.owner_edit, name="owner_edit"),

    #Reforzamiento03
    path('owner_list_ref03_01/', views.owner_list_ref03_01, name="owner_list_ref03_01"),
    path('owner_search_ref03_02/', views.owner_search_ref03_02, name="owner_search_ref03_02"),
    path('owner_edit_ref03_01/(?P<id_owner>[0-9]+)/$', views.owner_edit_ref03_01, name="owner_edit_ref03_01"),
    path('owner_delete_ref03_01/(?P<id_owner>[0-9]+)/$', views.owner_delete_ref03_01, name="owner_delete_ref03_01"),

    #URLs para las vistas basadas en clases.
    path('owner_list_vc/', views.OwnerList.as_view(), name="owner_list_vc"),
    path('owner_create_vc', views.OwnerCreate.as_view(), name="owner_create_vc"),
    path('owner_edit_vc/(?P<pk>[0-9]+)/$', views.OwnerUpdate.as_view(), name="owner_edit_vc"),
    path('owner_delete_vc/(?P<pk>[0-9]+)/$', views.OwnerDelete.as_view(), name="owner_delete_vc"),

    path('owner_list_vc_ref03/', views.OwnerList_ref03.as_view(), name="owner_list_vc_ref03"),
    path('owner_create_vc_ref03', views.OwnerCreate_ref03.as_view(), name="owner_create_vc_ref03"),
    path('owner_edit_vc_ref03/(?P<pk>[0-9]+)/$', views.OwnerUpdate_ref03.as_view(), name="owner_edit_vc_ref03"),
    path('owner_delete_vc_ref03/(?P<pk>[0-9]+)/$', views.OwnerDelete_ref03.as_view(), name="owner_delete_vc_ref03"),

    #URLs serializers
    path('owner_list_serializer/', views.ListOwnerSerializer, name='owner_list_srr'),

    #URLs Django RestFramework
    path('owner_list_drf_def/', views.owner_api_view, name='owner_list_rf_def'),
    path('owner_detail_drf_def/<int:pk>', views.owner_detail_view, name='owner_detail_rf_def')
]