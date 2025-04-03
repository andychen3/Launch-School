# https://launchschool.com/exercises/eae55f25

"""
input: Takes in an integer input to represent 
how many bottles of beer is on the wall
output: The beer song 
rules:
1. The parameters is optional on the second. if it's not provided then it does 
1 verse.
2. if it is provided it keeps going
3. If there is none it has to say no more.
4. Lyrics method does the whole thing.

DS:

Algo:


"""

class BeerSong:



    @classmethod
    def verse(cls, end, start=None):
        """
        - If second parameter is not passed then it does one verse
        - If second parameter is passed then 
        """
        song_lyrics = []

        if start is None:
            start = end

        for bottles in range(end, start - 1, -1):
            if bottles > 1:
                lyric = (f"{bottles} bottles of beer on the wall, {bottles} {cls.get_bottles(bottles)} of beer.\n"
                         f"Take one down and pass it around, {bottles - 1} {cls.get_bottles(bottles - 1)} of beer on the wall.\n")
                song_lyrics.append(lyric)
            elif bottles == 1:
                lyric = (f"{bottles} bottle of beer on the wall, {bottles} {cls.get_bottles(bottles)} of beer.\n"
                         f"Take it down and pass it around, no more {cls.get_bottles(bottles - 1)} of beer on the wall.\n")
                song_lyrics.append(lyric)
            else:
                lyric = (f"No more bottles of beer on the wall, no more bottles of beer.\n"
                         "Go to the store and buy some more, 99 bottles of beer on the wall.\n")
                song_lyrics.append(lyric)

        return "\n".join(song_lyrics)
    
    @classmethod
    def verses(cls, end, start):
        return cls.verse(end, start)

    @classmethod
    def lyrics(cls):
        return cls.verse(99, 0)
    
    @staticmethod
    def get_bottles(bottle):
        if bottle == 1:
            return "bottle"
        return "bottles"