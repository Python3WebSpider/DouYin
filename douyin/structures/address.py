from douyin.structures import Base


class Address(Base):
    
    def __init__(self, **kwargs):
        """
        init address object
        :param kwargs:
        """
        super().__init__()
        self.id = kwargs.get('id')
        self.province = kwargs.get('province')
        self.city = kwargs.get('city')
        self.district = kwargs.get('district')
        self.full = kwargs.get('full')
        self.address = kwargs.get('address')
        self.place = kwargs.get('place')
        self.postal_code = kwargs.get('postal_code')
        self.longitude = kwargs.get('longitude')
        self.latitude = kwargs.get('latitude')
    
    def __repr__(self):
        """
        address to str
        :return:
        """
        return '<Address: <%s, %s>>' % (self.id, self.place)
