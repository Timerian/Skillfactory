# adding Users
rick = User.objects.create_user('Rick')
morty = User.objects.create_user('Morty')

# creating objects of Author class
r = Author.objects.create(authorUser=rick)
m = Author.objects.create(authorUser=morty)

# creating four categories of posts
c1 = Category.objects.create(name='Adventure')
c2 = Category.objects.create(name='Do not do that!')
c3 = Category.objects.create(name='Drunk Rick')
c4 = Category.objects.create(name='Plumbus')

# creating three posts with adding categories for it
p1 = Post.objects.create(type='N', head='Amazing Mega Seeds',
                    text='Yesterday Morty was hidden the Mega Trees seeds in his rectum. '
                         'And then suffered in convulsions.',
                    author=r)

Post.objects.get(head='Amazing Mega Seeds').categories.add(c1)
Post.objects.get(head='Amazing Mega Seeds').categories.add(c2)

p2 = Post.objects.create(type='A', head='Fucking squirrels',
                    text='Never try to eavesdrop on squirrels. This could end badly.',
                    author=m)

Post.objects.get(head='Fucking squirrels').categories.add(c2)

p3 = Post.objects.create(type='A', head='He was insane',
                    text='Tonight my drunk grandfather almost destroyed the entire planet.',
                    author=m)

Post.objects.get(head='He was insane').categories.add(c1)

# creating comments for posts and comments
com1 = Comment.objects.create(text='Fuck you, Rick!', post=p1, user=morty)
com2 = Comment.objects.create(text='What are you angry about, sissy?', post=p1, user=rick)
com3 = Comment.objects.create(text="You are the worst asshole!", post=p1, user=morty)
com4 = Comment.objects.create(text='Bla bla bla...', post=p1, user=rick)
com5 = Comment.objects.create(text='Because you don’t have to climb where they don’t ask!', post=p2, user=rick)
com6 = Comment.objects.create(text='Life is shit!', post=p3, user=rick)

# making correction for rating value of posts and comments
for _ in range(10):
    p1.like()

for _ in range(6):
    p2.like()

for _ in range(8):
    p3.like()

for _ in range(2):
    com2.like()

for _ in range(99):
    com1.dislike()

for _ in range(6):
    com6.dislike()

# making updates of rating Users
r.update_rating()
m.update_rating()

# identify most rated author (his username and rating)
top_author_name_and_rating = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]
# Username
User.objects.get(id=top_author_name_and_rating.get('authorUser'))
# Rating
top_author_name_and_rating.get('ratingAuthor')

# print top post values in console
top_post_values = Post.objects.values().get(head=Post.objects.all().order_by('-rating').values('head')[0].get('head'))
top_post_text_preview = Post.objects.get(head=Post.objects.all().order_by('-rating').values('head')[0].get('head')).preview()

# values...
for k in top_post_values:
    top_post_values[k]

# ...and preview of top post text
top_post_text_preview


# print all comment of the top post
top_post = Post.objects.get(id=top_post_values['id'])
comments_top_post = top_post.comment_set.all()

for i in comments_top_post:
    i.time_add
    i.user.username
    i.rating
    i.text

