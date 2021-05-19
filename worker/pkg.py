import requests

from zzcore import StdAns


class Ans(StdAns):
    #AllowGroup = [874769998,596678277,7343311]

    def GETMSG(self):
        if len(self.parms) < 1:
            msg = '请输入包名 如：/pkg linux'
            return msg
        elif self.parms[1] == 'help':
            msg = '使用 /pkg 包名 查询Core, Extra, Testing, Multilib, Multilib-Testing, ' \
                  'Community, Community-Testing仓库的软件'
            return msg
        else:
            req = requests.get(
                url='https://archlinux.org/packages/search/json/?name=' + self.parms[1] + '&arch=x86_64').json()
            if req['results'] == []:
                req = requests.get(url='https://aur.archlinux.org/rpc/?v=5&type=search&arg=' + self.parms[1]).json()
                if req['resultcount'] == 0:
                    req = requests.get(url='https://aur.archlinux.org/rpc/?v=5&type=search&arg=' + self.parms[1]).json()
                # print(req)
                if req['resultcount'] > 0:
                    name = '包名：' + req['results'][0]['Name']
                    # pkgname = req['results'][0]['pkgname']
                    version = '版本：' + req['results'][0]['Version']
                    description = '描述：' + req['results'][0]['Description']
                    maintainer = '维护：' + req['results'][0]['Maintainer']
                    numvotes = '投票：' + str(req['results'][0]['NumVotes'])

                    url = req['results'][0]['URL']
                    if url is None:
                        url = '链接：None'
                    else:
                        url = '链接：' + url
                    msg = '仓库：AUR\n' + name + '\n' + version + '\n' + description + '\n' + maintainer \
                          + '\n' + numvotes + '\n' + url + '\n'
                    return msg
            else:
                repo = req['results'][0]['repo']
                pkgname = req['results'][0]['pkgname']
                pkgver = req['results'][0]['pkgver']
                pkgdesc = req['results'][0]['pkgdesc']
                url = req['results'][0]['url']
                # return repo,pkgname,pkgver,pkgdesc,url
                # print('仓库：' + repo + '\n包名：' + pkgname + '\n版本：' + pkgver + '\n描述：' + pkgdesc + '\n上游：' + url + '\n')
                msg = '仓库：' + repo + '\n包名：' + pkgname + '\n版本：' + pkgver + '\n描述：' + pkgdesc + '\n上游：' + url + '\n'
                return msg

