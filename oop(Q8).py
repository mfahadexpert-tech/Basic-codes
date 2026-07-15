#Ek Song class banayein jahan __init__ constructor ke zariye user 
# naye song ka title aur artist object
#banate waqt hi pass kar sake.
class song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def display_info(self):
        print(f"Song Title: {self.title}")
        print(f"Artist: {self.artist}")
s=song("Shape of You", "Ed Sheeran")
s1=song("Perfect", "Nusrat")
s.display_info()
s1.title = "Perfect"
s1.artist="nusrat"
s1.display_info()