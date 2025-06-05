from django.urls import path
from . views import UserViews,UserlistViews,UserDeleteView,UserupdateViews

urlpatterns = [
    path('create/',UserViews.as_view(),name='create'),
    path('userlist/',UserlistViews.as_view(),name='userlist'),
    path('user/delete/<int:id>/',UserDeleteView.as_view(),name='userdelete'),
    path('userupdate/<int:id>/',UserupdateViews.as_view(),name='userupdate'),
  
  

  
  
  
]