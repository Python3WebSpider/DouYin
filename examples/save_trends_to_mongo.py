import douyin
from douyin.structures import Topic, Music

# define handler
mongo_handler = douyin.handlers.MongoHandler()
# define downloader and specify handler
downloader = douyin.downloaders.VideoDownloader([mongo_handler])

for result in douyin.hot.trend():
    for item in result.data:
        # download videos of topic/music for 100 max per
        if isinstance(item, Topic):
            print('Get topic', item)
            downloader.download(item.videos(max=100))
        if isinstance(item, Music):
            print('Item', item)
            downloader.download(item.videos(max=100))
