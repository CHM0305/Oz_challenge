
from django.shortcuts import render,redirect
from django.urls import path
from django.http import HttpResponse, Http404
from bookmark import views
from django.contrib import admin

song_list=[
    {'title':'내가 제일 잘나가유','singer':'2NE1'},
    {'title': '심장공격', 'singer': '2PM'},
    {'title':'삐까뻔쩍','singer':'걸스데이'},
    {'title': 'ABCD', 'singer': '레인보우'}
]


def main(request):
    return HttpResponse("Hello World!")
def book_list(request):
    # book_text= ''
    # for i in range(0,10):
    #     book_text += f'book {i}<br>'

    return render(request,'book.html', {'range':range(0,10)})
def book(request,num1): #받는 변수명 꼭 통일해주기
    return render(request,'book_detail.html', {'num1':num1})

def language(request, lang):
    return HttpResponse(f'<h1>{lang}언어 페이지입니다.</h1>')

def songs(request):
    # song_titles = [f'<a href="/song/{index}">{song["title"]}</a><br>'
    #                for index,song in enumerate(song_list)
    #                ]
    return render(request, 'songs.html', {'song_list':song_list})

def song_detail(request, num2):
    #오류를 제대로 설명하기 위한 if문/에러를 지정해주지 않으면 무조건 서버측 에러 500번대가 나타남.
    if num2 > len(song_list)-1:
        raise Http404
    #song=song_list[num2]
    context= {'song_list':song_list,'num2':num2}
    return render(request,'song.html',context)

def gugu(request,num):
    # if num < 2 :
    #     #1. 값 지정 : 0,1단은 계산해도 값이 0과 1이기 때문에, 무조건 숫자를 지정해둔다.
    #     #2. redirect 주소 지정 함수 터미널에는 302 로그가 뜸.
    #     return redirect('/gugu/2')

    context={
        'num':num,
        #html에 widthratio 넓이 구하는
        #함수 사용할때
        'results':[num*i for i in range(1,10)]
        # 'range': range(1, 10)
    }

    return render(request,'gugudan.html',context)

#0번부터 시작한다....!!!!
url_admin=[
    path('admin/', admin.site.urls),
]
url_01=[
    path('',main),
    path('book_list/', book_list),
    path("book_list/<int:num1>/", book),  #받는 변수명 꼭 통일해주기
    path("book_list/<str:lang>/",language),
    path('songs/',songs),
    path('songs/<int:num2>/', song_detail),
    path('gugu/<int:num>',gugu),
]
url_02=[
    path('bookmark/', views.bookmark_list),
    path('bookmark/<int:pk>/', views.bookmark_detail),
]

urlpatterns = url_admin + url_01 + url_02
