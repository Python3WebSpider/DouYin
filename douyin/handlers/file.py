from os.path import join, exists
from os import makedirs
from douyin.handlers import Handler
from douyin.utils.type import mime_to_ext
import aiohttp


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
    
    async def process(self, url, name, **kwargs):
        """
        download to file
        :param url: resource url
        :param name: save name
        :param kwargs:
        :return:
        """
        kwargs.update({'ssl': False})
        async with aiohttp.ClientSession() as session:
            async with session.get(url, **kwargs) as response:
                if response.status == 200:
                    extension = mime_to_ext(response.headers.get('Content-Type'))
                    full_path = join(self.folder, '%s.%s' % (name, extension))
                    with open(full_path, 'wb') as f:
                        f.write(await response.content.read())
                    print('Downloaded file to', full_path)
                else:
                    print('Cannot download %s, response status %s' % (name, response.status))
