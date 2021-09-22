from zzcore import StdAns

from datetime import timedelta, datetime
import requests
import random


class Ans(StdAns):
    NotAllowGroup = [973510746]

    def GETMSG(self):

        if len(self.parms) < 2:
            try:
                illust = rsearch('')
            except Exception as e:
                # print(e)
                illust = {}

        elif self.parms[1] == 'help':
            msg = '/pixiv 获取昨日随机日榜\n/pixiv [关键词] 使用关键词搜索，不可以有空格哦\n/pixiv id [插画id] 获取指定插画，不可以是漫画（\n/pixiv help 展示本 help'
            return msg

        elif self.parms[1] == 'id':
            try:
                id = int(self.parms[2])
                illust = getbyid(id)
            except Exception as e:
                illust = {}

        else:
            try:
                illust = rsearch(self.parms[1])
            except Exception as e:
                illust = {}

        if illust == {}:
            msg = '[CQ:reply,id={}] 看起来什么东西出错了 >_<\n稍后再试试吧'.format(str(self.raw_msg['message_id']))
        else:
            imgid = str(illust['id'])

            imgtitle = illust['title']
            imgo = illust['image_urls']['original'].replace('https://i.pximg.net', 'https://i.pixiv.cat')
            imgl = illust['image_urls']['large'].replace('https://i.pximg.net', 'https://i.pixiv.cat')
            if self.parms[len(self.parms) - 1] == 'o':
                imgl = imgo

            msg = '[CQ:reply,id={}]咱帮你🔍找到了这个[CQ:image,file={}]\nid {}\ntitle {}\nurl {}'.format(
                str(self.raw_msg['message_id']), imgl, imgid, imgtitle, imgo)
            # .replace('https://i.pixiv.cat', 'https://pximg.sihuan.workers.dev')
            # msg =  picurl.replace('https://i.pixiv.cat', 'https://original.img.cheerfun.dev'
            return msg


def rsearch():
    r = random.randint(0, 30)

    # if s == '':
    url = 'https://api.obfs.dev/api/pixiv/rank'
    yesterday = datetime.today() + timedelta(-1)
    print(yesterday.strftime('%Y-%m-%d'))
    params = {
        'date': yesterday.strftime('%Y-%m-%d'),
        'mode': 'day',
        'page': r,
        'size': 5
    }
    # else:
        # url = 'https://api.obfs.dev/api/pixiv/illust'
        # params = {
            # 'id': s,
            # 'illustType': 'illust',
            # 'searchType': 'autoTranslate',
            # 'pageSize': 1,
            # 'page': r,
            # 'token': ''
        # }

    for _ in range(3):
        print(r)
        resp = requests.get(url=url, params=params).json()
        # if 'data' in resp:
        # if resp['illust']['type'] == 'illust':
            # if s == '':
            # params['page'] += 1
            # continue
        resp['illusts'][0]['image_urls'] = [{
            'large': resp['illusts'][0]['image_urls']['large'],
            'original': resp['illusts'][0]['meta_single_page']['original_image_url']
        }]
        # return resp['data']
        return resp['illusts']
        # return resp['data'][0]
        # params['page'] = int(params['page'] / 2)

    return {}


def getbyid(id):
    url = 'https://api.obfs.dev/api/pixiv/illust'
    params = {
        # 'type': 'illust',
        'id': id,
    }

    resp = requests.get(url=url, params=params).json()

    if 'illust' in resp and resp['illust']['type'] == 'illust':
        resp['illust']['image_urls'] = [{
            'large': resp['illust']['image_urls']['large'],
            'original': resp['illust']['meta_single_page']['original_image_url']
        }]
        return resp['illust']

    return {}
