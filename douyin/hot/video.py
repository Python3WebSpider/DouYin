from douyin.config import hot_video_url
from douyin.structure import HotVideo
from douyin.utils import fetch


def video():
    """
    get hot video result
    :return: HotVideo object
    """
    result = fetch(hot_video_url)
    # process json data
    active_time = result.get('active_time')
    video_list = result.get('aweme_list', [])
    data = [{'item': item.get('aweme_info'), 'hot_value': item.get('hot_value')} for item in video_list]
    # construct HotVideo object and return
    return HotVideo(active_time=active_time, data=data)
