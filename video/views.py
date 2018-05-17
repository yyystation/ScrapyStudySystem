import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from video.models import User, Media

from video.models import User
import datetime


def check_username(username):
    cur_user = User.objects.filter(username=username)
    if len(cur_user) != 0:
        return False
    else:
        return True


def write_data_to_database(username, password, name, email, phone):
    cur_time = datetime.datetime.now()
    try:
        User.objects.create(username=username, password=password, name=name, email=email, phone=phone,
                            create_time=cur_time)
    except Exception as e:
        print(e)
        return False
    else:
        return True


def index(request):
    recent = Media.objects.all().order_by("?")[:3]
    art_1 = Media.objects.filter(tag="Art").order_by("url")[:4]
    art_2 = Media.objects.filter(tag="Art").order_by("pic_url")[:4]
    art_3 = Media.objects.filter(tag="Art").order_by("title")[:4]
    art_4 = Media.objects.filter(tag="Art").order_by("view_num")[:4]
    recommend_1 = Media.objects.order_by("?")[:4]
    recommend_2 = Media.objects.order_by("?")[:4]
    design_1 = Media.objects.filter(tag="Design").order_by("?")[:4]
    design_2 = Media.objects.filter(tag="Design").order_by("?")[:4]
    recommend = [recommend_1, recommend_2]
    design = [design_1, design_2]
    art = [art_1, art_2, art_3, art_4]
    result = {
        "recents": recent,
        "arts": art,
        "recommends": recommend,
        "designs":design
    }

    for media in recent:
        media.url = media.url + "?quality=50&w=800"
        print(media.url)
    return render(request, "index.html", result)


def search(request):
    print(request.method)
    params = request.POST
    username = params.get("username")
    password = params.get("password")
    cur_user = User.objects.filter(username=username, password=password)
    print(cur_user)
    if len(cur_user) != 0:
        result = "login success"
    else:
        result = "login failed"
    ctx = {}
    ctx["result"] = result
    ctx["email"] = User.objects.get("email")
    return render(request, "result.html", ctx)


def sign_up(request):
    if request.method == "GET":
        return render(request, "sign/sign_up.html")
    params = request.POST
    username = params.get("username")
    password = params.get("password")
    password_again = params.get("password_again")
    name = params.get("name")
    email = params.get("email")
    phone = params.get("phone")
    flag = True
    sign_error_info = {}
    if username is not None:
        flag = check_username(username)
    if flag == False:
        result = "username 重复"
        sign_error_info["result"] = result
        return render(request, "sign/sign_failed.html", sign_error_info)
    if len(password_again) == 0 or len(password) == 0 or len(name) == 0 or len(phone) == 0 or len(email) == 0:
        result = "输入数据不全，请重新输入!"
        sign_error_info["result"] = result
        return render(request, "sign/sign_failed.html", sign_error_info)
    if password_again != password:
        result = "两次密码输入不一致"
        sign_error_info["result"] = result
        return render(request, "sign/sign_failed.html", sign_error_info)
    write_flag = write_data_to_database(username, password, name, email, phone)
    if write_flag:
        return render(request, "sign/sign_succ.html")
    else:
        result = "服务器未知错误，请与管理员联系！"
        sign_error_info["result"] = result
        return render(request, "sign/sign_failed.html", sign_error_info)
