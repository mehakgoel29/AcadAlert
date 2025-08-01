from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication
    path('', views.custom_login_view, name='login'),
    path('logout/', views.custom_logout_view, name='logout'),

   # Forgot Password URLs
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name='password_reset'),
    path('password_reset_done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('reset_done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
         name='password_reset_complete'),
    # User views
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('create-notice/', views.create_blog, name='create_blog'),
    path('my-blogs/', views.my_blogs, name='my_blogs'),
    path('user-feed/', views.user_feed, name='user_feed'),

    # Admin views
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('pending-blogs/', views.pending_blogs, name='pending_blogs'),
    path('approve-blog/<int:blog_id>/', views.approve_blog, name='approve_blog'),
    path('all-blogs/', views.all_blogs, name='all_blogs'),
    path('user-management/', views.user_management, name='user_management'),

    # Blog detail view (for both users and admins)
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),

    # Edit blog (for authors and admins)
    path('edit-blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),

    # Delete blog (for authors and admins)
    path('delete-blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
