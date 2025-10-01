import qzbot

qzbot.set_token("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjAzLCJ1c2VybmFtZSI6Im5tMTIzQG91dGxvb2suY29tIiwiZGV2aWNlX2lkIjoiZjRlMzRjYjBhMjBhM2RiYiJ9.ZDET4wW-fHwJj-WjuuzMdn2oyAE8eaGnKddEc-CX_Xw")

resource = qzbot.Resource()

print("=== 测试1: 获取资源列表 ===")
category_id = 1
result = resource.get_resources(category_id)
print("获取资源列表结果:", result)

print("\n" + "="*50 + "\n")

print("=== 测试2: 上传新资源 ===")
new_resource = {
    "size": "78.91PB",
    "icon_url": "test",
    "version": "9.1.1",
    "download_url": "https://fuckyou.com",
    "name": "测试资源",
    "category_id": 1,
    "package_name": "qzbot上传的，请不要通过此资源"
}

upload_result = resource.upload_resource(
    size=new_resource["size"],
    icon_url=new_resource["icon_url"],
    version=new_resource["version"],
    download_url=new_resource["download_url"],
    name=new_resource["name"],
    category_id=new_resource["category_id"],
    package_name=new_resource["package_name"]
)

print("上传资源结果:", upload_result)

print("\n" + "="*50 + "\n")

print("=== 测试3: 获取待审核资源 ===")
pending_result = resource.get_pending_approval_resources()
print("获取待审核资源结果:", pending_result)

print("\n=== 所有测试完成 ===")
