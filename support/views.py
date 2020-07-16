from django.shortcuts import  redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy

#로그인
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Post
from .forms import PostCreateForm

# 글목록 조회
class PostListView(ListView):
    template_name = 'support/post_list.html'
    model = Post #post_list, object_list 이름

#글 상세조회 (1개의 글 조회)
#template : board/post_detail.html
class PostDetailView(DetailView):
    template_name = 'support/post_detail.html'
    model = Post

#글 등록, 등록후 상세보기
@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    template_name = 'support/post_create.html'
    form_class = PostCreateForm
    # success_url = reverse_lazy('board:list') #class에서 sucessurl에서는 reverselazy써야함

    def get_success_url(self):
        return reverse('support:detail',args=[self.object.pk]) #self.object : insert한 모델객체

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    template_name = 'support/post_update.html'
    form_class = PostCreateForm
    model = Post  #update는 create와 다르게 폼을 만들때 조회를 해야하기때문에 모델을 지정해주어야함

    def get_success_url(self):
        return reverse('support:detail',args=[self.object.pk]) #self.object : insert한 모델객체

#글삭제
@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk) #조회
    post.delete()
    return redirect('support:list')