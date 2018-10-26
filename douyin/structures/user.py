from douyin.structures import Base


class User(Base):
    
    def __init__(self, **kwargs):
        """
        init user object
        :param kwargs:
        """
        super().__init__()
        self.id = kwargs.get('id')
        self.gender = kwargs.get('gender')
        self.name = kwargs.get('name')
        self.create_time = kwargs.get('create_time')
        self.birthday = kwargs.get('birthday')
        self.sign = kwargs.get('sign')
        self.alias = kwargs.get('alias')
        self.avatar = kwargs.get('avatar')
        self.verify = kwargs.get('verify')
        self.verify_info = kwargs.get('verify_info')
    
    def __repr__(self):
        """
        user to str
        :return:
        """
        return '<User: <%s, %s>>' % (self.alias, self.name)
