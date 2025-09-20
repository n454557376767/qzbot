import requests
import json
from . import config

def upload_resource(size, icon_url, version, download_url, name, category_id, package_name):
    url = "http://47.94.147.186:8503/upload_resource"
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "Content-Type": "application/json",
        "x-access-token": config.token,
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data = {
        "size": size,
        "icon_url": icon_url,
        "version": version,
        "download_url": download_url,
        "name": name,
        "category_id": category_id,
        "package_name": package_name
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return (response.status_code, response.json())
    except Exception as e:
        return None, f"请求出错: {str(e)}"
        