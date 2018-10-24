import requests

query = {
    "ac": "WIFI",
    "iid": "46961748949",
    "device_id": "58097798464",
    "os_api": "18",
    "app_name": "aweme",
    "channel": "App Store",
    "idfa": "B6B7BF1B-AADD-42E6-83AB-D29C93620305",
    "device_platform": "iphone",
    "build_number": "29101",
    "vid": "5A56818A-EC4B-4C9B-843F-881E99603F5A",
    "openudid": "825a48a41a70c4182b21cc442993c6bf6f1ed6e6",
    "device_type": "iPhone9,2",
    "app_version": "2.9.1",
    "version_code": "2.9.1",
    "os_version": "12.0",
    "screen_width": "1242",
    "aid": "1128",
    "pass-region": "1",
    "detail_list": "0",
    "mas": "01b4002e3d345720d85d1983fe6b328535431c67b1f365be1f2f38",
    "as": "a1e5000df9532bbfa03287",
    "ts": "1540362041"
}

base_url = 'https://aweme.snssdk.com/aweme/v1/hot/search/list/'

response = requests.get(base_url, params=query, verify=False)
print(response.url)
print(response.status_code)
print(response.json())
