# import fruits

# fruits.apple()
# print fruits.marmalade

# fruits['apple':'this is dictionary']
# fruits.apple()
# fruits.marmalade

# print fruits['apple']

class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                    "I don't wnat to get sued",
                    "So I'll stop right there."])

bulls_on_parade = Song(["They rally arround the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()