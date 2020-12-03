import requests
import os
import ast
import time


#######################
# 通知服务
#######################



NOTIFYCFG = 0     # [0,1,2,3]  0:不通知    1:server酱    2:bark服务    3:Telegram_bot

SCKEY = ''        # Server酱的SCKEY
BARK = ''         # bark服务,自行搜索
TG_BOT_TOKEN = ''           # telegram bot token 自行申请
TG_USER_ID = ''             # telegram 用户ID
##################################################################


def n0(a, b):
    """空函数,即不使用通知服务"""
    print(">>>>未开启通知服务")
    return


def serverJ(title, content):
    """server酱服务"""
    sckey = SCKEY
    if "SCKEY" in os.environ:
        """
        判断是否运行自GitHub action,"SCKEY" 该参数与 repo里的Secrets的名称保持一致
        """
        sckey = os.environ["SCKEY"]

    if not sckey:
        print("server酱服务的SCKEY未设置!!\n取消推送")
        return
    print("serverJ服务启动")
    content = content.replace("\n", "\n\n")
    data = {
        "text": title,
        "desp": content
    }
    response = requests.post(f"https://sc.ftqq.com/{sckey}.send", data=data)
    print(response.text)


def bark(title, content):
    """bark服务"""
    bark_token = BARK
    title = content.replace("#", "")
    content = content.replace("#", "")
    if "BARK" in os.environ:
        """
        判断是否运行自GitHub action,"BARK" 该参数与 repo里的Secrets的名称保持一致
        """
        bark_token = os.environ["BARK"]
    if not bark_token:
        print("bark服务的bark_token未设置!!\n取消推送")
        return
    response = requests.get(
        f"""https://api.day.app/{bark_token}/{title}/{content}""")
    print(response.text)


def telegram_bot(title, content):
    """Telegram_bot服务"""
    print("\n")
    tg_bot_token = TG_BOT_TOKEN
    tg_user_id = TG_USER_ID
    if "TG_BOT_TOKEN" in os.environ and "TG_USER_ID" in os.environ:
        tg_bot_token = os.environ["TG_BOT_TOKEN"]
        tg_user_id = os.environ["TG_USER_ID"]
    if not tg_bot_token or not tg_user_id:
        print("Telegram推送的tg_bot_token或者tg_user_id未设置!!\n取消推送")
        return
    print("Telegram 推送开始")
    send_data = {"chat_id": tg_user_id, "text": title +
                 '\n\n'+content, "disable_web_page_preview": "true"}
    response = requests.post(
        url=f'https://api.telegram.org/bot{tg_bot_token}/sendMessage', data=send_data)
    print(response.json()['ok'])


if "NOTIFYCFG" in os.environ and os.environ["NOTIFYCFG"].strip():
    NOTIFYCFG = ast.literal_eval(os.environ["NOTIFYCFG"])

notify = [n0, serverJ, bark, telegram_bot][NOTIFYCFG]

if __name__ == "__main__":
    print("通知服务测试")
    start = time.time()
    notify("QQRead脚本通知服务", "needYou2Know\n通知服务测试")
    print("耗时: ", time.time()-start, "s")
