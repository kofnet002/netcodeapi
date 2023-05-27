from django.urls import path
from .views import GetCodes, CodeDetail, RegisterView, EndPoints
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import MyTokenObtainPairView

urlpatterns = [
    path('', EndPoints.as_view()),
    path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    path('codes/', GetCodes.as_view()),
    path('codes/<str:id>/', CodeDetail.as_view()),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
