class Video():
    
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.desc = kwargs.get('desc')
        self.author = kwargs.get('author')
        self.music = kwargs.get('music')
        self.like_count = kwargs.get('like_count')
        self.comment_count = kwargs.get('comment_count')
        self.share_count = kwargs.get('share_count')
        self.video_url = kwargs.get('video_url')
        self.is_ads = kwargs.get('is_ads') or False
        self.duration = kwargs.get('duration')
        self.create_time = kwargs.get('create_time')
        self.share_url = kwargs.get('share_url')
        self.ratio = kwargs.get('ratio')
        self.cover = kwargs.get('cover')
        self.address = kwargs.get('address')
    
    # def
