from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,
                            null=False,
                            unique=False)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',
                               default=None)
    content = models.TextField()
    created = models.DateTimeField(verbose_name="When the post was created",
                                   auto_now=True)
    updated = models.DateTimeField(verbose_name="When the post was updated",
                                   auto_now_add=True)
    STATUS = (
        (0, "Draft"),
        (1, "Published")
    )
    status = models.IntegerField(verbose_name="Status of the post",
                                 choices=STATUS,
                                 default=1)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
