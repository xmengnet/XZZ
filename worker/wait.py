from zzcore import StdAns
import re
import requests


class Ans(StdAns):
    def GETMSG(self):
        try:
            url = self.raw_msg['message'][1]['data']['url']
            resp = requests.get(
                f"https://trace.moe/api/search?url={url}").json()['docs'][0]
        except:
            return "There something wrong."

        video_url = f"https://media.trace.moe/video/{resp['anilist_id']}/{resp['filename']}?t={resp['at']}&token={resp['tokenthumb']}"

        m, s = divmod(float(resp['at']), 60)
        h, m = divmod(m, 60)
        print("%02d:%02d:%02d" % (h, m, s))
        text = f"{resp['title_native']}\n{resp['title_chinese']}\nEP#{resp['episode']} {h:02.0f}:{m:02.0f}:{s:02.0f}\n{resp['similarity'][:5]} similarity"

        msg = f"[CQ:video,file={video_url}]\n{text}"
        return msg