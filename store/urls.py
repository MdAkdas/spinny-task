from django.urls import path
from .api import BoxCreateApi, BoxListApi, BoxUpdateApi, BoxDeleteApi, MyBoxListApi

urlpatterns = [

    path('api/add_box', BoxCreateApi.as_view()),
    path('api/list_boxes', BoxListApi.as_view()),
    path('api/list_my_boxes', MyBoxListApi.as_view()),
    path('api/update_box/<int:pk>', BoxUpdateApi.as_view()),
    path('api/delete_box/<int:pk>', BoxDeleteApi.as_view()),

]