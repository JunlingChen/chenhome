import threading
import time
import multiprocessing


movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxx.mp4"]
music_list = ['周杰伦.mp3', '五月天.mp3']
movie_format = ['mp4', 'avi']
music_format = ['mp3']


def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("你现在收看的是：{}".format(i))
            time.sleep(3)
        elif i.split(".")[1] in music_format:
            print("你现在收听的是:{}".format(i))
            time.sleep(2)
        else:
            print("没有能播放的格式")


def thread_run():
    t1 = threading.Thread(target=play, args=(movie_list,))
    t2 = threading.Thread(target=play, args=(music_list,))
    t1.start()
    t2.start()

#
# if __name__ == "__main__":
#     thread_run()


# 类的方式去完成

class MyThread(threading.Thread):
    def __init__(self, playlist):
        super().__init__()
        self.playlist = playlist

    def run(self):
        play(self.playlist)



# if __name__ == "__main__":
#     m1 = MyThread(movie_list)
#     m2 = MyThread(music_list)
#     m1.start()
#     m2.start()


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=play, args=(movie_list,))
    t2 = multiprocessing.Process(target=play, args=(music_list,))

    t1.start()
    t2.start()