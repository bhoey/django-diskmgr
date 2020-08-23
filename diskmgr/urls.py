from django.contrib import admin
from django.urls import path
from diskapp.views import disk_views, main_views, host_views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', main_views.index, name='index'),

    # Class-based Views
    path('disk/add/',            disk_views.DiskCreate.as_view(),   name='disk_create'),
    path('disk/delete/<int:pk>', disk_views.DiskDelete.as_view(),   name='disk_delete'),
    path('disk/edit/<int:pk>',   disk_views.DiskUpdate.as_view(),   name='disk_update'),

    # Function-based Views
    path('host/add',             host_views.host_add,    name='host_add'),
    path('host/edit/<int:pk>',   host_views.host_update, name='host_update'),
    path('host/delete/<int:pk>', host_views.host_delete, name='host_delete'),

]
