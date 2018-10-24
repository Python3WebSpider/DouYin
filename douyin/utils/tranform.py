import json
from douyin.structure import Video, User
import dateparser


def parse_datetime(string):
    """
    parse string to datetime safely
    :param string: str to parse
    :return: datetime
    """
    if not string:
        return None
    return dateparser.parse(str(string))


def first(array):
    """
    get first element of list or None
    :param array:
    :return:
    """
    if isinstance(array, list) and len(array) > 1:
        return array[0]
    return None


def get_video_url(array):
    """
    get video url from list
    :param array:
    :return:
    """
    if isinstance(array, list) and len(array) > 1:
        return array[-1]
    return None


def data_to_video(data):
    """
    transfer json data to video object
    :param data:
    :return:
    """
    statistics = data.get('statistics', {})
    like_count = statistics.get('digg_count')
    comment_count = statistics.get('comment_count')
    share_count = statistics.get('share_count')
    id = statistics.get('aweme_id')
    desc = data.get('desc')
    is_ads = data.get('is_ads')
    duration = data.get('duration')
    create_time = parse_datetime(data.get('create_time'))
    share_url = data.get('share_url')
    ratio = data.get('video', {}).get('ratio')
    cover = first(data.get('video', {}).get('origin_cover', {}).get('url_list'))
    play_url = get_video_url(data.get('video', {}).get('play_addr', {}).get('url_list'))
    author = data_to_user(data.get('author', {}))
    return Video(
        id=id,
        desc=desc,
        like_count=like_count,
        share_count=share_count,
        comment_count=comment_count,
        is_ads=is_ads,
        duration=duration,
        create_time=create_time,
        share_url=share_url,
        ratio=ratio,
        cover=cover,
        play_url=play_url,
        author=author
    )


def data_to_music(data):
    pass


def data_to_user(data):
    alias = data.get('unique_id') or data.get('short_id')
    id = data.get('uid')
    name = data.get('nickname')
    sign = data.get('signature')
    avatar = first(data.get('avatar_larger', {}).get('url_list', []))
    gender = data.get('gender')
    birthday = data.get('birthday')
    create_time = parse_datetime(data.get('create_time'))
    verify = bool(data.get('custom_verify').strip())
    verify_info = data.get('custom_verify').strip()
    return User(
        id=id,
        alias=alias,
        name=name,
        sign=sign,
        avatar=avatar,
        gender=gender,
        verify=verify,
        verify_info=verify_info,
        create_time=create_time,
        birthday=birthday
    )
