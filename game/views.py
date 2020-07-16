from django.shortcuts import  redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse, reverse_lazy

from board.models import CustomUser

#로그인
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator

from .models import Game, Genre_list, Comment
from .forms import GameCreateForm

from django.db.models import Q

# 글목록 조회

def game_list(request):
    paginate_by = 15
    context = {}

    context['is_paginated'] = True

    # print(context)
    all_games = Game.objects.all()
    paginator = Paginator(all_games, paginate_by)
    page_number_range = 10 #페이지그룹에 속한 페이지 수
    # CBV에서 self.request: HttpRequest
    # request.POST : POST 방식으로 넘어온 요청파라미터 조회
    # request.GET : GET 방식으로 넘어온 요청파라미터 조회
    current_page = int(request.GET.get('page', 1))
    context['current_page'] = current_page

    #시작/끝 index 조회
    start_index = int((current_page-1)/page_number_range)*page_number_range
    end_index = start_index + page_number_range

    # 현재 페이지가 속한 페이지 그룹의 범위
    current_page_group_range = paginator.page_range[start_index : end_index]
    print("current_page_group_range", current_page_group_range)

    start_page = paginator.page(current_page_group_range[0])
    end_page = paginator.page(current_page_group_range[-1])

    has_previous_page = start_page.has_previous()
    has_next_page = end_page.has_next()

    context['current_page_group_range'] = current_page_group_range
    if has_previous_page: #이전페이지 그룹이 있다면
        context['has_previous_page'] = has_previous_page
        context['previous_page'] = start_page.previous_page_number

    if has_next_page: #다음 페이지 그룹이 있다면
        context['has_next_page'] = has_next_page
        context['next_page'] = end_page.next_page_number

    ########## 장르 리스트 ###############
    genre_list = Genre_list.objects.all()
    context['genre_list'] = genre_list

    # pricelist = game.objects.all()
    # price = min(d,d,d,.)
    # context['price']
    e = paginate_by * current_page
    s = e - paginate_by
    print("내용 index", s, e)
    game_list = Game.objects.all()[s:e]

    # 최저가
    min_price_list = []
    for game in game_list:
        min_price = [game.steam, game.origin, game.uplay, game.epic_games, game.drmfree]
        min_price = min([p for p in min_price if p is not 0])
        # print(min_price)
        min_price_list.append(min_price)
    # context['min_price'] = min_price_list
    context['game_lowest_price'] = zip(game_list, min_price_list)

    return render(request, 'game/game_list.html', context)
 
def game_search(request):
    paginate_by = 15
    context = {}
    game_list = Game.objects.all()

    b = request.GET.get('b','') #검색에서 입력한 값이 넘어옴
    f = request.GET.getlist('f') #장르 체크박스 입력한 데이터 값들이 넘어옴(getlist -> 여러개 받을 수 있음)
    price = request.GET.get('price','')
    print(price)

    # if b and f: #만약 b(검색창에서 넘어온 값)와 f(필터 체크박스에서 넘어온 값)가 둘다 있다면
    #     print(b,f)
    #     query = Q() #Q()조건절 만들어줌
    #     br = br.filter(Q(title__icontains=b)| Q(developer__icontains = b)) #b(검색창에서 입력한 값)이 title에 있거나 price에 있거나 developer에 있거나
    #     ### 만약 foreign key를 가지고 온다면 Q(genre__genre_name__icontains=b) 이런 식으로 앞에 foreign key의 원래 class와FK로 받아오는 값을 입력해야함
        
    #     for i in f: #f(필터 체크박스 입력값 ->['adventure','rpg'] 이런식으로 값이 넘어옴)
    #         query = query | Q(genre__icontains=i) #i 가 장르에 포함되어 있다면
    #         br = br.filter(query)
    if b: #b(검색창)에서 값이 넘어왔다면
        print(b)
        game_list = game_list.filter(Q(title__icontains=b)|  Q(developer__icontains = b))
    if f: #f(체크박스 필터)에서 값이 넘어왔다면
        print(f)
        query = Q()
        for i in f:
            query = query | Q(genre__icontains=i)
            game_list = game_list.filter(query)
    if price == '0':
        game_list = game_list.filter(steam__gt=0)
    elif price == '1': #price(가격필터)에서 값이 넘어왔다면
        game_list = game_list.filter(steam__lte=20000)
    elif price == '2':
        game_list = game_list.filter(steam__lte=30000)
    elif price == '3':
        game_list = game_list.filter(steam__lte=40000)        
    elif price == '4':
        game_list = game_list.filter(steam__lte=50000)
    else:
        game_list = game_list.filter(steam__gt=50000)
    
    context['is_paginated'] = True

    # print(context)
    paginator = Paginator(game_list, paginate_by)
    page_number_range = 10 #페이지그룹에 속한 페이지 수
    # CBV에서 self.request: HttpRequest
    # request.POST : POST 방식으로 넘어온 요청파라미터 조회
    # request.GET : GET 방식으로 넘어온 요청파라미터 조회
    current_page = int(request.GET.get('page', 1))
    context['current_page'] = current_page

    #시작/끝 index 조회
    start_index = int((current_page-1)/page_number_range)*page_number_range
    end_index = start_index + page_number_range

    # 현재 페이지가 속한 페이지 그룹의 범위
    current_page_group_range = paginator.page_range[start_index : end_index]
    print("current_page_group_range", current_page_group_range)

    start_page = paginator.page(current_page_group_range[0])
    end_page = paginator.page(current_page_group_range[-1])

    has_previous_page = start_page.has_previous()
    has_next_page = end_page.has_next()

    context['current_page_group_range'] = current_page_group_range
    if has_previous_page: #이전페이지 그룹이 있다면
        context['has_previous_page'] = has_previous_page
        context['previous_page'] = start_page.previous_page_number

    if has_next_page: #다음 페이지 그룹이 있다면
        context['has_next_page'] = has_next_page
        context['next_page'] = end_page.next_page_number

    ########## 장르 리스트 ###############
    genre_list = Genre_list.objects.all()
    context['genre_list'] = genre_list

    # pricelist = game.objects.all()
    # price = min(d,d,d,.)
    # context['price']
    e = paginate_by * current_page
    s = e - paginate_by
    print("내용 index", s, e)
    
    game_list = game_list[s:e]
    # 최저가
    min_price_list = []
    for game in game_list:
        min_price = [game.steam, game.origin, game.uplay, game.epic_games, game.drmfree]
        min_price = min([p for p in min_price if p is not 0])
        # print(min_price)
        min_price_list.append(min_price)
    # context['min_price'] = min_price_list
    context['game_lowest_price'] = zip(game_list, min_price_list)
    

    return render(request, 'game/game_search.html', context)

# class SearchListView(ListView):

#     template_name = 'game/game_search.html'
#     model = Game
#     paginate_by = 15


#     def get_context_data(self, **kwargs):

#         context = super().get_context_data(**kwargs) #context value들을 담는 컨테이너
#         # print(context)
#         paginator = context['paginator']
#         page_number_range = 10 #페이지그룹에 속한 페이지 수
#         # CBV에서 self.request: HttpRequest
#         # request.POST : POST 방식으로 넘어온 요청파라미터 조회
#         # request.GET : GET 방식으로 넘어온 요청파라미터 조회
#         current_page = int(self.request.GET.get('page', 1))

#         #시작/끝 index 조회
#         start_index = int((current_page-1)/page_number_range)*page_number_range
#         end_index = start_index + page_number_range

#         # 현재 페이지가 속한 페이지 그룹의 범위
#         current_page_group_range = paginator.page_range[start_index : end_index]
#         print("current_page_group_range", current_page_group_range)

#         start_page = paginator.page(current_page_group_range[0])
#         end_page = paginator.page(current_page_group_range[-1])

#         has_previous_page = start_page.has_previous()
#         has_next_page = end_page.has_next()

#         context['current_page_group_range'] = current_page_group_range
#         if has_previous_page: #이전페이지 그룹이 있다면
#             context['has_previous_page'] = has_previous_page
#             context['previous_page'] = start_page.previous_page_number

#         if has_next_page: #다음 페이지 그룹이 있다면
#             context['has_next_page'] = has_next_page
#             context['next_page'] = end_page.next_page_number

#         ## 장르 리스트
#         genre_list = Genre_list.objects.all()
#         context['genre_list'] = genre_list

#         ## PRICEEE
   


#         return context

#     def get_queryset(self):
#         br = Game.objects.all()
#         b = self.request.GET.get('b','') #검색에서 입력한 값이 넘어옴
#         f = self.request.GET.getlist('f') #장르 체크박스 입력한 데이터 값들이 넘어옴(getlist -> 여러개 받을 수 있음)
#         price = self.request.GET.get('price','')
#         print(price)

#         # if b and f: #만약 b(검색창에서 넘어온 값)와 f(필터 체크박스에서 넘어온 값)가 둘다 있다면
#         #     print(b,f)
#         #     query = Q() #Q()조건절 만들어줌
#         #     br = br.filter(Q(title__icontains=b)| Q(developer__icontains = b)) #b(검색창에서 입력한 값)이 title에 있거나 price에 있거나 developer에 있거나
#         #     ### 만약 foreign key를 가지고 온다면 Q(genre__genre_name__icontains=b) 이런 식으로 앞에 foreign key의 원래 class와FK로 받아오는 값을 입력해야함
            
#         #     for i in f: #f(필터 체크박스 입력값 ->['adventure','rpg'] 이런식으로 값이 넘어옴)
#         #         query = query | Q(genre__icontains=i) #i 가 장르에 포함되어 있다면
#         #         br = br.filter(query)
#         if b: #b(검색창)에서 값이 넘어왔다면
#             print(b)
#             br = br.filter(Q(title__icontains=b)|  Q(developer__icontains = b))
#         if f: #f(체크박스 필터)에서 값이 넘어왔다면
#             print(f)
#             query = Q()
#             for i in f:
#                 query = query | Q(genre__icontains=i)
#                 br = br.filter(query)
#         if price == '0':
#             br = br.filter(steam__gt=0)
#         elif price == '1': #price(가격필터)에서 값이 넘어왔다면
#             br = br.filter(steam__lte=20000)
#         elif price == '2':
#             br = br.filter(steam__lte=30000)
#         elif price == '3':
#             br = br.filter(steam__lte=40000)        
#         elif price == '4':
#             br = br.filter(steam__lte=50000)
#         else:
#             br = br.filter(steam__gt=50000)
#         return br


#글 상세조회 (1개의 글 조회)
class GameDetailView(DetailView):
    template_name = 'game/game_detail.html'
    model = Game

#글 등록, 등록후 상세보기
# @method_decorator(login_required, name='dispatch')
class GameCreateView(CreateView):
    template_name = 'game/game_create.html'
    form_class = GameCreateForm
    # success_url = reverse_lazy('board:list') #class에서 sucessurl에서는 reverselazy써야함

    def get_success_url(self):
        return reverse('game:detail',args=[self.object.pk]) #self.object : insert한 모델객체

# @method_decorator(login_required, name='dispatch')
class GameUpdateView(UpdateView):
    template_name = 'game/game_update.html'
    form_class = GameCreateForm
    model = Game  #update는 create와 다르게 폼을 만들때 조회를 해야하기때문에 모델을 지정해주어야함

    def get_success_url(self):
        return reverse('game:detail',args=[self.object.pk]) #self.object : insert한 모델객체

#글삭제
# @login_required
def game_delete(request, pk):
    game = Game.objects.get(pk=pk) #조회
    game.delete()
    return redirect(reverse('game:list'))

# 댓글
@login_required
def comment_write(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Game, pk=pk)
        content = request.POST.get('content')
        conn_user = request.user
        Comment.objects.create(post=post, comment_writer=conn_user, comment_contents=content)
        return redirect(reverse('game:detail', args=[pk]))
# 댓글 삭제
@login_required
def comment_delete(request, pk):

    comment = Comment.objects.get(pk=pk)
    game_pk = comment.post.pk
        
    if comment.comment_writer == CustomUser.objects.get(username = request.user.get_username()):
        comment.delete()
        return redirect(reverse('game:detail',  args=[game_pk]))
    else:
        return render(request, 'game/game_detail.html', {'comment':comment, "auth_error":"'해당댓글에 대한 삭제 권한이 없습니다.'"})

# 좋아요 기능
def like(request, pk): 
    game = get_object_or_404(Game, id=pk)
    
    if request.user in game.like_users.all():
        #좋아요 취소
        game.like_users.remove(request.user)
    else:
        game.like_users.add(request.user)
    
    return redirect('game:detail', pk = pk)