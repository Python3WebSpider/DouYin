#!pip install douyin

import douyin

# Hotmusic
result = douyin.hot.music()
# music objects
musics = result.data
# print every music
for music in musics:
    print(music)

# define handler and specify folder
handler = douyin.handlers.FileHandler(folder='./musics')
# define downloader
downloader = douyin.downloaders.MusicDownloader([handler])
# download musics
downloader.download(musics)
