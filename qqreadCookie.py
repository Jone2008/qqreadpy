import requests
import json
import time
import os
import re
import ast
import notification


"""
需要推送通知的，修改notification.py
"""

###############################
# 方案1 本地执行、云服务器、云函数等等   下载到本地，填写参数，执行

# qqreadheaders参数填写，填写完注意不要上传
# 如果有其它账号，还需要将qqreadheaders2填写进下面的qqreadheadersLists
qqreadheaders1 = '{}'
qqreadheaders2 = '{}'

# qqreadheaders参数填写，填写完注意不要上传
# 如果有其它账号，还需要将qqreadtimeheaders2填写进下面的qqreadheadersLists
qqreadtimeheaders1 = '{}'
qqreadtimeheaders2 = '{}'

# qqreadheaders参数填写，填写完注意不要上传
# 如果有其它账号，还需要将qqreadheaders2填写进下面的qqreadheadersLists
qqreadtimeurl1 = ""
qqreadtimeurl2 = ""

# 如为多账号，请修改下面参数
qqreadheadersLists = [qqreadheaders1, ]
qqreadtimeheadersLists = [qqreadtimeheaders1, ]
qqreadtimeurlLists = [qqreadtimeurl1, ]

qqreadLists = list(
    zip(qqreadheadersLists, qqreadtimeheadersLists, qqreadtimeurlLists))

####################################
# 方案2 GitHub action 自动运行    各参数读取自secrets


if "QQREADHEADERS" and "QQREADTIMEHEADERS" and "QQREADTIMEURL" in os.environ:
    qqreadheaders = os.environ["QQREADHEADERS"].split('\n')
    qqreadtimeheaders = os.environ["QQREADTIMEHEADERS"].split('\n')
    qqreadtimeurl = os.environ["QQREADTIMEURL"].split('\n')
    qqreadLists = []
    if len(qqreadheaders) == len(qqreadtimeheaders) and len(qqreadtimeheaders) == len(qqreadtimeurl):
        qqreadLists = list(
            zip(qqreadheaders, qqreadtimeheaders, qqreadtimeurl))
    else:
        print("各项Secrets数量不符，请修改！")
    


#######################################


def valid(qqheaders):
    headers = ast.literal_eval(qqheaders[0])
    response = requests.get(
        'https://mqqapi.reader.qq.com/mqq/user/init', headers=headers)
    if response.json()["data"]['isLogin'] == False:
        QQNUM = re.findall(r'ywguid=(.*?);ywkey', headers['Cookie'])[0]
        print(f"""## {QQNUM}: headers过期""")
        notification.notify(
            f"""## QQ账号【{QQNUM}】 headers过期""", f"""## 账号【{QQNUM}】 headers过期 ，及时修改""")
        return False
    return True


def get_cookies():
    return [i for i in qqreadLists if valid(i)]


if __name__ == "__main__":
    print(">>>检查有效性")
    for i in get_cookies():
        print(i)
