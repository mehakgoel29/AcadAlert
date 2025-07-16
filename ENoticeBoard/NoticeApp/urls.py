from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.custom_login_view, name='login'),
    path('logout/', views.custom_logout_view, name='logout'),

    # User views
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('create-blog/', views.create_blog, name='create_blog'),
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
