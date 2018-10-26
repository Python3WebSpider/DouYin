import douyin
from douyin.structures import Topic, Music

# define file handler and specify folder
file_handler = douyin.handlers.FileHandler(folder='./videos')
# define mongodb handler
mongo_handler = douyin.handlers.MongoHandler()
# define downloader
downloader = douyin.downloaders.VideoDownloader([mongo_handler, file_handler])

for result in douyin.hot.trend():
    for item in result.data:
        # download videos of topic/music for 200 max per
        if isinstance(item, Topic):
            print('Item', item)
            downloader.download(item.videos(max=30))
        if isinstance(item, Music):
            print('Item', item)
            downloader.download(item.videos(max=30))
