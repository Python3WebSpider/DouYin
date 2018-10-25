# DouYin API

Api of douyin app for humans.

## Installation

```
pip3 install douyin
```

## Usage

Here is the sample code:

```python
import douyin

# HotVideo
search_video = douyin.hot.video()
# video objects
videos = search_video.data
# print every video
for video in videos:
    print(video)
    print(video.author)
    print(video.music)
    print(video.address)

# define handler and specify folder
handler = douyin.handlers.FileHandler(folder='./downloads')
# define downloader
downloader = douyin.downloaders.VideoDownloader([handler])
# download videos
downloader.download(videos)

```

then you can get:

```
<Video: <6613646708372933902, #哈士奇 #捏一下就>>
<User: <1550299675, 二哈撒手没的日常>>
<Music: <6574318393246092046, 断线>>
<Address: <B02000JML4, 太湖>>
<Video: <6613934804712819971, #室友 快艾特室友们>>
<User: <ACE_00, ACE_共犯>>
<Music: <6607667275321314051, @是你的很美味创作的原声>>
None
0%|                                                    | 0/20 [00:00<?, ?it/s]
Downloading <Video: <6613646708372933902, #哈士奇 #捏一下就>> ...
  5%|██▏                                         | 1/20 [00:01<00:19,  1.02s/it]
Downloading <Video: <6613934804712819971, #室友 快艾特室友们>> ...
 10%|████▍                                       | 2/20 [00:05<00:35,  1.97s/it]
Downloading <Video: <6614442537929149703, 哈哈哈😄😂够我笑一年>> ...
 15%|██████▌                                     | 3/20 [00:07<00:34,  2.03s/it]
Downloading <Video: <6613545646597082372, #这可能是你从没听过>> ...
 20%|████████▊                                   | 4/20 [00:09<00:35,  2.20s/it]
Downloading <Video: <6614086376252001544, 余生有你 请多指教@>> ...
```

![](https://ws3.sinaimg.cn/large/006tNbRwgy1fwjsl8n4bhj315u17uaei.jpg)
