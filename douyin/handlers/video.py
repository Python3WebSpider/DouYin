from douyin.handlers import FileHandler
from douyin.structures import Video


class VideoFileHandler(FileHandler):
    
    async def process(self, obj, **kwargs):
        """
        process video obj
        :param obj:
        :param kwargs:
        :return:
        """
        if isinstance(obj, Video):
            return await self._process(obj, **kwargs)
