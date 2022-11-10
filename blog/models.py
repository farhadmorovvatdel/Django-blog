from django.db import models
from django.contrib.auth.models import User
from django.utils.text import  slugify
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'



class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_blog')
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.BooleanField(default=False)
    image=models.ImageField(upload_to='blogs/',blank=True)
    description=RichTextUploadingField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories',null=True)
    def __str__(self):
        return  f'{self.user.username}-{self.title}'

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        return super(Blog, self).save(*args,**kwargs)

    class Meta:
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogs'

    def TotalComments(self):
        total=self.postcomment.count()
        return total

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usercomment',null=True)
    post= models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='postcomment',null=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.post.title}'






