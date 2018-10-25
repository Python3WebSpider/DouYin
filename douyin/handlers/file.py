from os.path import join, exists
from os import makedirs
import requests
from douyin.handlers import Handler
from mimetypes import guess_extension
from douyin.utils.type import mime_to_ext


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
        kwargs.update({'verify': False})
        with requests.get(url, **kwargs) as response:
            extension = mime_to_ext(response.headers.get('Content-Type'))
            full_path = join(self.folder, '%s.%s' % (name, extension))
            with open(full_path, 'wb') as f:
                f.write(response.content)
            print('Downloaded file to', full_path)
