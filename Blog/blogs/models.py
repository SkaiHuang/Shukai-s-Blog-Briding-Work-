from django.db import models
from users.models import BlogUser
from datetime import datetime



class Post(models.Model):
    user = models.ForeignKey(BlogUser, verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=50)
    content = models.TextField('Content')
    pub_date = models.DateTimeField('Pub Date', default=datetime.now)
    cover = models.ImageField('Blog Cover', upload_to='static/images/post', default='static/images/UOB.png')
    views = models.IntegerField('Viewed Number', default=0)
    recommend = models.BooleanField('Recommend Blog', default=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name='Blog', on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, verbose_name='Author', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Pub Date', default=datetime.now)
    content = models.TextField('Content')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'



class CV(models.Model):
    user = models.ForeignKey(BlogUser, verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=50)
    content = models.TextField('Content')
    pub_date = models.DateTimeField('Pub Date', default=datetime.now)
    views = models.IntegerField('Viewed Number', default=0)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CV'

