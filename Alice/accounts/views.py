from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return redirect('../../admin')  # یا هر صفحه‌ی دیگری که می‌خواهید بعد از ثبت‌نام کاربر به آن منتقل شود
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
