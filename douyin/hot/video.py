from douyin.config import hot_video_url
from douyin.structures import HotVideo
from douyin.utils import fetch
from douyin.utils.tranform import data_to_video, parse_datetime


def video():
    """
    get hot video result
    :return: HotVideo object
    """
    result = fetch(hot_video_url)
    # process json data
    datetime = parse_datetime(result.get('active_time'))
    video_list = result.get('aweme_list', [])
    videos = []
    for item in video_list:
        video = data_to_video(item.get('aweme_info'))
        video.hot_count = item.get('hot_value')
        videos.append(video)
    # construct HotVideo object and return
    return HotVideo(datetime=datetime, data=videos)
