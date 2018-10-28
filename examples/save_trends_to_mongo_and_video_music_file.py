import douyin
from douyin.structures import Topic, Music

# define file handler and specify folder
video_file_handler = douyin.handlers.VideoFileHandler(folder='./videos')
music_file_handler = douyin.handlers.MusicFileHandler(folder='./musics')
# define mongodb handler
mongo_handler = douyin.handlers.MongoHandler(conn_uri='localhost')
# define downloader
downloader = douyin.downloaders.VideoDownloader([mongo_handler, video_file_handler, music_file_handler])

for result in douyin.hot.trend():
    for item in result.data:
        # download videos of topic/music for 30 max per
        if isinstance(item, Topic):
            print('Item', item)
            downloader.download(item.videos(max=30))
        if isinstance(item, Music):
            print('Item', item)
            downloader.download(item.videos(max=30))
