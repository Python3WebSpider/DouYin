import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from douyin.utils.fetch import fetch
