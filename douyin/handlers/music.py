from douyin.handlers import FileHandler
from douyin.structures import Music, Video


class MusicFileHandler(FileHandler):
    
    async def process(self, obj, **kwargs):
        """
        process music
        :param obj:
        :param kwargs:
        :return:
        """
        if isinstance(obj, Video):
            obj = obj.music
            if isinstance(obj, Music):
                return await self._process(obj, **kwargs)
