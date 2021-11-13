from zzcore import StdAns
import requests


class Ans(StdAns):
    def GETMSG(self):
        # print('https://api.devopsclub.cn/api/icpquery?url=' + self.parms[1])
        r = requests.get(url='https://api.devopsclub.cn/api/icpquery?url=' + self.parms[1]).json()
        if r['code'] == 0:
            organizer_name = r['data']['organizer_name']
            organizer_nature = r['data']['organizer_nature']
            recording_license_number = r['data']['recording_license_number']
            site_name = r['data']['site_name']
            if r['data']['site_index_url'] == '':
                site_index_url = ''
            else:
                site_index_url = '网站首页地址：' + r['data']['site_index_url']
            msg = '主办单位名称：' + organizer_name + '\n' + \
                  '主办单位性质：' + organizer_nature + '\n' + \
                  '网站备案/许可证号：' + recording_license_number + '\n' + \
                  '网站名称：' + site_name + '\n' + \
                  site_index_url
        else:
            msg = '可能是查询接口坏掉了，可不是咱！'
        return msg
