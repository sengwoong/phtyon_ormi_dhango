from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
db = {
        1: {
            'title': '제목 1', 
            'contents': 'Post 1 body', 
            'img': 'https://picsum.photos/200/300'
            },
        2: {
            'title': '제목 2', 
            'contents': 'Post 2 body', 
            'img': 'https://picsum.photos/200/300'
            },
        3: {
            'title': '제목 3', 
            'contents': 'Post 3 body', 
            'img': 'https://picsum.photos/200/300'
            },
    }
def blog_post(request, post_id):
    
    return render(request, f'blog{post_id}.html',{'db': db})


def post(request, pk):
    # db = Cafe.objects.get(pk=pk)
    if db.get(pk):
        return render(request, 'blog/post.html', {'post': db.get(pk)})
    else:
        return HTTPResponse('잘못된 접근입니다!')


def bookinfo(request):
    '''
    교육용 크롤링 페이지입니다.
    '''
    return render(request, 'blog/bookinfo.html')
