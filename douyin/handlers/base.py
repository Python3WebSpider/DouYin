class Handler(object):
    
    def process(self, obj, **kwargs):
        """
        parent method, you must implement this method in child object
        :param obj:
        :param kwargs:
        :return:
        """
        raise NotImplementedError
