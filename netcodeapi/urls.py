from django.urls import path
from .views import GetCodes, CodeDetail, RegisterView, LoginView, EndPoints

urlpatterns = [
    path('', EndPoints.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('codes/', GetCodes.as_view()),
    path('codes/<str:id>/', CodeDetail.as_view()),
]