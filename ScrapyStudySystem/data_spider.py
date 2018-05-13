# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 0007 15:03
# @Author  : yyy
import requests
import time


def get_video_data_from_ted():
    talk_url = "https://www.ted.com/topics/combo?models=Talks"
    print(talk_url)
    try:
        response = requests.get(talk_url)
        print(response)
        datas = response.json()
        talk_datas = []
        for data in datas:
            talk_datas.append(data["label"])
    except Exception as e:
        print(e)
    else:
        for talk_data in talk_datas:
            url = "https://www.ted.com/playlists/browse.json?topics=%s" % talk_data
            url = url.replace(" ", "+")
            try:
                response = requests.get(url)
                print(response)
                datas = response.json()
                media_info = {}
                for data in datas:
                    title = data["title"]
                    url = data["url"]
                    pic_url=data["thumb"]
            except Exception as e:
                print(e)
            else:
                print(url)
                print(datas)
                time.sleep(10)


if __name__ == '__main__':
    get_video_data_from_ted()
