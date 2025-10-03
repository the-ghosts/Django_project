from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created= models.DateTimeField(default=timezone.now)


    class Meta:
        ordering=('-date_created',)
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    @property
    def total_likes(self):
        return self.reactions.filter(value='like').count()

    @property
    def total_dislikes(self):
        return self.reactions.filter(value='dislike').count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete= models.CASCADE)
    comments = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.comments

REACTION_CHOICES = (
    ('like', 'Like'),
    ('dislike', 'Dislike'),
)
class Reaction(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name="reactions")
    value = models.CharField(max_length=10, choices=REACTION_CHOICES, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'post')  # user can only react once per post

    def __str__(self):
        return f"{self.user} {self.value} {self.post}"