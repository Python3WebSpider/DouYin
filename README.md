# DouYin

API of DouYin App for humans.

## Installation

```
pip3 install douyin
```

## Usage

Here is the sample code:

```python
import douyin
from douyin.structures import Topic, Music

# define file handler and specify folder
video_file_handler = douyin.handlers.VideoFileHandler(folder='./videos')
music_file_handler = douyin.handlers.MusicFileHandler(folder='./musics')
# define mongodb handler
mongo_handler = douyin.handlers.MongoHandler()
# define downloader
downloader = douyin.downloaders.VideoDownloader([mongo_handler, video_file_handler, music_file_handler])

for result in douyin.hot.trend():
    for item in result.data:
        # download videos of topic/music for 100 max per
        downloader.download(item.videos(max=100))
```

then you can get:

```
Item <Topic: <1565818716518401, panama>>
Processing <Video: <6616517521098935565, 真香#panama>> ...
Processing <Video: <6500385230921141518, 哈哈哈哈哈>> ...
...
Processing <Video: <6479958542747962637, 👅ก่อนกินข้>> ...
Processing <Video: <6473811426107460878, 😁>> ...
0%|                                                      | 0/10 [00:00<?, ?it/s]
Processing 1-10 of files
Processing <Video: <6616517521098935565, 真香#panama>> ...
Saving <Video: <6616517521098935565, 真香#panama>> to mongodb...
Processing <Video: <6500385230921141518, 哈哈哈哈哈>> ...
Saving <Video: <6500385230921141518, 哈哈哈哈哈>> to mongodb...
Processing <Video: <6562690160868199693, 皇城相府版C哩C哩跨>> ...
....
Downloading <Video: <6580510322468064526, 第二遍 后面的小哥哥>> ...
Saved <Video: <6479958542747962637, 👅ก่อนกินข้>> to mongodb successfully
Downloading <Video: <6479958542747962637, 👅ก่อนกินข้>> ...
Saved <Video: <6473811426107460878, 😁>> to mongodb successfully
Downloading <Video: <6473811426107460878, 😁>> ...
Downloaded file to ./videos/6580510322468064526.mp4
10%|████▌                                         | 1/10 [00:01<00:16,  1.84s/it]
Downloaded file to ./videos/6516746291806997763.mp4
20%|█████████▏                                    | 2/10 [00:01<00:10,  1.33s/it]
Downloaded file to ./videos/6600742831352974596.mp4
40%|██████████████████▍                           | 4/10 [00:02<00:05,  1.03it/s]
Downloaded file to ./videos/6484393014599879950.mp4
50%|███████████████████████                       | 5/10 [00:02<00:04,  1.15it/s]
Downloaded file to ./videos/6616517521098935565.mp4
60%|███████████████████████████▌                  | 6/10 [00:03<00:03,  1.27it/s]
Downloaded file to ./videos/6479958542747962637.mp4
70%|████████████████████████████████▏             | 7/10 [00:03<00:01,  1.68it/s]
Downloaded file to ./videos/6472305134377372941.mp4
80%|████████████████████████████████████▊         | 8/10 [00:03<00:00,  2.05it/s]
Downloaded file to ./videos/6562690160868199693.mp4
90%|█████████████████████████████████████████▍    | 9/10 [00:04<00:00,  2.27it/s]
Downloaded file to ./videos/6500385230921141518.mp4
100%|█████████████████████████████████████████████| 10/10 [00:04<00:00,  2.33it/s]
```

![](https://ws2.sinaimg.cn/large/006tNbRwgy1fwmad1yh6wj30lf0p3aaf.jpg)

![](https://ws3.sinaimg.cn/large/006tNbRwly1fwo1ystiraj30lg0e3gm0.jpg)

![](https://ws3.sinaimg.cn/large/006tNbRwly1fwo20dbzduj30lg0e3q49.jpg)

![](https://ws2.sinaimg.cn/large/006tNbRwly1fwo21zyfkyj30jm0m175e.jpg)

## Examples

See [examples](./examples)
