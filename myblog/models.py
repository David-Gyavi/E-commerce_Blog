from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='myblog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments",  on_delete=models.CASCADE)
    name = models.TextField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_owner = models.ForeignKey(
        User, related_name="comment_owner", on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
