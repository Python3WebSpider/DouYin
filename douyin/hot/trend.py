from douyin.utils import fetch
from douyin.config import hot_trend_url, common_headers
from douyin.utils.tranform import data_to_music, data_to_topic
from douyin.structures.hot import HotTrend
from douyin.utils.common import parse_datetime


# define trend query params
query = {
    'version_code': '2.9.1',
    'count': '10',
}


def trend():
    """
    get trend result
    :return:
    """
    offset = 0
    while True:
        query['cursor'] = str(offset)
        result = fetch(hot_trend_url, headers=common_headers, params=query, verify=False)
        category_list = result.get('category_list')
        datetime = parse_datetime(result.get('extra', {}).get('now'))
        final = []
        for item in category_list:
            # process per category
            if item.get('desc') == '热门话题':
                final.append(data_to_topic(item.get('challenge_info', {})))
            if item.get('desc') == '热门音乐':
                final.append(data_to_music(item.get('music_info', {})))
        yield HotTrend(datetime=datetime, data=final, offset=offset, count=int(query.get('count')))
        offset += 10
