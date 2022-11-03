from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author, Post, Category, Comment
from .filters import PostFilter
from .forms import ArticleForm, NewsForm
from django.contrib.auth.mixins import PermissionRequiredMixin


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
    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     post.type = 'A'
    #     return super().form_valid(form)


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
        return super().form_valid(form)


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

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'A'
        return super().form_valid(form)


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


