from django.urls import path
from .views import AllCodes, CodeDetail, RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('codes/', AllCodes.as_view()),
    path('codes/<str:id>/', CodeDetail.as_view()),
]