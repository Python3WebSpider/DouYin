from urllib.parse import urlparse, parse_qs


def parse_query(url):
    """
    get query dict of url
    :param url:
    :return:
    """
    result = urlparse(url)
    query = result.query
    query_dict = parse_qs(query)
    query_dict = {k: v[0] for k, v in query_dict.items()}
    return query_dict
