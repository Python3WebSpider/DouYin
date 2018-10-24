# url = 'https://aweme.snssdk.com/aweme/v1/hot/search/list/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&detail_list=1&mas=018fa49f892cef47483e66cfafc93cb60218333ead79ec36a2e727&as=a1958f5c7b791bf03f3994&ts=1540354203'
import json
from urllib.parse import urlparse, parse_qs

# url = 'https://api.amemv.com/aweme/v1/hotsearch/aweme/billboard/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&mas=01e3e5cef0de029bfcdd34f97a802bb868733f3265261a5cdb072e&as=a13500cd74892b29d04593&ts=1540360596'

# url = 'https://api.amemv.com/aweme/v1/hot/search/list/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&detail_list=0&mas=01b4002e3d345720d85d1983fe6b328535431c67b1f365be1f2f38&as=a1e5000df9532bbfa03287&ts=1540362041'

url = 'https://api.amemv.com/aweme/v1/hotsearch/positive_energy/billboard/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&mas=0126b21946481b48568f8847ece5918e73ccee5c12110cae38cf31&as=a1a5d22deffc2bd0109280&ts=1540366543'


result = urlparse(url)
print(result)

query = result.query
print(query)

query_dict = parse_qs(query)
print(query_dict)

query_dict = {k: v[0] for k, v in query_dict.items()}
print(query_dict)

print(json.dumps(query_dict, indent=2))
