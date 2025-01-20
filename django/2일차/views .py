from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import path
from bookmark.models import Bookmark
#메인 알고리즘


def bookmark_list(request):
    # return HttpResponse('<h1>북마크 리스트 페이지입니다.</h1>')
    # 생성된 테이블의 내용(models)을 가지고 와야함! objects.all()=SELECT * FROM 테이블명
    bookmakrs = Bookmark.objects.filter(id__gte=50)
    context = {
        'bookmakrs': bookmakrs,
    }
    return render(request,'bookmark_list.html', context)

def bookmark_detail(request,pk): #id를 사용해도 되지만 DB를 연결한다는 생각으로 장고는 거의 PK를 사용한다 함,
    #bookmark 받아오기.(만약 pk값이 존재하지 않는 다른 값을 가지고 오게되면 유저에러400번대 나게 하는 법)
    #1번째 try:except구문
    # try:
    #     bookmark = Bookmark.objects.get(pk=pk)
    #     #get은 무조건 하나만 가져와야함. 다른것을 가지고 오게되면 무조건 400번대 에러가 나게.
    # except:
    #     raise Http404
    #2번째 get_object_or_404클래스
    #Bookmark테이블의 pk값을 가지고 오는데 만약 이 값이 아니라면 오류를!

    bookmark = get_object_or_404(Bookmark, pk=pk)

    context = {'bookmark':bookmark}
    return render(request,'bookmark_detail.html', context)

