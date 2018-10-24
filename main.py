# from douyin.hot import search

import douyin

# result = search()
# print(result)
#
# print(result.data)

# search_result = douyin.hot.search()
search_video = douyin.hot.video()
# search_energy = douyin.hot.energy()
# print(search_energy)

# search_energy = douyin.hot.energy()
# print(se)

# search_music = douyin.hot.music()
# print(search_music)

# print(search_result)

# print(search_result)
# print(search_video)

videos = search_video.data
for video in videos:
    print(video)
    print(video.author)
    print(video.music)
