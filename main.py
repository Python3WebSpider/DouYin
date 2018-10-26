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
# handler = douyin.handlers.FileHandler(folder='./videos')
# # define downloader
# downloader = douyin.downloaders.VideoDownloader([handler])
# # download videos
# downloader.download(videos)
# from douyin.structures import Topic
from douyin.structures import Topic, Music

for result in douyin.hot.trend():
    print(result)
    for item in result.data:
        # if isinstance(item, Topic):
        #     print(item)
        #     for video in item.videos():
        #         print(video)
        if isinstance(item, Music):
            print(item)
            for video in item.videos():
                print(video)
