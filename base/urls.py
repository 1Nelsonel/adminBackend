from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import HomeView, LogoutView, Members, MemberDetail
urlpatterns = [

    # ================================================================================
    # auth 
    # ================================================================================
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('logout/', LogoutView.as_view(), name ='logout'),

    # ================================================================================
    # home
    # ================================================================================
    path('home/', HomeView.as_view(), name='home'),

    # ================================================================================
    # member
    # ================================================================================
    path('members/', Members.as_view(), name='members'),
    path('member/<str:str>/', MemberDetail.as_view(), name='memberDetail'),
]