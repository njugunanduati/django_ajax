from django.urls import path, include
from django.views.generic.base import TemplateView
from rooms import views

urlpatterns = [
    path('rooms/', TemplateView.as_view(template_name="rooms/main.html"), name='room_main'),
    path('rooms/list', views.RoomList.as_view(), name='room_list'),
    path('rooms/create', views.RoomCreate.as_view(), name='room_create'),
    path('rooms/update/<int:pk>', views.RoomUpdate.as_view(), name='room_update'),
    path('rooms/delete/<int:pk>', views.RoomDelete.as_view(), name='room_delete'),
    path('rooms/<int:pk>', views.RoomDetail.as_view(), name='room_detail'), 
]