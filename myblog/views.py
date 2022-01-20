from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Comment
from .forms import CommentForm


# def myblog(request):
#    render(request, 'myblog.html', {})

class PostList(ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'myblog/myblog.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'myblog/post_detail.html'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'myblog/add_comment.html'

    def form_valid(self, form):
        post = Post.objects.filter(slug=self.kwargs['slug'])


# assuming user.username = admin is the superuser,
        form.instance.comment_owner = self.request.user
        form.instance.post_id = post[0].id
        return super().form_valid(form)

    success_url = reverse_lazy("myblog")


class EditCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'myblog/edit_comment.html'
    success_url = reverse_lazy("myblog")
