from zzcore import StdAns
import requests


class Ans(StdAns):
    def GETMSG(self):
        r = requests.get(url='https://api.oick.cn/icp/api.php?url=' + str(self.parms[1]).lower()).json()
        if r['code'] == '200':
            organizer_name = r['主办单位名称']
            organizer_nature = r['主办单位性质']
            recording_license_number = r['网站备案/许可证号']
            site_name = r['网站名称']
            if r['网站首页网址'] == '':
                site_index_url = ''
            else:
                site_index_url = '网站首页地址：' + r['网站首页网址']
            msg = '主办单位名称：' + organizer_name + '\n' + \
                  '主办单位性质：' + organizer_nature + '\n' + \
                  '网站备案/许可证号：' + recording_license_number + '\n' + \
                  '网站名称：' + site_name + '\n' + \
                  site_index_url

        elif r['code'] == 201:
            msg = '未有此域名ICP备案记录!'
        elif r['code'] == 202:
            msg = '域名不能为空!'
        return msg
