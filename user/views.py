import re

from django.http import JsonResponse

from .models import User
import bcrypt
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import jwt
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        if User.objects.filter(user_id=request.POST['user_id']).exists():
            user = User.objects.get(user_id=request.POST['user_id'])
            passwd = user.passwd.encode('utf=8')
            if bcrypt.checkpw(request.POST['password'].encode('utf=8'), passwd):
                from django.conf.global_settings import SECRET_KEY
                token = jwt.encode({"id": user.user_id}, SECRET_KEY, algorithm="HS256")
                request.session['user'] = user.user_id
                request.session['role'] = user.role
                print('test:', user.img)
                if user.img == '':
                    request.session['img'] = '/media/images/Profile_photo.png'
                else:
                    request.session['img'] = user.img.url
                # request.session['img']= user.img.url

                return redirect("list")
            return render(request, "user/login.html")
        return render(request, "user/login.html")
    else:
        return render(request, "user/login.html")


def join_select(request):
    if request.session.get('user'):
        print(request.session.get('role'))
    return render(request, 'user/join_select.html')


def join_mentor(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordCheck']:
            password_not_hashed = request.POST['password']
            hashed_password = bcrypt.hashpw(password_not_hashed.encode('utf=8'), bcrypt.gensalt())
            User(
                name=request.POST['name'],
                nickname=request.POST['nickname'],
                tel=request.POST['tel'],
                birth=request.POST['birthday'],
                sex=request.POST['gender'],
                user_id=request.POST['user_id'],
                passwd=hashed_password.decode('utf=8'),
                schoolPassType=request.POST['schoolPassType'],
                student_id=request.POST['student_id'],
                school=request.POST['university'],
                department=request.POST['department'],
                status=request.POST['attending'],
                img=request.FILES.get('chooseFile'),
                role=1
            ).save()
            return redirect('login')
        return render(request, 'user/join_mentor.html')
    else:
        form = UserCreationForm
        return render(request, 'user/join_mentor.html', {'form': form})


def join_mentee(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordCheck']:
            password_not_hashed = request.POST['password']
            hashed_password = bcrypt.hashpw(password_not_hashed.encode('utf=8'), bcrypt.gensalt())
            User(
                name=request.POST['name'],
                nickname=request.POST['nickname'],
                tel=request.POST['tel'],
                birth=request.POST['birthday'],
                sex=request.POST['gender'],
                user_id=request.POST['user_id'],
                passwd=hashed_password.decode('utf=8'),
                school=request.POST['university'],
                department=request.POST['department'],
                status=request.POST['attending'],
                img=request.FILES.get('chooseFile'),
                role=2
            ).save()
            return redirect('login')
        return render(request, 'user/join_mentee.html')
    else:
        form = UserCreationForm
        return render(request, 'user/join_mentee.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('login')


def mypage(request):
    return render(request, 'user/mypage.html')


def certify(request):
    return render(request, 'user/certify.html')


def find_id(request):
    return render(request, 'user/find_id.html')


def IdCheck(request):
    print('아이디 중복 체크')
    user_id = request.GET.get('user_id')
    try:
        _id = User.objects.get(user_id=user_id)
    except:
        _id = None
    if _id is None:
        duplicate = "pass"
    else:
        duplicate = "fail"
    context = {'duplicate': duplicate}
    print('duplicate : ', duplicate)
    return JsonResponse(context)


def withdrawal(request):
    print(request.session['user'])
    user = User.objects.get(user_id=request.session['user'])
    logout(request)
    user.delete()
    return redirect('login')
