import requests


def fetch(url, **kwargs):
    """
    fetch api response
    :param url: fetch url
    :param kwargs: other requests params
    :return: json of response
    """
    kwargs.update({'verify': False})
    response = requests.get(url, **kwargs)
    if response.status_code != 200:
        raise requests.ConnectionError('Expected status code 200, but got {}'.format(response.status_code))
    return response.json()
