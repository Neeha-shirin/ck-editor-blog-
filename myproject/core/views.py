from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('core/student_dashboard')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BlogForm()

    blogs = Blog.objects.all()
    return render(request, 'admin_dashboard.html', {'form': form, 'blogs': blogs})


@login_required
def student_dashboard(request):
    blogs = Blog.objects.all()
    return render(request, 'student_dashboard.html', {'blogs': blogs})


def login_redirect(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    else:
        return redirect('student_dashboard')
    
    
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')



