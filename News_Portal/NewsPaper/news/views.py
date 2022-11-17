from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Author, Post, Category, Comment
from .filters import PostFilter
from .forms import ArticleForm, NewsForm


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if user not in category.subscribers.all():
        category.subscribers.add(user)
        message = 'Successfully subscribed to '
    else:
        message = 'You are already subscribed to '
    return render(request, 'subscribe.html', {'category': category, 'message': message})


def limit_notify(post):
    author = post.author.authorUser.id
    today = datetime.today().day
    today_posts = Post.objects.filter(time_add__day=today, author=author)
    print('fuck you')
    if len(today_posts) >= 3:
        print('fuck you')
        post.full_clean()
        success_url = '/limit_exceed/'
        return success_url
    else:
        return False


class PostsList(ListView):
    model = Post
    ordering = '-time_add'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_post'
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'news.change_post'
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'news.delete_post'
    model = Post
    template_name = 'post_delete.html'


class NewsList(PostsList, ListView):
    pass


class NewsDetail(PostDetail, DetailView):
    pass


class NewsCreate(PostCreate, CreateView):
    form_class = NewsForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'N'
        if link := limit_notify(post):
            return HttpResponseRedirect(link)
        else:
            result = super().form_valid(form)
            return result


class NewsUpdate(PostUpdate, UpdateView):
    form_class = NewsForm


class NewsDelete(PostDelete, DeleteView):
    success_url = reverse_lazy('news_list')


class ArticlesList(PostsList, ListView):
    pass


class ArticleDetail(PostDetail, DetailView):
    pass


class ArticleCreate(PostCreate, CreateView):
    form_class = ArticleForm
    success_url = None

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'N'
        if link := limit_notify(post):
            return HttpResponseRedirect(link)
        else:
            result = super().form_valid(form)
            return result


class ArticleUpdate(PostUpdate, UpdateView):
    form_class = ArticleForm


class ArticleDelete(PostDelete, DeleteView):
    success_url = reverse_lazy('articles_list')


class AuthorsList(ListView):
    model = Author
    ordering = 'authorUser'
    template_name = 'authors.html'
    context_object_name = 'authors'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'author'


class CategoriesList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'categories.html'
    context_object_name = 'categories'


class CategoryNewsList(ListView):
    model = Post
    template_name = 'categories_news_list.html'
    context_object_name = 'categories_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(categories=self.category).order_by('-time_add')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'


class CommentsList(ListView):
    model = Comment
    ordering = 'time_add'
    template_name = 'comments.html'
    context_object_name = 'comments'


class CommentDetail(DetailView):
    model = Comment
    template_name = 'comment.html'
    context_object_name = 'comment'

