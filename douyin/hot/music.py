from douyin.config import hot_music_url
from douyin.structure import HotMusic
from douyin.utils import fetch

# todo


def music():
    """
    get hot music result
    :return: HotMusic object
    """
    result = fetch(hot_music_url)
    # process json data
    active_time = result.get('active_time')
    video_list = result.get('music_list', [])
    data = [{'item': item.get('music_info'), 'hot_value': item.get('hot_value')} for item in video_list]
    # construct HotMusic object and return
    return HotMusic(active_time=active_time, data=data)
