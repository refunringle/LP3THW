class song (object):
    def __init__(self,lyric):
        self.lyric=lyric

    def song_line (self):
        for i in self.lyric:
            print(i)

a=song(['happy birthday to you',
'this for you','and so this is so happy','but now its rainy time'])

a.song_line()