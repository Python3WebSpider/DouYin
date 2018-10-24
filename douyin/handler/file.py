from os.path import join, exists
from os import makedirs
import requests
from douyin.handler import Handler


class FileHandler(Handler):
    
    def __init__(self, folder):
        """
        init save folder
        :param folder:
        """
        super().__init__()
        self.folder = folder
        if not exists(self.folder):
            makedirs(self.folder)
    
    def process(self, url, name, **kwargs):
        """
        download to file
        :param url: resource url
        :param name: save name
        :param kwargs:
        :return:
        """
        full_path = join(self.folder, name)
        kwargs.update({'verify': False})
        with requests.get(url, **kwargs) as response:
            with open(full_path, 'wb') as f:
                f.write(response.content)
