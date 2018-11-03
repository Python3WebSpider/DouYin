import requests

# query = {
# "ac": "WIFI",
# "iid": "46961748949",
# "device_id": "58097798464",
# "os_api": "18",
# "app_name": "aweme",
# "channel": "App Store",
# "idfa": "B6B7BF1B-AADD-42E6-83AB-D29C93620305",
# "device_platform": "iphone",
# "build_number": "29101",
# "vid": "5A56818A-EC4B-4C9B-843F-881E99603F5A",
# "openudid": "825a48a41a70c4182b21cc442993c6bf6f1ed6e6",
# "device_type": "iPhone9,2",
# "app_version": "2.9.1",
# "version_code": "2.9.1",
# "os_version": "12.0",
# "screen_width": "1242",
# "aid": "1128",
# "pass-region": "1",
# "keyword": "三庭五眼标准脸",
# "count": "12",
# "offset": "60",
# "source": "video_search",
# "hot_search": "1",
# "mas": "01dd88c948b345ad9d54935e1c9cb91e2e52195833e37a0d4a04ee",
# "as": "a1856aed60b72b4d628753",
# "ts": "1540533616"
# }

# query = {
#     # "ac": "WIFI",
#     # "iid": "46961748949",
#     # "device_id": "58097798464",
#     # "os_api": "18",
#     # "app_name": "aweme",
#     # "channel": "App Store",
#     # "idfa": "B6B7BF1B-AADD-42E6-83AB-D29C93620305",
#     # "device_platform": "iphone",
#     # "build_number": "29101",
#     # "vid": "5A56818A-EC4B-4C9B-843F-881E99603F5A",
#     # "openudid": "825a48a41a70c4182b21cc442993c6bf6f1ed6e6",
#     # "device_type": "iPhone9,2",
#     # "app_version": "2.9.1",
#     "version_code": "2.9.1",
#     # "os_version": "12.0",
#     # "screen_width": "1242",
#     # "aid": "1128",
#     # "pass-region": "1",
#     "count": "10",
#     "cursor": "30",
#     # "mas": "017cf50c73008bad543b552ca0369777473911b0e7c8fbc462a721",
#     # "as": "a195ab9d916dfba5629896",
#     # "ts": "1540535761"
# }

# query = {
#     # "ac": "WIFI",
#     # "iid": "46961748949",
#     "device_id": "33333333",
#     # "os_api": "18",
#     # "app_name": "aweme",
#     # "channel": "App Store",
#     # "idfa": "B6B7BF1B-AADD-42E6-83AB-D29C93620305",
#     # "device_platform": "iphone",
#     # "build_number": "29101",
#     # "vid": "5A56818A-EC4B-4C9B-843F-881E99603F5A",
#     # "openudid": "825a48a41a70c4182b21cc442993c6bf6f1ed6e6",
#     # "device_type": "iPhone9,2",
#     # "app_version": "2.9.1",
#     # "version_code": "2.9.1",
#     # "os_version": "12.0",
#     # "screen_width": "1242",
#     # "aid": "1128",
#     # "pass-region": "1",
#     "cursor": "0",
#     "music_id": "6606196836371794691",
#     # "pull_type": "2",
#     "count": "11",
#     # "type": "6",
#     # "mas": "0143c9f3d621b358454717211b3d5b91be242eaad18243a010d6a8",
#     # "as": "a1756b5dab96bb15627918",
#     # "ts": "1540535659"
# }

# query = {
#     "ac": "WIFI",
#     "iid": "46961748949",
#     "device_id": "58097798464",
#     "os_api": "18",
#     "app_name": "aweme",
#     "channel": "App Store",
#     "idfa": "B6B7BF1B-AADD-42E6-83AB-D29C93620305",
#     "device_platform": "iphone",
#     "build_number": "29101",
#     "vid": "5A56818A-EC4B-4C9B-843F-881E99603F5A",
#     "openudid": "825a48a41a70c4182b21cc442993c6bf6f1ed6e6",
#     "device_type": "iPhone9,2",
#     "app_version": "2.9.1",
#     "version_code": "2.9.1",
#     "os_version": "12.0",
#     "screen_width": "1242",
#     "aid": "1128",
#     "pass-region": "1",
#     "query_type": "0",
#     "cursor": "72",
#     "ch_id": "1579168686354445",
#     "count": "18",
#     "pull_type": "2",
#     "type": "5",
#     "mas": "01fa6c53471c45dc2f83db17c2c208d492d353529e1eae812f2728",
#     "as": "a1656b8d763eabc5a28997",
#     "ts": "1540535782"
# }

# query = {
# "ac": "WIFI",
# "iid": "46961748949",
# "device_id": "222222",
# "os_api": "18",
# "app_name": "aweme",
# "channel": "App Store",
# "idfa": "B6B7BF1B-AADD-42E6-83AB-D29C93620305",
# "device_platform": "iphone",
# "build_number": "29101",
# "vid": "5A56818A-EC4B-4C9B-843F-881E99603F5A",
# "openudid": "825a48a41a70c4182b21cc442993c6bf6f1ed6e6",
# "device_type": "iPhone9,2",
# "app_version": "2.9.1",
# "version_code": "2.9.1",
# "os_version": "12.0",
# "screen_width": "1242",
# "aid": "1129",
# "pass-region": "1",
# "query_type": "0",
# "cursor": "0",
# "ch_id": "1614257803840525",
# "count": "18",
# "pull_type": "2",
# "type": "5",
# "mas": "019e89de1c6917f6ff17e5a3fb15e9f4a042dc4b112dd70bc304ee",
# "as": "a115357dd5d06b22130853",
# "ts": "1540575749"
# }

query = {
    # "ac": "WIFI",
    # "iid": "49530073634",
    "device_id": "58097798460",
    # "os_api": "18",
    # "app_name": "aweme",
    # "channel": "App Store",
    # "idfa": "B6B7BF1B-AADD-42E6-83AB-D29C93620305",
    # "device_platform": "iphone",
    # "build_number": "31006",
    # "vid": "5A56818A-EC4B-4C9B-843F-881E99603F5A",
    # "openudid": "825a48a41a70c4182b21cc442993c6bf6f1ed6e6",
    # "device_type": "iPhone9,2",
    # "app_version": "3.1.0",
    # "js_sdk_version": "1.3.0.1",
    # "version_code": "3.1.0",
    # "os_version": "12.0",
    # "screen_width": "1242",
    "aid": "1129",
    # "pass-region": "1",
    "query_type": "0",
    "cursor": "0",
    "ch_id": "1615917132956695",
    "count": "18",
    # "pull_type": "2",
    # "type": "5",
    # "mas": "019a446388982299eccaa62c24afeab1fa2c9ae7543ea3cb48af31",
    # "as": "a16575fd5f15fbfaad0086",
    # "ts": "1541233247"
}

headers = {
    # 'Host': 'api.amemv.com',
    # 'x-Tt-Token': '0077066df5297676b148df690836bac9ead09e8e3d4fe366c5ab3ab74a827035cd3506b08117028a67cd66bded5e96645a45',
    # 'User-Agent': 'Aweme 2.9.1 rv:29101 (iPhone; iOS 12.0; zh_CN) Cronet',
    'User-Agent': 'Aweme 3.1.0 rv:31006 (iPhone; iOS 12.0; zh_CN) Cronet'
    # 'Cookie': 'odin_tt=673293b03d79c15c86fc2bafd05bea71b96c3f1a97a17a96dca9afff9187ae4dc0cbd2c9b6f0ac8037fd90e276c65844; sid_guard=77066df5297676b148df690836bac9ea%7C1539280576%7C5184000%7CMon%2C+10-Dec-2018+17%3A56%3A16+GMT; uid_tt=b1fe77b7423959544e77e71126f0f0ef; sid_tt=77066df5297676b148df690836bac9ea; sessionid=77066df5297676b148df690836bac9ea; install_id=46961748949; ttreq=1$3154adbaa6f2ab4377c851ceb5e0878b8b73a80a'
}

# base_url = 'https://api.amemv.com/aweme/v1/category/list/'

base_url = 'https://api.amemv.com/aweme/v1/challenge/aweme/'

response = requests.get(base_url, params=query, verify=False, headers=headers)
print(response.url)
print(response.status_code)
print(response.json())
