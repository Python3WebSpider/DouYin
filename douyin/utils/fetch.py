import requests
from retrying import retry

from douyin.config import retry_max_number, retry_min_random_wait, retry_max_random_wait, fetch_timeout


def need_retry(exception):
    """
    need to retry
    :param exception:
    :return:
    """
    result = isinstance(exception, (requests.ConnectionError, requests.ReadTimeout))
    if result:
        print('Exception', type(exception), 'occurred, retrying...')
    return result


def fetch(url, **kwargs):
    """
    warp _fetch method
    :param url: fetch url
    :param kwargs: other requests params
    :return: result of _fetch
    """
    
    @retry(stop_max_attempt_number=retry_max_number, wait_random_min=retry_min_random_wait,
           wait_random_max=retry_max_random_wait, retry_on_exception=need_retry)
    def _fetch(url, **kwargs):
        """
        fetch api response
        :param url: fetch url
        :param kwargs: other requests params
        :return: json of response
        """
        kwargs.update({'verify': False})
        kwargs.update({'timeout': fetch_timeout})
        response = requests.get(url, **kwargs)
        if response.status_code != 200:
            raise requests.ConnectionError('Expected status code 200, but got {}'.format(response.status_code))
        return response.json()
    
    try:
        result = _fetch(url, **kwargs)
        return result
    # give up retrying
    except (requests.ConnectionError, requests.ReadTimeout):
        return {}
