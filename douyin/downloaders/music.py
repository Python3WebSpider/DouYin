from douyin.structures import Music
from douyin.handlers import Handler
from douyin.downloaders import Downloader


class MusicDownloader(Downloader):
    
    def process_item(self, obj):
        """
        process item
        :param obj: single obj
        :return:
        """
        if isinstance(obj, Music):
            print('\nDownloading', obj, '...')
            for handler in self.handlers:
                if isinstance(handler, Handler):
                    handler.process(obj.play_url, obj.id)
