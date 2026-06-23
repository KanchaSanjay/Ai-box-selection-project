from django.urls import path
from .views import box_recommendation

urlpatterns = [
    path('recommend-box/', box_recommendation),
]
