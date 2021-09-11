from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
from .models import Customer


def user_login(request):
    # đăng nhập
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        # người dùng đăng nhập thất bại
        messages.info(request, "đăng nhập thất bại , vui lòng thử lại !")

    return render(request, 'accounts/login.html')

def user_register(request):
    if request.method == "POST":
        # nhận dữ liệu ng dùng :
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone_field')
        #print(username, email, phone)

        # điều kiện để đăng kí :
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request," Tên người dùng đã đăng kí !")
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,"Email đã được đăng kí ! ")
                    return redirect('user_register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    data = Customer(user=user, phone_field=phone)
                    data.save()

                    # đăng nhập người dùng
                    our_user = authenticate(username=username, password=password)
                    if our_user is not None:
                        login(request, user)
                        return redirect('/')
        else:
            messages.info(request, " Hai mật khẩu điền không giống nhau")
            return redirect('user_register')

    return render(request, 'accounts/register.html')


def user_logout(request):
    # đăng xuất
    logout(request)
    return redirect('/')
