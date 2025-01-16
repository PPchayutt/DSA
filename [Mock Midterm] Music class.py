class Song:
    def __init__(self, name, genre, durations):
        self.name = name
        self.genre = genre
        self.durations = durations

    def ftime(self):
        return self.durations // 60
    
    def rtime(self):
        return self.durations % 60

    def show_info(self):
        return (f"{self.name} <|> {self.genre} <|> {Rickroll.ftime()}.{Rickroll.rtime():02}")
    
Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())
