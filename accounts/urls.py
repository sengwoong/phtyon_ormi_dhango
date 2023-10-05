from django.urls import path
from accounts.views import login, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # 다른 URL 패턴을 추가할 수 있습니다.
]
