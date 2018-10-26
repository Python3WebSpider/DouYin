from douyin.structures import Music
from douyin.handlers import Handler
from douyin.downloaders import Downloader


class MusicDownloader(Downloader):
    
    async def process_item(self, obj):
        """
        process item
        :param obj: single obj
        :return:
        """
        if isinstance(obj, Music):
            print('Processing', obj, '...')
            for handler in self.handlers:
                if isinstance(handler, Handler):
                    await handler.process(obj)
