from douyin.config import hot_energy_url
from douyin.structures import HotEnergy
from douyin.utils import fetch


# todo

def energy():
    """
    get hot energy result
    :return: HotEnergy object
    """
    result = fetch(hot_energy_url)
    # process json data
    active_time = result.get('active_time')
    video_list = result.get('aweme_list', [])
    data = [{'item': item.get('aweme_info'), 'hot_value': item.get('hot_value')} for item in video_list]
    # construct HotEnergy object and return
    return HotEnergy(active_time=active_time, data=data)
