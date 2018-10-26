import requests
from retrying import retry


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
    
    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=3000, retry_on_exception=need_retry)
    def _fetch(url, **kwargs):
        """
        fetch api response
        :param url: fetch url
        :param kwargs: other requests params
        :return: json of response
        """
        kwargs.update({'verify': False})
        kwargs.update({'timeout': 2})
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
