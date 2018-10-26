from douyin.config import hot_search_url
from douyin.structures import HotSearch
from douyin.utils import fetch


def search():
    """
    get hot search result
    :return: HotSearch object
    """
    result = fetch(hot_search_url)
    # process json data
    datetime = result.get('data', {}).get('active_time')
    word_list = result.get('data', {}).get('word_list', [])
    data = [{'item': item.get('word'), 'hot_value': item.get('hot_value')} for item in word_list]
    # construct HotSearch object and return
    return HotSearch(datetime=datetime, data=data)
