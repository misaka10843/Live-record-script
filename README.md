# Live-record-script
Used to extend the functional scripts in [olive](https://github.com/go-olive/olive) (the scripts in this repository can be used mostly separately)

用于扩展[olive](https://github.com/go-olive/olive)中的功能脚本(此仓库的脚本基本上都能分开独立使用)

此仓库中的所有脚本均为为了让olive拥有更多自定义的上传/通知功能

如果是olive本身的问题，还请不要在此仓库发送Issue

## Attention! （中文用户可以跳过）

Please note that since most of the functions in this repository are designed for uploading live recordings to Bilibili or for personal use, other websites or languages besides Chinese have not been taken into consideration.

## 使用前必看

因为编写此仓库时考虑到可能有人只需要特定一个功能，所有并没有将所有功能集成

所以您需要自己编写`config.yaml`，还有按照下文安装依赖(如果懒或者需要全部功能可以直接`pip install -r requirements.txt`)

<details>
<summary>

`config.yaml`格式如下

</summary>

```yaml
# mail.py配置
mail:
  # 邮箱的smtp服务器
  mail_host: "smtp.163.com"
  # 您的邮箱
  mail_user: "xxxxxxx@163.com"
  # smtp的密钥。基本上国内的邮箱都不是登录密码，而是需要申请的key
  mail_pass: "xxxxxxx"
  # 发送邮箱，最好与mail_user相同
  sender: "xxxxxxx@163.com"
  # 收件人邮箱，需要将提示邮件发送给谁，可以以数组的方式输入
  receivers: ['xxxxxxx@outlook.jp','xxxx@qq.com']

# bilibiliup.py配置
biliup:
  # 上传线路，目前可手动切换为bda2, kodo, ws, qn，或者直接填写AUTO，会选择最优线路
  lines: "AUTO"
  # 线程数量
  tasks: "3"
  # 延后时间(类似于定时发布)，单位为秒
  dtime: "0"
  # 是否进行mail通知(0:否，1:是)，请将mail.py移动到bilibiliup.py的同等级目录
  mail: 1
  # 登录方式，支持password与cookie，对于新手来说请使用password
  login: 'password'
  # cookie登录方式，如果不知道你的cookie的话，请安装olive
  # 然后在终端输入 olive biliup login
  cookie:
    # 你的cookie.json的文件路径
    cookie_file: "/xxxx/xx/cookie.json"
  # 账号密码登录方式
  password:
    # 你的手机号/邮箱等
    username: "12345678"
    # 你的账号密码
    password: "Aa12345678"
  # 主播的名字/id，请对应如何使用-bilibiliup.py中使用方法中的主播的名字/id
  # 以下内容可以多复制几个，只要有匹配的主播的名字/id就会使用对应下面的设置
  # 但是请注意！如果在如何使用-bilibiliup.py中使用方法中的主播的名字/id没有在此配置文件中
  # 会导致程序报错或退出
  こかむも:
    # 视频标题，其中支持以下占位符
    # %%Y-%m-%d% ：输出年月日
    # %%m-%d%：输出月日
    # %Streamer%：输出主播名字/id
    title: "[%%m-%d%/%Streamer%直播回放]"
    # 视频简介
    desc: "视频简介"
    # 直播间链接，用于获取%LiveTitle%的标题，并且用于填写转载的链接
    live_url: "http://xxxx"
    # 视频分区ID，详细可看 https://github.com/biliup/biliup/wiki
    tid: 152
    # 视频的标签，请不要添加超过10个
    set_tag: ['直播','回放']
    # 动态内容，留空为不编写动态
    dynamic: ""
    # 视频封面图片路径
    cover_path: "/xxx/xx/1.jpg"
    
```

</details>

## 如何使用

### mail.py
`python mail.py 主播的名字/id 视频的路径`

如果是在olive中配置文件的话，就应该这样写

`PostCmds = '[{"Path":"oliveshell","Args":["/usr/local/python/bin/python3","/www/wwwroot/LiveRe/mail.py","直播的id/名字 $FILE_PATH"]}]'`

### bilibiliup.py

`python bilibiliup.py 主播的名字/id 视频的路径`

如果是在olive中配置文件的话，就应该这样写

`PostCmds = '[{"Path":"oliveshell","Args":["/usr/local/python/bin/python3","/www/wwwroot/LiveRe/bilibiliup.py","直播的id/名字 $FILE_PATH"]}]'`

## 各个功能需要的依赖

### mail.py
```text
    pyyaml
```