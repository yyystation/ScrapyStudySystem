import random

from django.db.models import Max, Count
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
    recent = Media.objects.all().order_by("?")[:10]
    # categories = Media.objects.values("tag").distinct().order_by("?")[:10]
    categories = Media.objects.values("tag").annotate(pic_url=Max("pic_url")).all().order_by("pic_url")[:10]
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
        "designs": design,
        "categories": categories
    }

    for media in recent:
        media.url = media.url + "?quality=50&w=800"
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


def categories(request):
    recent = Media.objects.all().order_by("?")[:10]
    if request.GET.get("tag") is None:
        tag = "Future"
    else:
        tag = request.GET.get("tag")
    if request.GET.get("page") is None:
        page = 1
    else:
        page = int(request.GET.get("page"))
    menu = Media.objects.filter(tag=tag)
    menu_count = len(menu)
    menu_num = int(menu_count / 12 + 1)
    menu_num = [i + 1 for i in range(menu_num)]
    newest_menu = Media.objects.all().order_by("update_time")
    tag_menu = Media.objects.values("tag").annotate(tag_num=Count("tag")).all()
    result = {
        "recents": recent,
        "tag": tag,
        "menu": menu[(page - 1) * 12:page * 12],
        "menu_num": menu_num,
        "page": page,
        "menu_count": menu_count,
        "tag_menu": tag_menu,
        "newest_menu": newest_menu
    }
    return render(request, "categories.html", result)


def single(request):
    media_id = request.GET.get("media_id")
    media = Media.objects.filter(media_id=media_id).all()[0]
    Media.objects.filter(media_id=media_id).update(view_num=media.view_num + 1)
    result = {
        "media": media
    }
    return render(request, "single-video-v1.html", result)


def like_media(request):
    media_id = request.GET.get("media_id")
    media_id = int(media_id)
    media = Media.objects.filter(media_id=media_id).all()[0]
    Media.objects.filter(media_id=media_id).update(like_num=media.like_num + 1)
    result = {
        "media": media
    }
    return render(request, "single-video-v1.html", result)


def register(request):
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