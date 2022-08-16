from django.db import models
from django.contrib.auth.models import User

# 게시물 class
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hit += 1
        self.save()


# 댓글 class
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment