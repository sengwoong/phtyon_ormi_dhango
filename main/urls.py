from django.urls import path
from main.views import about, contact, index

urlpatterns = [
    path('', index, name='index'),  # 루트 URL 패턴
    path('about/', about, name='about'),  # '/about/' URL 패턴
    path('contact/', contact, name='contact'),  # '/contact/' URL 패턴
]

