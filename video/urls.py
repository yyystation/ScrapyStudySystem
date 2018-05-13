# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 0003 14:50
# @Author  : yyy
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import video

urlpatterns = [
    url(r'^index$', "video.views.index")
]
