from django.db import models
from tinymce.models import HTMLField
import tinymce

# Create your models here.
class Article(models.Model):
    title = models.CharField('标题', max_length=50)
    content = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']


class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.TextField('评论内容')
    created_time = models.DateTimeField('评论时间', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.content[:20]

    class Meta:
        ordering = ['-created_time']


