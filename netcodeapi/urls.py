from django.urls import path
from .views import AllCodes, CodeDetail

urlpatterns = [
    path('codes/', AllCodes.as_view()),
    path('codes/<str:id>/', CodeDetail.as_view()),
]