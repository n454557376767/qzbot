import requests
import json

token = None
def set_token(new_token):
    
    global token
    token = new_token


def send_post(title, content, category_id, message_type, is_markdown):
    if not token:
        return None, "请先调用set_token函数设置token"
    
    url = "http://47.94.147.186:8503/post_message"
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "x-access-token": token,
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 91; K-91 Build/NoneK91)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    
    # 初始化data，先不包含title
    data = {
        "category_id": category_id,
        "message_type": message_type,
        "content": content
    }
    
    # 仅当title不为空（非None/空字符串）时，添加title项
    if title and str(title).strip():
        data["title"] = title
    # 按需添加is_markdown
    if is_markdown:
        data["is_markdown"] = is_markdown
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return (response.status_code, response.json())
    except Exception as e:
        return None, f"请求出错: {str(e)}"
        
        
def upload_resource(size, icon_url, version, download_url, name, category_id, package_name):
    url = "http://47.94.147.186:8503/upload_resource"
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "Content-Type": "application/json",
        "x-access-token": token,
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
        
def sign_in():
    
    url = "http://47.94.147.186:8503/online_qingzhougood"
    
    
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "Content-Type": "application/json",
        "x-access-token": token,
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    
    try:
        response = requests.post(url, headers=headers, data="")
        
        return response.status_code, response.json()
    except Exception as e:
        
        return None, f"请求出错：{str(e)}"


def get_resources(category_id):
    url = "http://47.94.147.186:8503/get_resources"
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    params = {
        "category_id": category_id
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        return response.status_code, response.json()
    except Exception as e:
        return None, f"请求出错: {str(e)}"
        
def decode_unicode_escape(data):
    return json.loads(json.dumps(data))
    

def get_messages(category_id, page, per_page):
    
    url = f"http://47.94.147.186:8503/v3/get_message?category_id={category_id}&page={page}&per_page={per_page}"
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "x-access-token": token,  
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        return response.json()
    except requests.RequestException as e:
       return None, f"请求出错: {str(e)}"

def post_referenced_message(content, referenced_message_id, category_id):
    url = "http://47.94.147.186:8503/post_referenced_message"
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "Content-Type": "application/json",
        "x-access-token": token,  
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data = {
        "referenced_message_id": referenced_message_id,
        "category_id": category_id,
        "content": content
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
    except Exception as e:
        return str(e)
        
        
def like_message(message_id):
    url = "http://47.94.147.186:8503/like_message"
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "x-access-token": token,
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data = {"message_id": message_id}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
    except Exception as e:
        return {"error": str(e)}