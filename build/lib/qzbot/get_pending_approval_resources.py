import requests
import json
from . import config

def get_pending_approval_resources():
    url = "http://47.94.147.186:8503/pending_resources"
    headers = {
      'Host': "47.94.147.186:8503",
      'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
      'Connection': "Keep-Alive",
      'Accept-Encoding': "gzip",
      'Accept-Language': "zh-cn,zh;q=0.5",
      'Accept-Charset': "UTF-8",
      'Content-Type': "application/json",
      'x-access-token': config.token
    }
    
    response = requests.get(url, headers=headers)
    
    return response.json()