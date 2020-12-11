# -*- coding: utf-8 -*-
# @Time    : 2020-12-11
# @Author  : water008@github
# @File    : qqread.py

"""

Github地址    https://github.com/Water008/qqread
TG 频道       https://t.me/water_scripts
TG 群组       https://t.me/joinchat/AAAAAEhFTR9JV3Vf6NAWZw

⚠️必须参数获取方法：

进入 https://m.q.qq.com/a/s/6fb00f7035f82425df91a5b668f6be8b

进一本书阅读一会儿，然后退出，获取QQREADHEADERS QQREADBODYS 和 QQREADTIMEURL

QQREADHEADERS 和 QQREADTIMEURL 匹配链接为 https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?.......

QQREADBODYS 匹配链接为 https://mqqapi.reader.qq.com/log/v4/mqq/track

详细说明请阅读 https://github.com/Water008/qqread/blob/main/README.md

如遇问题，欢迎提交Issues或在TG反馈

⚠️宝箱奖励为20分钟一次，自己根据情况设置定时，建议cron设置为 */11 * * * * ，即每11分钟运行一次

"""

import os
import re
import ast
import time
import json
import random
import requests
import qqreadCookie
import notification
from datetime import datetime, timedelta


# 以下为可修改参数
TIME = 5  # 单次上传阅读时间，默认为5分钟
LIMIT_TIME = 18  # 每日最大上传阅读时间，默认为18小时
DELAYSEC = 1  # 单次任务延时，默认为1秒
NOTIFYTYPE = 3  # 0为关闭通知，1为所有通知，2为领取宝箱成功通知，3为每领15个宝箱通知一次
DRAWAMOUNT = 0  # [0, 10, 30, 50, 100] 分别为关闭自动提现、提现10元、30元、50元、100元，默认为关闭
# 以上为可修改参数

if "NOTIFYTYPE" in os.environ and os.environ["NOTIFYTYPE"].strip():
    NOTIFYTYPE = ast.literal_eval(os.environ["NOTIFYTYPE"])
if "DRAWAMOUNT" in os.environ and os.environ["DRAWAMOUNT"].strip():
    DRAWAMOUNT = ast.literal_eval(os.environ["DRAWAMOUNT"])


def getTemplate(headers, functionId):
    """请求模板"""
    functionURL = f"https://mqqapi.reader.qq.com/mqq/{functionId}"
    delay()
    data = requests.get(functionURL, headers=ast.literal_eval(headers)).json()
    return data


def qqreadtask(headers):
    """获取任务列表"""
    task_data = getTemplate(headers, "red_packet/user/page?fromGuid=")['data']
    return task_data


def qqreadmytask(headers):
    """获取“我的”页面任务"""
    mytask_data = getTemplate(headers, "v1/task/list")['data']['taskList']
    return mytask_data


def qqreadinfo(headers):
    """获取用户名"""
    info_data = getTemplate(headers, "user/init")['data']
    return info_data


def qqreadticket(headers):
    """书券签到"""
    qqreadticketurl = "https://mqqapi.reader.qq.com/mqq/sign_in/user"
    delay()
    ticket_data = requests.post(
        qqreadticketurl, headers=ast.literal_eval(headers)).json()['data']
    return ticket_data


def qqreadsign(headers):
    """每日打卡"""
    sign_data = getTemplate(headers, "red_packet/user/clock_in/page")['data']
    return sign_data


def qqreadsign2(headers):
    """每日打卡翻倍"""
    sign2_data = getTemplate(headers, "red_packet/user/clock_in_video")
    return sign2_data


def qqreadtodayread(headers):
    """每日阅读"""
    todayread_data = getTemplate(headers, "red_packet/user/read_book")
    return todayread_data


def qqreadvideo(headers):
    """视频奖励"""
    video_data = getTemplate(headers, "red_packet/user/watch_video")
    return video_data


def qqreadbox(headers):
    """宝箱奖励"""
    box_data = getTemplate(headers, "red_packet/user/treasure_box")
    return box_data


def qqreadbox2(headers):
    """宝箱奖励翻倍"""
    box2_data = getTemplate(headers, "red_packet/user/treasure_box_video")
    return box2_data


def qqreadwktime(headers):
    """获取本周阅读时长"""
    wktime_data = getTemplate(headers, "v1/bookShelfInit")['data']['readTime']
    return wktime_data


def qqreadwkpickinfo(headers):
    """周阅读时长奖励查询"""
    wkpickinfo_data = getTemplate(headers, "pickPackageInit")['data']
    return wkpickinfo_data


def qqreadwkpick(headers, num):
    """周阅读时长奖励领取"""
    wkpick_data = getTemplate(headers, f"pickPackage?readTime={num}")
    return wkpick_data


def qqreadtodaytime(headers, bidnum):
    """获取本日阅读时长"""
    bid = re.findall(r'bid=(\d+)&', bidnum)[0]
    todaytime_data = getTemplate(headers, f"page/config?router=%2Fpages%2Fbook-read%2Findex&options=%7B%22bid%22%3A%22{bid}%22%7D")[
        'data']['pageParams']['todayReadSeconds']
    return todaytime_data//60


def qqreadtodaygift(headers, sec):
    """本日阅读时长奖励"""
    todygift_data = getTemplate(
        headers, f"red_packet/user/read_time?seconds={sec}")['data']
    return todygift_data


def qqreadaddtime(headers, addtimeurl):
    """上传阅读时长"""
    sectime = random.randint(TIME*60*1000, (TIME+1)*60*1000)
    findtime = re.compile(r'readTime=(\d+)&read_')
    findtime1 = re.compile(r'readTime%22%3A(\d+)%2C')
    url = re.sub(findtime.findall(addtimeurl)[
                 0], str(sectime), str(addtimeurl))
    url = re.sub(findtime1.findall(addtimeurl)[
                 0], str(sectime), str(addtimeurl))
    delay()
    addtime_data = requests.get(url, headers=ast.literal_eval(headers)).json()
    return addtime_data


def qqreadssr(headers, sec):
    """每日阅读时长奖励"""
    readssr_data = getTemplate(
        headers, f"red_packet/user/read_time?seconds={sec}")
    return readssr_data


def qqreadwithdrawinfo(headers):
    """查询提现信息"""
    withdrawinfo_data = getTemplate(
        headers, f"red_packet/user/withdraw/list?pn=1")['data']['list'][0]
    return withdrawinfo_data


def qqreadwithdrawal(headers, amount):
    """提现"""
    qqreadwithdrawalurl = f"https://mqqapi.reader.qq.com/mqq/red_packet/user/withdraw?amount={amount}"
    delay()
    withdrawal_data = requests.post(
        qqreadwithdrawalurl, headers=ast.literal_eval(headers)).json()
    if withdrawal_data['data']['code'] == 0:
        msg = withdrawal_data['msg']
    else:
        msg = withdrawal_data['data']['msg']
    return msg


def qqreadtrack(headers, data: str):
    """Track"""
    qqreadtrackurl = "https://mqqapi.reader.qq.com/log/v4/mqq/track"
    finddis = re.compile(r'"dis".*?(\d{13})')
    data = re.sub(finddis.findall(data)[
        0], str(int(time.time()*1000)), str(data))
    delay()
    track_data = requests.post(
        qqreadtrackurl, data=json.dumps(ast.literal_eval(data)), headers=ast.literal_eval(headers)).json()
    return track_data


def totalAmount(headers) -> str:
    """统计今日获得金币"""
    totalamount = 0
    for pn in range(12):
        url = f'https://mqqapi.reader.qq.com/mqq/red_packet/user/trans/list?pn={pn+1}'
        amount_data = requests.get(url, headers=ast.literal_eval(headers)).json()['data']['list']
        for i in amount_data:
            if i['createTime'] >= getTimestamp():
                totalamount += i['amount']
    return str(totalamount)


def gettime():
    """获取北京时间"""
    bj_dt = datetime.utcnow()+timedelta(hours=8)
    return bj_dt


def getTimestamp() -> int:
    """获取当日0点时间戳"""
    bj_dt = (datetime.utcnow()+timedelta(hours=8)
             ).strftime('%Y-%m-%d') + " 00:00:00"
    timeArray = time.strptime(bj_dt, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray)*1000)
    return timeStamp


def delay():
    """延时"""
    time.sleep(DELAYSEC)


def sendmsg(title: str, content: str):
    """发送通知"""
    notification.notify(title, content)


def start(index, secrets):
    print(f"\n============开始运行第{index+1}个账号===========")
    start_time = time.time()
    tz = ""
    info_data = qqreadinfo(secrets[0])
    todaytime_data = qqreadtodaytime(secrets[0], secrets[2])
    wktime_data = qqreadwktime(secrets[0])
    print(f"Track update {qqreadtrack(secrets[0], secrets[1])['msg']}")
    task_data = qqreadtask(secrets[0])
    mytask_data = qqreadmytask(secrets[0])

    tz += f"=== {gettime().strftime('%Y-%m-%d %H:%M:%S')} ===\n"
    tz += f"=== 📣系统通知📣 ===\n"
    tz += f"【用户信息】{info_data['user']['nickName']}\n"
    tz += f"【账户余额】{task_data['user']['amount']}金币\n"
    tz += f"【今日阅读】{todaytime_data}分钟\n"
    tz += f"【本周阅读】{wktime_data}分钟\n"
    tz += f"【{task_data['taskList'][0]['title']}】{task_data['taskList'][0]['amount']}金币,{task_data['taskList'][0]['actionText']}\n"
    tz += f"【{task_data['taskList'][1]['title']}】{task_data['taskList'][1]['amount']}金币,{task_data['taskList'][1]['actionText']}\n"
    tz += f"【{task_data['taskList'][2]['title']}】{task_data['taskList'][2]['amount']}金币,{task_data['taskList'][2]['actionText']}\n"
    tz += f"【{task_data['taskList'][3]['title']}】{task_data['taskList'][3]['amount']}金币,{task_data['taskList'][3]['actionText']}\n"
    tz += f"【第{task_data['invite']['issue']}期】时间{task_data['invite']['dayRange']} [已邀请{task_data['invite']['inviteCount']}人，再邀请{task_data['invite']['nextInviteConfig']['count']}人获得{task_data['invite']['nextInviteConfig']['amount']}金币]\n"
    tz += f"【{task_data['fans']['title']}】{task_data['fans']['fansCount']}个好友,{task_data['fans']['todayAmount']}金币\n"
    tz += f"【宝箱任务{task_data['treasureBox']['count'] + 1}】{task_data['treasureBox']['tipText']}\n"

    if task_data['treasureBox']['doneFlag'] == 0:
        box_data = qqreadbox(secrets[0])
        if box_data['code'] == 0:
            tz += f"【宝箱奖励{box_data['data']['count']}】获得{box_data['data']['amount']}金币\n"

    for i in range(len(task_data['taskList'])):
        if task_data['taskList'][i]['title'].find("立即阅读") != -1 and task_data['taskList'][i]['doneFlag'] == 0:
            todayread_data = qqreadtodayread(secrets[0])
            if todayread_data['code'] == 0:
                tz += f"【每日阅读】获得{todayread_data['data']['amount']}金币\n"

        if task_data['taskList'][i]['title'].find("打卡") != -1:
            sign_data = qqreadsign(secrets[0])
            if task_data['taskList'][i]['doneFlag'] == 0:
                tz += f"【今日打卡】获得{sign_data['todayAmount']}金币，已连续签到{sign_data['clockInDays']}天\n"
            if sign_data['videoDoneFlag'] == 0:
                sign2_data = qqreadsign2(secrets[0])
                if sign2_data['code'] == 0:
                    tz += f"【打卡翻倍】获得{sign2_data['data']['amount']}金币\n"

        if task_data['taskList'][i]['title'].find("视频") != -1 and task_data['taskList'][i]['doneFlag'] == 0:
            video_data = qqreadvideo(secrets[0])
            if video_data['code'] == 0:
                tz += f"【视频奖励】获得{video_data['data']['amount']}金币\n"

        if task_data['taskList'][i]['title'].find("阅读任务") != -1 and task_data['taskList'][i]['doneFlag'] == 0:
            if todaytime_data >= 1 and todaytime_data < 15:
                todaygift_data = qqreadtodaygift(secrets[0], 30)
                if todaygift_data['amount'] > 0:
                    tz += f"【阅读金币1】获得{todaygift_data['amount']}金币\n"
            if todaytime_data >= 5 and todaytime_data < 30:
                time.sleep(2)
                todaygift_data = qqreadtodaygift(secrets[0], 300)
                if todaygift_data['amount'] > 0:
                    tz += f"【阅读金币2】获得{todaygift_data['amount']}金币\n"
            if todaytime_data >= 30:
                time.sleep(2)
                todaygift_data = qqreadtodaygift(secrets[0], 1800)
                if todaygift_data['amount'] > 0:
                    tz += f"【阅读金币3】获得{todaygift_data['amount']}金币\n"

    for i in range(len(mytask_data)):
        if mytask_data[i]['title'].find("每日签到") != -1 and mytask_data[i]['doneFlag'] == 0:
            ticket_data = qqreadticket(secrets[0])
            if ticket_data['takeTicket'] > 0:
                tz += f"【书券签到】获得{ticket_data['takeTicket']}书券\n"

    if wktime_data >= 1200:
        wkpickinfo_data = qqreadwkpickinfo(secrets[0])
        package = ['10', '10', '20', '30', '50', '80', '100', '120']
        if wkpickinfo_data[-1]['isPick'] == False:
            for m, i in enumerate(wkpickinfo_data):
                info = getTemplate(
                    secrets[0], f"pickPackage?readTime={i['readTime']}")
                if info['code'] == 0:
                    tz += f"【周时长奖励{m+1}】领取{package[m]}书券\n"
        else:
            tz += "【周时长奖励】已全部领取\n"

    if task_data['treasureBox']['videoDoneFlag'] == 0:
        time.sleep(6)
        box2_data = qqreadbox2(secrets[0])
        if box2_data['code'] == 0:
            tz += f"【宝箱翻倍】获得{box2_data['data']['amount']}金币\n"

    if todaytime_data//60 <= LIMIT_TIME:
        addtime_data = qqreadaddtime(secrets[0], secrets[2])
        if addtime_data['code'] == 0:
            tz += f"【阅读时长】成功上传{TIME}分钟\n"

    if DRAWAMOUNT != 0 and task_data['user']['amount'] >= DRAWAMOUNT*10000 and gettime().hour == 21:
        withdrawinfo_data = qqreadwithdrawinfo(secrets[0])['createTime']
        if withdrawinfo_data < getTimestamp():
            withdrawal_data = qqreadwithdrawal(secrets[0], DRAWAMOUNT*10000)
            sendmsg("企鹅读书提现通知", f"提现{DRAWAMOUNT}元：{withdrawal_data}")
            tz += f"【自动提现】提现{DRAWAMOUNT}元（{withdrawal_data}）"

    tz += f"【今日收益】{totalAmount(secrets[0])}金币\n"

    tz += f"\n🕛耗时：{time.time()-start_time}秒"
    print(tz)

    if NOTIFYTYPE == 1:
        sendmsg("企鹅读书通知", tz)
    if NOTIFYTYPE == 2 and task_data['treasureBox']['doneFlag'] == 0:
        sendmsg("企鹅读书通知", tz)
    if NOTIFYTYPE == 3 and task_data['treasureBox']['doneFlag'] == 0 and task_data['treasureBox']['count'] % 15 == 0:
        sendmsg("企鹅读书通知", tz)


if __name__ == "__main__":
    for index, secrets in enumerate(qqreadCookie.get_cookies()):
        start(index, secrets)
