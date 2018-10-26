from douyin.utils.fetch import fetch
from douyin.config import music2video_url, common_headers


class Music(object):
    
    def __init__(self, **kwargs):
        """
        music init args
        :param kwargs:
        """
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.cover_url = kwargs.get('cover_url')
        self.play_url = kwargs.get('play_url')
        self.owner_id = kwargs.get('owner_id')
        self.owner_name = kwargs.get('owner_name')
        self.hot_count = kwargs.get('hot_count')
    
    def __repr__(self):
        """
        music to str
        :return:
        """
        return '<Music: <%s, %s>>' % (self.id, self.name)
    
    def videos(self):
        """
        get videos of topic
        :return:
        """
        from douyin.utils.tranform import data_to_video
        query = {
            'device_id': '33333333',
            'music_id': self.id,
            'count': '18',
        }
        offset = 0
        while True:
            # define cursor
            query['cursor'] = str(offset)
            print(query)
            result = fetch(music2video_url, params=query, headers=common_headers, verify=False)
            print(result)
            aweme_list = result.get('aweme_list', [])
            for item in aweme_list:
                video = data_to_video(item)
                yield video
            # next page
            if result.get('has_more'):
                offset += 18
            else:
                break
