from douyin.config import hot_video_url
from douyin.structure import HotVideo
from douyin.utils import fetch


def video():
    """
    get hot video result
    :return: HotSearch object
    """
    result = fetch(hot_video_url, verify=False)
    print(result)
    # process json data
    active_time = result.get('data', {}).get('active_time')
    video_list = result.get('data', {}).get('aweme_list', [])
    print(video_list)
    data = [{'item': item.get('aweme_info'), 'hot_value': item.get('hot_value')} for item in video_list]
    # construct HotSearch object and return
    return HotVideo(active_time=active_time, data=data)
