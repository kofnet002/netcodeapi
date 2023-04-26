from django.urls import path
from .views import AllCodes, CodeDetail, RegisterView

urlpatterns = [
    path('sign-up/', RegisterView.as_view()),
    path('codes/', AllCodes.as_view()),
    path('codes/<str:id>/', CodeDetail.as_view()),
]