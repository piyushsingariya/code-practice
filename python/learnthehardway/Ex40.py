class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    
happ_bday = Song(["Happy birthday to you",
                    "Happy Birthday to you",
                    "Happy Birthday to you",
                    "Happy Birthday, dear ____ _____",
                    "Happy Birthday to you."])

happ_bday.sing_me_a_song()