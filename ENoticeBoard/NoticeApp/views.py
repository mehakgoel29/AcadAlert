from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Blog
from .models import Notice
from .forms import BlogForm
from .forms import NoticeForm
from django.contrib import messages


# Custom login view
def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('user_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Custom logout view
def custom_logout_view(request):
    logout(request)
    return redirect('login')

# User dashboard view
@login_required
def user_dashboard(request):
    # Sirf approved notices hi bhej rahe hain
    notices = Notice.objects.filter(approved=True).order_by('-created_at')
    return render(request, 'user_dashboard.html', {'notices': notices})



# View to create a new blog post (user side)
@login_required
def create_notice(request):
    if request.method == "POST":
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user   # logged-in user
            notice.approved = False        # by default approval pending
            notice.save()
            messages.success(request, "Notice submitted for admin approval!")
            return redirect("/user-dashboard/")  # ya kahin aur
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = NoticeForm()

    return render(request, "create_blog.html", {"form": form})


# View to display user's blogs
@login_required
def my_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'my_blogs.html', {'blogs': blogs})

# View to display approved blogs on the user feed
def user_feed(request):
    blogs = Notice.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'user_feed.html', {'blogs': blogs})



# Admin dashboard view
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

# View to display pending blogs for approval (admin side)
@user_passes_test(lambda u: u.is_superuser)
def pending_blogs(request):
    blogs = Blog.objects.filter(is_approved=False)
    return render(request, 'pending_blogs.html', {'blogs': blogs})

# View to approve a blog (admin side)
@user_passes_test(lambda u: u.is_superuser)
def approve_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.is_approved = True
    blog.save()
    return redirect('pending_blogs')

# View to display all blogs (admin side)
@user_passes_test(lambda u: u.is_superuser)
def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'all_blogs.html', {'blogs': blogs})

# View to manage users (admin side)
@user_passes_test(lambda u: u.is_superuser)
def user_management(request):
    users = User.objects.all()
    return render(request, 'user_management.html', {'users': users})

# View to display blog details (for both users and admins)
@login_required
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

# View to edit a blog (for authors and admins)
@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.user != blog.author and not request.user.is_superuser:
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

# View to delete a blog (for authors and admins)
@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.user != blog.author and not request.user.is_superuser:
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        blog.delete()
        return redirect('my_blogs')
    
    return render(request, 'delete_blog.html', {'blog': blog})


