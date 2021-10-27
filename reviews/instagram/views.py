from email import message
from xml.etree.ElementTree import PI
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import YearArchiveView, CreateView, ListView, DetailView, ArchiveIndexView, UpdateView, DeleteView
from django.http import HttpResponse, HttpRequest
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .models import Post
from instagram.forms import PostForm


 
# Create your views here.

# 포스트 만드는 부분
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.info(self.request, "포스트를 저장했습니다.")
        return super().form_valid(form)

post_new = PostCreateView.as_view()

# @login_required
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit = False)
#             post.author = request.user # 현재 로그인 User Instance
#             post.save()
#             messages.info(request, "포스트를 저장했습니다.")
#             return redirect(post)
#     else:
#         form = PostForm()

#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': None
#     })


# 포스트 수정하는 부분
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, "포스트를 수정했습니다.")
        return super().form_valid(form)

post_edit = PostUpdateView.as_view()

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     # 작성자 Check Tip
#     if post.author != request.user:
#         messages.error(request, '작성자만 수정할 수 있습니다.')
#         return redirect(post)
    
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             messages.info(request, "포스트를 수정했습니다.")
#             return redirect(post)
#     else:
#         form = PostForm(instance = post)

#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': post
#     })


# 포스트 삭제 부분

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # 방법1
    # success_url = './instagram/'

    # 방법2
    # def get_success_url(self):
    #     return reverse('instagram:post_list')

    # 방법3
    success_url = reverse_lazy('instagram:post_list')

post_delete = PostDeleteView.as_view()

# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         messages.success(request, '포스팅을 삭제했습니다.')
#         return redirect('instagram:post_list')
#     return render(request, 'instagram/post_confirm_delete.html', {
#         'post': post
#     })

# 로그인 기능

# 여러가지 방법이 존재 요즘은 맨 위 방법을 많이 사용
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 100

post_list = PostListView.as_view()

# @method_decorator(login_required,name='dispatch')
# class PostListView(ListView):
#     model = Post
#     paginate_by = 10

# post_list = PostListView.as_view() 

# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')

#     if q:
#         qs = qs.filter(message__icontains=q)

#     # instagam/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html',{
#         'post_list': qs,
#         'q': q,
#     })

class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public = True)
        return qs

post_detail = PostDetailView.as_view()

# post_detail = DetailView.as_view(
#     model = Post,
#     queryset=Post.objects.filter(is_public = True))


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html',{
#         'post': post,
#     })





def kakao_map1(request):
    return render(request, 'kcalroad/index.html')

def kakao_map(request):
    return render(request, 'instagram/kakao_map.html')

def kakao_map2(request):
    return render(request, 'instagram/kakao_map1.html')
    
post_archive = ArchiveIndexView.as_view(model= Post, date_field='created_at')
post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at',make_object_list=True)
