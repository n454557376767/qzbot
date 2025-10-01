import requests
import json
from . import config

class Resource:
    def __init__(self):
        self.base_url = "http://47.94.147.186:8503"
        self.headers = {
            "Accept-Language": "zh-cn,zh;q=0.5",
            "Accept-Charset": "UTF-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
            "Host": "47.94.147.186:8503",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "Content-Type": "application/json",
            "x-access-token": config.token
        }

    def upload_resource(self, size, icon_url, version, download_url, name, category_id, package_name):
        if not config.token:
            return "请先在config模块中设置token"
        
        url = f"{self.base_url}/upload_resource"
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
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"

    def get_resources(self, category_id):
        url = f"{self.base_url}/get_resources"
        params = {"category_id": category_id}
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"

    def get_pending_approval_resources(self):
        if not config.token:
            return "请先在config模块中设置token"
            
        url = f"{self.base_url}/pending_resources"
        
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"

    def approve_resource(self, status, resource_id, reject_reason=None):
        if not config.token:
            return "请先在config模块中设置token"
            
        url = f"{self.base_url}/approve_resource"
        payload = {"status": status, "resource_id": resource_id}
        
        if reject_reason is not None:
            payload["reject_reason"] = reject_reason
            
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(payload))
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"
