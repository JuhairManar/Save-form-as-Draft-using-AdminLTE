from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_form_view, name='my_form_view'),
    path('drafts/', views.draft_list, name='draft_list'),
    path('submitted/', views.submitted_list, name='submitted_list'),
    path('edit_draft/<int:pk>/', views.edit_draft, name='edit_draft'),
    path('view_submitted/<int:pk>/', views.view_submitted, name='view_submitted'),
]
