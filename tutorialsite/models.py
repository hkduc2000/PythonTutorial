from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
   tag = models.ForeignKey(
         'tutorialsite.Tag', related_name='posts', on_delete=models.CASCADE)
   title = models.CharField(max_length=200)
   text = models.TextField()

   def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
        
   def __str__(self):
      return str(self.pk) + " " + self.title

class Comment(models.Model):
   post = models.ForeignKey(
       'tutorialsite.Post', related_name='comments', on_delete=models.CASCADE)
   author = models.CharField(max_length=200)
   text = models.TextField()
   create_date = models.DateTimeField(default=timezone.now)
   approved_comment = models.BooleanField(default=False)

   def approve(self):
      self.approved_comment = True
      self.save()

   def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

   def __str__(self):
      return str(self.pk) + " " + self.text

   
class Exercise(models.Model):
   post = models.ForeignKey(
       'tutorialsite.Post', related_name='exercises', on_delete=models.CASCADE)
   title = models.CharField(max_length=200)
   text = models.TextField()
   solution = models.TextField()
   def __str__(self):
      return str(self.pk) + " " + self.title
   
class Tag(models.Model):
   name = models.CharField(max_length=200)

   def __str__(self):
      return str(self.pk) + " " + self.name
