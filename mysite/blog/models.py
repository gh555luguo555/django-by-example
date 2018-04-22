from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, 
                        self).get_queryset().filter(status='published')

class Post(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    #  在SQL数据库中会被转化成VARCHAR。
    title = models.CharField(max_length=250)
    # 这个字段将会在URLs中使用。slug就是一个短标签
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                                related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                    choices=STATUS_CHOICES,
                                    default='draft')

    class Meta:
        # 查询数据库的时候默认返回的是根据publish字段进行降序排列过的结果。
        # 我们使用符号指定进行降序排列
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                    args=[self.publish.year,
                        self.publish.strftime('%m'),
                        self.publish.strftime('%d'),
                        self.slug])


