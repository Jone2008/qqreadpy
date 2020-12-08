# QQRead使用说明

> 基于python的自动化脚本  
> 低调使用，请勿到处宣传  


### 特别声明:

- 本仓库发布的脚本及其中涉及的任何解锁和解密分析脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。

- 本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。

- 本人对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害。

- 间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, 本人对于由此引起的任何隐私泄漏或其他后果概不负责。

- 请勿将本仓库的任何内容用于商业或非法目的，否则后果自负。

- 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。

- 任何以任何方式查看此项目的人或直接或间接使用该项目的任何脚本的使用者都应仔细阅读此声明。本人保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或Script项目的规则，则视为您已接受此免责声明。

 **您必须在下载后的24小时内从计算机或手机中完全删除以上内容**  
> ***您使用或者复制了本仓库且本人制作的任何脚本，则视为 `已接受` 此声明，请仔细阅读*** 



### 主要参数：

| 名称                 | 功能           | 属性   | 备注                            |  
| :------------------: | :-----------: | :----: | ------------------------------ | 
| `QQREADHEADERS`      | 主header      | 必须   | 绝大多数功能的正常使用需要此参数  | 
| `QQREADBODYS`        | 主body        | 必须   | 绝大多数功能的正常使用需要此参数  |  
| `QQREADTIMEURL`      | 阅读时长URL    | 必须   | 上传阅读时长功能需要的URL        | 
| `NOTIFYTYPE`         | 通知类型       | 非必须 | 详见通知类型                    |  
| `NOTIFYCFG`          | 通知服务       | 非必须 | 详见通知服务                    | 
| `SCKEY`              | server酱key   | 非必须 | 自行获取                        | 
| `BARK`               | bark秘钥      | 非必须 | 自行获取                        | 
| `TG_BOT_TOKEN`      | telegram推送  | 非必须 | tg推送,填写自己申请[@BotFather](https://t.me/BotFather)的Token,如`10xxx4:AAFcqxxxxgER5uw` , [具体教程](https://github.com/lxk0301/jd_scripts/blob/master/backUp/TG_PUSH.md) |
| `TG_USER_ID`         | telegram推送  | 非必须 | tg推送,填写[@getuseridbot](https://t.me/getuseridbot)中获取到的纯数字ID, [具体教程](https://github.com/lxk0301/jd_scripts/blob/master/backUp/TG_PUSH.md) |


**⚠️cookie获取方法：**

1. 进入 https://m.q.qq.com/a/s/d3eacc70120b9a37e46bad408c0c4c2a 

2. 进一本书阅读一会儿，然后退出，获取`QQREADHEADERS` `QQREADBODYS` 和 `QQREADTIMEURL` 

3. `QQREADHEADERS` 和 `QQREADTIMEURL` 匹配链接为 https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?.......

   `QQREADBODYS` 匹配链接为 https://mqqapi.reader.qq.com/log/v4/mqq/track

4. `QQREADHEADERS`参数格式为


  ```
{"Cookie":"ywguid=123456789;ywkey=wedqwdlAWVJp9;platform=android;channel=mqqmina;mpVersion=0.30.0;qq_ver=8.4.18.4945;os_ver=Android10","aaa":"bbb",......}
  ```

多账号请按`Enter`键换行隔开示例(这里给下三个账号的示例)

  ```
{"Cookie":"ywguid=123456789;ywkey=******","aaa":"bbb",......}
{"Cookie":"ywguid=123456789;ywkey=******","aaa":"bbb",......}
{"Cookie":"ywguid=123456789;ywkey=******","aaa":"bbb",......}
  ```

5. `QQREADBODYS` 参数格式为

```
{"common":{"appid":***,"areaid":5,"qq_ver":"8.4.18.4945","os_ver":"Android 10","mp_ver":"0.31.0","mpos_ver":"1.21.0","brand":"***","model":"***","screenWidth":393,"screenHeight":816,"windowWidth":393,"windowHeight":762,"openid":"***","guid":***,"session":"***","scene":1023,"source":-1,"hasRedDot":"false","missions":-1,"caseID":-1},"dataList":[{"click1":"bookShelf_myshelf_myBook_C","click2":"qqauthorize_addRCS_succ_C","route":"pages/book-read/index","refer":"pages/book-shelf/index","options":{"bid":"27325720","cid":"3","from":"shelf"},"dis":1607325831391,"ext6":31,"eventID":"bookRead_show_I","type":"shown","ccid":3,"bid":"27325720","bookStatus":1,"bookPay":1,"chapterStatus":0,"ext1":{"font":18,"bg":0,"pageMode":1},"from":"bookShelf_myshelf_myBook_C_0_27325720"}]}
```

多账号请按`Enter`键换行隔开示例(这里给下三个账号的示例)

  ```
{"common":{"appid":***,"areaid":5,"qq_ver":"8.4.18.4945","os_ver":"Android 10","mp_ver":"0.31.0","mpos_ver":"1.21.0","brand":"***","model":"***","screenWidth":393,"screenHeight":816,"windowWidth":393,"windowHeight":762,"openid":"***","guid":***,"session":"***","scene":1023,"source":-1,"hasRedDot":"false","missions":-1,"caseID":-1},"dataList":[{"click1":"bookShelf_myshelf_myBook_C","click2":"qqauthorize_addRCS_succ_C","route":"pages/book-read/index","refer":"pages/book-shelf/index","options":{"bid":"27325720","cid":"3","from":"shelf"},"dis":1607325831391,"ext6":31,"eventID":"bookRead_show_I","type":"shown","ccid":3,"bid":"27325720","bookStatus":1,"bookPay":1,"chapterStatus":0,"ext1":{"font":18,"bg":0,"pageMode":1},"from":"bookShelf_myshelf_myBook_C_0_27325720"}]}
{"common":{"appid":***,"areaid":5,"qq_ver":"8.4.18.4945","os_ver":"Android 10","mp_ver":"0.31.0","mpos_ver":"1.21.0","brand":"***","model":"***","screenWidth":393,"screenHeight":816,"windowWidth":393,"windowHeight":762,"openid":"***","guid":***,"session":"***","scene":1023,"source":-1,"hasRedDot":"false","missions":-1,"caseID":-1},"dataList":[{"click1":"bookShelf_myshelf_myBook_C","click2":"qqauthorize_addRCS_succ_C","route":"pages/book-read/index","refer":"pages/book-shelf/index","options":{"bid":"27325720","cid":"3","from":"shelf"},"dis":1607325831391,"ext6":31,"eventID":"bookRead_show_I","type":"shown","ccid":3,"bid":"27325720","bookStatus":1,"bookPay":1,"chapterStatus":0,"ext1":{"font":18,"bg":0,"pageMode":1},"from":"bookShelf_myshelf_myBook_C_0_27325720"}]}
{"common":{"appid":***,"areaid":5,"qq_ver":"8.4.18.4945","os_ver":"Android 10","mp_ver":"0.31.0","mpos_ver":"1.21.0","brand":"***","model":"***","screenWidth":393,"screenHeight":816,"windowWidth":393,"windowHeight":762,"openid":"***","guid":***,"session":"***","scene":1023,"source":-1,"hasRedDot":"false","missions":-1,"caseID":-1},"dataList":[{"click1":"bookShelf_myshelf_myBook_C","click2":"qqauthorize_addRCS_succ_C","route":"pages/book-read/index","refer":"pages/book-shelf/index","options":{"bid":"27325720","cid":"3","from":"shelf"},"dis":1607325831391,"ext6":31,"eventID":"bookRead_show_I","type":"shown","ccid":3,"bid":"27325720","bookStatus":1,"bookPay":1,"chapterStatus":0,"ext1":{"font":18,"bg":0,"pageMode":1},"from":"bookShelf_myshelf_myBook_C_0_27325720"}]}
  ```

6. `QQREADTIMEURL` 参数格式为

```
https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?scene=***&refer=-1&bid=***&readTime=***&read_type=0&conttype=1&read_status=0&chapter_info=%5B%7B%221%22%3A%7B%22readTime%22%3A***%2C%22pay_status%22%3A0%7D%7D%5D&sp=-1
```

多账号请按`Enter`键换行隔开示例(这里给下三个账号的示例)

  ```
https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?scene=***&refer=-1&bid=***&readTime=***&read_type=0&conttype=1&read_status=0&chapter_info=%5B%7B%221%22%3A%7B%22readTime%22%3A***%2C%22pay_status%22%3A0%7D%7D%5D&sp=-1
https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?scene=***&refer=-1&bid=***&readTime=***&read_type=0&conttype=1&read_status=0&chapter_info=%5B%7B%221%22%3A%7B%22readTime%22%3A***%2C%22pay_status%22%3A0%7D%7D%5D&sp=-1
https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?scene=***&refer=-1&bid=***&readTime=***&read_type=0&conttype=1&read_status=0&chapter_info=%5B%7B%221%22%3A%7B%22readTime%22%3A***%2C%22pay_status%22%3A0%7D%7D%5D&sp=-1
  ```
  
7. **特别注意：** 三个参数中每个账号信息出现的顺序一定要一致，且每个参数有几个账号就写几行，不要有多余空行！

### 运行方式

##### 1、方案一 

本地执行、云服务器、云函数等等

下载到本地，填写 `qqreadCookie.py` 中的 `qqreadheaders` `qqreadbodys` `qqreadtimeurl` 等信息  
云函数请善用搜索以及对应官方文档

##### 2、方案二

GitHub action自动运行，账号信息读取自 `Repo-Setting-Secrets`  
**！请勿滥用！**



### 通知服务

默认不开启，需要通知服务的需修改 `NOTIFYCFG` 参数

目前会发送通知的情况有: 账号headers过期; 全部通知；收获宝箱通知；每收获15个宝箱通知  

支持两种通知方式，后续看心情添加其他通知方式

```
  [0，1，2，3]  0:不通知     1:server酱      2:bark服务      3:Telegram_bot
```

1. 使用Server酱的需要参数 `SCKEY` ，支持GitHub action
2. 使用bark的填写 `BARK` ，支持GitHub action
3. 使用Telegram Bot的填写 `TG_BOT_TOKEN` `TG_USER_ID` ，支持GitHub action

### 通知类型

默认为每领15个宝箱通知一次，需要其他通知类型请修改 `NOTIFYTYPE` 参数

支持三种通知类型

```
  [0，1，2，3]  0：关闭通知   1：所有通知   2：领取宝箱成功通知   3：每领15个宝箱通知一次
```

### 同步Fork后的代码

手动同步，[具体教程](http://www.ibloger.net/article/3361.html)

### 特别感谢(排名不分先后)：

* [@ziye12](https://github.com/ziye12)

* [@Zero-S1](https://github.com/Zero-S1)

* [@lxk0301](https://github.com/lxk0301)

