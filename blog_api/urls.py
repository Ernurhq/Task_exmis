from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
def redirect_to_posts(request):
    return redirect('/api/posts/')

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('', redirect_to_posts),  # <-- вот он
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

