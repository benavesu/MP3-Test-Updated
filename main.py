import winsound
import lyricwikia
import time
from threading import Thread

##Introduction and heading
print("YOU ARE LISTENING TO: \n\n ♫♪♩ WHAM! Careless Whisper ♫♪♩ \n \t______________ \n")



#Creating two seperate functions for each action to be executed (lyrics and song)
def lyrics():
    print()
    time.sleep(15.0)
    print("Oh Ooo Whoah-Ooo Whoah")
    time.sleep(2.0)
    print("Ohh Huuuh")
    time.sleep(5.0)
    
    lyrics = lyricwikia.get_lyrics('wham', 'careless whisper') #API for getting full song lyrics
    listLyrics = []
    listLyrics = lyrics.split('\n') #places lyrics in listLyrics array

    listLyrics = listLyrics[9:68] #has only the lyrics from indexes 9 to 69
    
    time.sleep(5.5)
    print(listLyrics[0]) #space
    print(listLyrics[1]) #I feel so unsure
    time.sleep(6.0)
    print(listLyrics[2]) #as I take your hand
    time.sleep(7.0)
    print(listLyrics[3])#as the music dies
    time.sleep(2.5)
    print(listLyrics[4]) #something in your eyes
    time.sleep(3.0)
    print(listLyrics[5]) #calls to mind the silver screen
    time.sleep(2.0)
    print(listLyrics[6]) #space
    time.sleep(5.0)
    print(listLyrics[7]) #I'm never gonna dance again
    time.sleep(3.0)
    print(listLyrics[8]) #guilty feet
    time.sleep(3.0)
    print(listLyrics[9]) #though it's easy to pretend
    time.sleep(2.5)
    print(listLyrics[10]) #I know you're not a fool
    time.sleep(2.0)
    print(listLyrics[11])#space
    time.sleep(2.0)
    print(listLyrics[12])#shouldve known better than to cheat a friend
    time.sleep(2.5)
    print(listLyrics[13]) #and waste the chance that I've been givem
    time.sleep(3.5)
    print(listLyrics[14]) #so I'm never gonna dance again
    time.sleep(3.0)
    print(listLyrics[15]) #the way I danced with you
    time.sleep(4.5)
    print("Ohhhh Huuuuh")
    time.sleep(11.0)
    print()
    print("Hope you enjoyed ヾ(*◎○◎)ﾉ♫♪♩") 

def song():
    #winsound command that will actually play the song
    winsound.PlaySound("Careless Whisper- George Michael (Lyrics).wav", winsound.SND_ASYNC)
    #The song is roughly 342 seconds long, so I had the time.sleep() to 350 seconds
    time.sleep(350.0)

#using multithreading to run both functions simultaneously
if __name__ == '__main__':
    Thread(target = lyrics).start()
    Thread(target = song).start()


