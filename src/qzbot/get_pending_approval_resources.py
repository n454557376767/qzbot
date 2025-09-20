import requests
import json
from . import config

def approve_resource(status, resource_id, reject_reason=None):
    url = "http://47.94.147.186:8503/approve_resource"
    payload = {"status": status, "resource_id": resource_id}
    if reject_reason is not None:
        payload["reject_reason"] = reject_reason
    headers = {
        'Host': "47.94.147.186:8503",
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'Accept-Language': "zh-cn,zh;q=0.5",
        'Accept-Charset': "UTF-8",
        'x-access-token': config.token
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()