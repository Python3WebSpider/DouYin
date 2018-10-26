#!pip install douyin

import douyin

#
# # HotMusic
# result = douyin.hot.music()
# # music objects
# musics = result.data
# # print every music
# for music in musics:
#     print(music)
#
# # define handler and specify folder
# handler = douyin.handlers.FileHandler(folder='./musics')
# # define downloader
# downloader = douyin.downloaders.MusicDownloader([handler])
# # download musics
# downloader.download(musics)
#
# # HotVideo
# result = douyin.hot.video()
# # video objects
# videos = result.data
# # print every video
# for video in videos:
#     print(video)
#
# # define handler and specify folder
# file_handler = douyin.handlers.FileHandler(folder='./videos')
mongo_handler = douyin.handlers.MongoHandler()
# # define downloader
downloader = douyin.downloaders.VideoDownloader([mongo_handler])
# # download videos
# downloader.download(videos)
# from douyin.structures import Topic
from douyin.structures import Topic, Music

for result in douyin.hot.trend():
    print(result)
    for item in result.data:
        if isinstance(item, Topic):
            print('Item', item)
            downloader.download(item.videos(max=100))
        if isinstance(item, Music):
            print('Item', item)
            downloader.download(item.videos(max=100))
