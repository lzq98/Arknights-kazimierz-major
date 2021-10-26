import requests
import time
import json

x_session_token = ""  # B服玩家不需要填写此项
uid = ""
raw_cookies = ""

address = "https://ak.hypergryph.com/activity/kazimierz-major/pullBox"
cookies = raw_cookies.split("; ")
cookie = {}
for c in cookies:
    temp = c.split("=")
    cookie[temp[0]] = temp[1]

headers = {
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en-AU;q=0.7,en;q=0.6,ja;q=0.5',
    'content-length': '29',
    'Content-Type': 'application/json;charset=UTF-8',
    'dnt': '1',
    'origin': 'https://ak.hypergryph.com',
    'referer': 'https://ak.hypergryph.com/activity/kazimierz-major?source=bilibili',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'x-session-uid': uid,
    'x-session-token': x_session_token
}


def run():
    for i in range(6):
        data = '{"box": ' + str(i) + '}'
        r = requests.post(address, data=data, cookies=cookie, headers=headers)
        time.sleep(2)
        result = json.loads(r.text)
        if result['code'] == 0:
            print("签到成功，领取第" + str(result['data']['box']+1) + "个补给包")
            print("龙门币：" + str(result['data']['content']['LMD']))
            print("合成玉：" + str(result['data']['content']['ORD']))
            break
        else:
            print("领取第" + str(i+1) + "个补给包失败：" + result['msg'])


if __name__ == "__main__":
    run()  # 第一次运行
    while True:
        now_localtime = time.strftime("%H:%M", time.localtime())
        if now_localtime == "04:00":
            run()
            time.sleep(61)
        else:
            time.sleep(29)
