from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from . models import Post, Category, Comment
from . forms import PostCreateForm

#  로그인 인증 decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Q
from accounts.models import CustomUser
from django.http import HttpResponseRedirect,HttpResponse


# 글 목록 조회
class PostListView(ListView):
    template_name = 'board/post_list.html'
    model = Post # post_list, object_list 이름

    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #context value들을 담는 컨테이너
        # print(context)
        paginator = context['paginator']
        page_number_range = 10 #페이지그룹에 속한 페이지 수
        # CBV에서 self.request: HttpRequest
        # request.POST : POST 방식으로 넘어온 요청파라미터 조회
        # request.GET : GET 방식으로 넘어온 요청파라미터 조회
        current_page = int(self.request.GET.get('page', 1))

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



        return context



class SearchPost(ListView):
    template_name='board/post_search.html'
    model= Post

    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #context value들을 담는 컨테이너
        # print(context)
        paginator = context['paginator']
        page_number_range = 10 #페이지그룹에 속한 페이지 수
        # CBV에서 self.request: HttpRequest
        # request.POST : POST 방식으로 넘어온 요청파라미터 조회
        # request.GET : GET 방식으로 넘어온 요청파라미터 조회
        current_page = int(self.request.GET.get('page', 1))

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



        return context



    def get_queryset(self):
        br = Post.objects.all()
        b = self.request.GET.get('b','')
        
        
        if b:
            print(b)
            br = br.filter(title__icontains=b)
            print(br)

        return br

# 글 상세 조회 (1개의 글 조회)
# template : board/post_detail.html
# post_list.html에서 링크
class PostDetailView(DetailView):
    template_name = "board/post_detail.html"
    model = Post # post, object




# 글 등록
# template: board/post_create.html
# 등록 후: 상세보기
# 링크: base.html에 메뉴
@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    template_name = 'board/post_create.html'
    form_class = PostCreateForm
    # success_url = reverse_lazy('board:list')

    def get_success_url(self):
        return reverse('board:detail', args=[self.object.pk]) # self.object: insert한 모델객체

# 글 수정
@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    template_name = 'board/post_update.html'
    form_class = PostCreateForm
    model = Post

    def dispatch(self, request, *args, **kwargs):
        # print(kwargs['pk'])
        post = Post.objects.get(pk=kwargs['pk'])
        if post.writer == CustomUser.objects.get(username = request.user.get_username()):
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(request, 'board/post_detail.html', {'post':post, "auth_error":"'해당페이지에 대한 수정 권한이 없습니다.'"})

    def get_success_url(self):
        return reverse('board:detail', args=[self.object.pk])

# 글 삭제
@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk) # 조회
    if post.writer == CustomUser.objects.get(username = request.user.get_username()):
        post.delete()
        return redirect('board:list')
    else:
        return render(request, 'board/post_detail.html', {'post':post, "auth_error":"'해당페이지에 대한 삭제 권한이 없습니다.'"})


# 댓글
@login_required
def comment_write(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get('content')

        conn_user = request.user

        Comment.objects.create(post=post, comment_writer=conn_user, comment_contents=content)
        return redirect(reverse('board:detail', args=[pk]))

@login_required
def comment_delete(request, pk):
    comment = Comment.objects.get(pk=pk)
    board_pk = comment.post.pk
    post = get_object_or_404(Post, pk=board_pk)
    if comment.comment_writer == CustomUser.objects.get(username = request.user.get_username()):
        comment.delete()
        return redirect(reverse('board:detail',  args=[board_pk]))
    else:
        return render(request, 'board/post_detail.html', {'post':post, "auth_error1":"'해당댓글에 대한 삭제 권한이 없습니다.'"})


# 좋아요 기능
def like(request, pk): 
    post = get_object_or_404(Post, id=pk)
    
    if request.user in post.like_users.all():
        #좋아요 취소
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    
    return redirect('board:detail', pk = pk)