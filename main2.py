from douyin.structures import Video, Music

import datetime

music = Music(id='xxxx', name='sdfsdfsdf')
v = Video(id='xxxx', ratio=333, create_time=datetime.datetime(2018, 1, 23))
v.music = music

print(v)
print(v.__dict__)

print(v.json())
