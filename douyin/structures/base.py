import datetime
from copy import deepcopy


class Base():
    
    def json(self):
        """
        object to json
        :return:
        """
        from douyin.structures import Video, Music, User, Topic, Address
        # transfer object to dict
        d = deepcopy(self.__dict__)
        # iterate every attribute
        for k, v in d.items():
            if not v:
                continue
            # recurrent call json method
            if isinstance(v, (Video, Music, User, Topic, Address)):
                d[k] = v.json()
            # to string
            if isinstance(v, datetime.datetime):
                d[k] = str(v)
        return d
