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
