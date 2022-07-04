u1 = User.objects.create_user(username='Billy')
u2 = User.objects.create_user(username='Van')
Author.objects.create(authorUser=u1)
Author.objects.create(authorUser=u2)
author = Author.objects.get(id=1)
author = Author.objects.get(id=2)
Category.objects.create(name='Gym')
Category.objects.create(name='It')
Category.objects.create(name='Fights')
Category.objects.create(name='News')
Post.objects.create(author=author, categoryType='Ar', title='opennewgym', text='opisaniegyma')
Post.objects.create(author=author, categoryType='Ar', title='randomtitle', text='randomtext')
Post.objects.create(author=author, categoryType='NW', title='news', text='novienovosti')
Post.objects.get(id=1).post.Category.add(Category.objects.get(id=1))
Post.objects.get(id=1).post.Category.add(Category.objects.get(id=1))
Post.objects.get(id=2).post.Category.add(Category.objects.get(id=2))
Post.objects.get(id=3).post.Category.add(Category.objects.get(id=3))
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).autorUser, text='cool')
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).autorUser, text='koment')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).autorUser, text='randomtext')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).autorUser, text='wow')
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
a = Author.objects.get(id=1)
a.update_rating()
a.ratingAuthor
Post.objects.get(id=1).like()
a = Author.objects.get(id=1)
c = Author.objects.get(id=2)
a.update_rating()
a.ratingAuthor
a = Author.objects.order_by('-ratingAuthor')[:1]
a
for i in a:
    i.ratingAuthor
    i.authorUser.username
best_post = Post.objects.order_by('-rating')[:1]
Post.objects.get(id=best_post).dateCreation
Post.objects.get(id=best_post).author.authorUser.username
Post.objects.get(id=best_post).rating
Post.objects.get(id=best_post).title
Post.objects.get(id=best_post).preview()
Comment.objects.filter(commentPost_id=best_post).values('dateCreation', 'commentUser_id', 'rating', 'text')

