from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime


# Types of posts
from django.urls import reverse

article = 'A'
news = 'N'


# create class Author
class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):

        post_rating = self.post_set.aggregate(postRating=Sum('rating'))
        post_rate = 0
        post_rate += post_rating.get('postRating')

        comment_rating = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        com_rate = 0
        com_rate += comment_rating.get('commentRating')

        x = 0
        for i in self.post_set.all():
            z = i.comment_set.aggregate(y=Sum('rating'))
            x += z.get('y')

        self.ratingAuthor = post_rate * 3 + x + com_rate
        self.save()

    def __str__(self):
        return f'{self.authorUser.username}'


# create class Category
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f'{self.name}'


# create class Post
class Post(models.Model):
    TYPE = [
        (article, "Article"),
        (news, "News")
    ]

    type = models.CharField(max_length=1, choices=TYPE, default=news)
    head = models.CharField(max_length=255, blank=True)
    time_add = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:30] + '...'

    def is_type(self):
        for k in self.TYPE:
            if self.type == k[0]:
                return k[1]

    def __str__(self):
        return f'Author: {self.author}\n' \
               f'Head: {self.head}\n' \
               f'Rating of post: {self.rating}\n'

    def is_category(self):
        k = ''
        for i in self.categories.all():
            if not k:
                k += f'{i.name}'
            else:
                k += f', {i.name}'
        return f'{k}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.head} | {self.category}'


class Comment(models.Model):
    text = models.TextField()
    time_add = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:30] + '...'

    def __str__(self):
        return f'{self.user.username}\n' \
               f'{self.post.head}\n' \
               f'Рейтинг публикации: {self.rating}\n' \
               f'{self.time_add}\n' \
               f'{self.preview()}'
