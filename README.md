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

`config.yaml`格式如下

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
```