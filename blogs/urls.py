from django.urls import path
from blogs.views import blog_post

urlpatterns = [
    path('<int:post_id>/', blog_post),
    # 다른 URL 패턴들을 추가할 수 있습니다.
]
