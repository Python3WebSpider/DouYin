# urls
hot_search_url = 'https://api.amemv.com/aweme/v1/hot/search/list/'
hot_video_url = 'https://api.amemv.com/aweme/v1/hotsearch/aweme/billboard/'
hot_energy_url = 'https://api.amemv.com/aweme/v1/hotsearch/positive_energy/billboard/'
hot_music_url = 'https://api.amemv.com/aweme/v1/hotsearch/music/billboard/'
hot_trend_url = 'https://api.amemv.com/aweme/v1/category/list/'
topic2video_url = 'https://api.amemv.com/aweme/v1/challenge/aweme/'
music2video_url = 'https://api.amemv.com/aweme/v1/music/aweme/'

# http
fetch_timeout = 5
common_headers = {
    # 'User-Agent': 'Aweme 2.9.1 rv:29101 (iPhone; iOS 12.0; zh_CN) Cronet',
    'User-Agent': 'Aweme 3.1.0 rv:31006 (iPhone; iOS 12.0; zh_CN) Cronet'
}

# retrying
retry_max_number = 10
retry_min_random_wait = 1000  # ms
retry_max_random_wait = 5000  # ms
