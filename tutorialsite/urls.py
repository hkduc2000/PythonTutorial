from django.urls import path
from tutorialsite import views

APP_NAME = 'tutorialsite'

urlpatterns = [
   path('',
      views.IndexView.as_view(),
      name='index'),

   path('exercise/',
      views.ExerciseView.as_view(),
      name='exercise'),

   path('post/<int:pk>/',
      views.PostDetailView.as_view(),
      name='post_detail'),
   
    path('post/new/',
         views.CreatePostView.as_view(),
         name='post_new'),

   path('post/<int:pk>/edit/',
        views.PostUpdateView.as_view(),
        name='post_edit'),
   path('post/<int:pk>/remove/',
      views.PostDeleteView.as_view(),
      name='post_remove'),

   path('post/<int:pk>/comment/',
      views.add_comment_to_post,
      name='add_comment_to_post'),

   path('comment/<int:pk>/approve/',
      views.comment_approve,
      name='comment_approve'),

   path('comment/<int:pk>/remove/',
      views.comment_remove,
      name='comment_remove'),

    path('post/<int:pk>/exercise/',
         views.ExerciseListView.as_view(),
         name='exercise_list'),

   path('exercise/<int:pk>/',
      views.ExerciseDetailView.as_view(),
      name='exercise_detail'),

   path('exercise/new/',
         views.CreateExerciseView.as_view(),
         name='exercise_new'),
]
