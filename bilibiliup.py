import json
import os
import sys

from biliup.plugins.bili_webup import BiliBili, Data
import yaml
import re
from datetime import datetime

if len(sys.argv) == 1:
    print("缺少主播ID arg或者文件路径arg，请按照GitHub仓库中的README进行运行！")
    exit()
# 定义要查找和替换的模式

patterns = {
    r'%%Y-%m-%d%': datetime.now().strftime('%Y.%m.%d'),
    r'%%m-%d%': datetime.now().strftime('%m.%d'),
    r'%Streamer%': sys.argv[1],
}

if not os.path.exists("config.yaml"):
    print("您并没有config.yaml，请按照GitHub仓库中的README进行设置！")
    exit()
# 读取YAML文件
with open('config.yaml', 'r', encoding='utf-8') as file:
    yaml_data = file.read()
# 查找和替换模式
for pattern, replacement in patterns.items():
    yaml_data = re.sub(pattern, replacement, yaml_data)

# 解析YAML数据
data = yaml.load(yaml_data, Loader=yaml.FullLoader)['biliup']


def bili_video_up(streamer_id):
    video_file = sys.argv[2]
    video = Data()
    video.title = data[streamer_id]['title']
    video.desc = data[streamer_id]['desc']
    video.source = data[streamer_id]['live_url']
    # 设置视频分区,默认为122 野生技能协会
    video.tid = data[streamer_id]['tid']
    video.set_tag(data[streamer_id]['set_tag'])
    if data[streamer_id]['dynamic'] != "":
        video.dynamic = data[streamer_id]['dynamic']
    lines = data['lines']
    tasks = data['tasks']
    dtime = data['dtime']  # 延后时间，单位秒
    with BiliBili(video) as bili:
        print(data['login'])
        if data['login'] == 'cookie':
            with open(data['cookie']['cookie_file']) as f:
                json_data = f.read()
            # 解析JSON数据
            cookies = json.loads(json_data)
            bili.login("bili.cookie", {
                'cookies': {
                    'SESSDATA': cookies['cookie_info']['cookies'][0]['value'],
                    'bili_jct': cookies['cookie_info']['cookies'][1]['value'],
                    'DedeUserID__ckMd5': cookies['cookie_info']['cookies'][3]['value'],
                    'DedeUserID': cookies['cookie_info']['cookies'][2]['value']
                }, 'access_token': cookies['access_token']})
        else:
            print("qwq")
            bili.login_by_password(data['password']['username'], data['password']['password'])
        video_part = bili.upload_file(video_file, lines=lines, tasks=tasks)  # 上传视频，默认线路AUTO自动选择，线程数量3。
        video.append(video_part)  # 添加已经上传的视频
        video.delay_time(dtime)  # 设置延后发布（2小时~15天）
        video.cover = bili.cover_up(data[streamer_id]['cover_path']).replace('http:', '')
        ret = bili.submit()  # 提交视频


try:
    bili_video_up(sys.argv[1])
except Exception as e:
    print(f"上传出错：{e}")
    if data['mail'] == 1:
        import mail

        title = f"{sys.argv[1]}的直播回放上传出错！"
        content = f"{sys.argv[1]}的直播回放{sys.argv[2]}上传出错！<br>错误详细:{e}"
        mail.sendEmail(title, content)
    exit()

if data['mail'] == 1:
    import mail

    title = f"{sys.argv[1]}的直播回放上传完成！"
    content = f"{sys.argv[1]}的直播回放{sys.argv[2]}上传完成！"
    mail.sendEmail(title, content)
