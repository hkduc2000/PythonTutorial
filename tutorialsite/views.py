from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView, FormView)
from tutorialsite.models import Post, Comment, Tag, Exercise
from tutorialsite.forms import PostForm, CommentForm, ExerciseForm
from django.views.generic.edit import FormMixin
from django.views import View

# Create your views here.
class TemplateView(TemplateView):
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["Tag"] = Tag.objects.all() 
       return context
   

class ListView(ListView):
   def get_context_data(self, **kwargs):
        ctx = super(ListView, self).get_context_data(**kwargs)
        ctx['Tag'] = Tag.objects.all()
        return ctx

class DetailView(DetailView):
   def get_context_data(self, **kwargs):
        ctx = super(DetailView, self).get_context_data(**kwargs) 
        ctx['Tag'] = Tag.objects.all()
        return ctx

class TemplateView(TemplateView):
   def get_context_data(self, **kwargs):
      ctx = super(TemplateView, self).get_context_data(**kwargs)
      ctx['Tag'] = Tag.objects.all()
      return ctx

class IndexView(TemplateView):
   template_name = 'tutorialsite/index.html'

class ExerciseView(TemplateView):
   template_name = 'tutorialsite/baseExercise.html'

class PostDetailView(DetailView):
   context_object_name = 'post_detail'
   model = Post

   def get_object(self):
      post = super().get_object()
      return post
      

class PostUpdateView(LoginRequiredMixin, UpdateView):
   login_url = 'login/'
   redirect_field_name = 'tutorialsite/post_detail.html'
   form_class = PostForm
   model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
   login_url = 'login/'
   redirect_field_name = 'tutorialsite/post_detail.html'
   form_class = PostForm
   model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
   model = Post
   success_url = reverse_lazy('index')


class ExerciseListView(DetailView):
   context_object_name = 'post_detail'
   model = Post
   template_name = "tutorialsite/exercise_list.html"

   def get_object(self):
      post = super().get_object()
      return post

class ExerciseDetailView(DetailView):
   context_object_name = 'exercise_detail'
   model = Exercise

   def get_object(self):
      exercise = super().get_object()
      return exercise

class CreateExerciseView(LoginRequiredMixin, CreateView):
   login_url = 'login/'
   redirect_field_name = 'tutorialsite/exercise_detail.html'
   form_class = ExerciseForm
   model = Exercise

################################
################################


def add_comment_to_post(request, pk):
   post = get_object_or_404(Post, pk=pk)
   if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
   else:
      form = CommentForm()
   return render(request, 'tutorialsite/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   comment.approve()
   return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   post_pk = comment.post.pk
   comment.delete()
   return redirect('post_detail', pk=post_pk)
