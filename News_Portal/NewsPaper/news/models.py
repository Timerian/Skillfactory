from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


# Types of posts
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


# create class Category
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


# create class Post
class Post(models.Model):
    TYPE = [
        (article, "Статья"),
        (news, "Новости")
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


# table for connect tables Post and Category
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# create class Comment
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
