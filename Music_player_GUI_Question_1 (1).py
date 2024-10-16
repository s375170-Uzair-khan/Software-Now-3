
# Importing all the necessary modules
from tkinter import *
from tkinter import filedialog

# pip install pygame
import pygame.mixer as mixer  
import os

# Initializing the mixer
mixer.init()

# Define a MusicPlayer class to encapsulate the functionality
class MusicPlayer(Tk):
    def __init__(self):
        super().__init__()

        # GUI Initialization
        self.geometry('700x220')  #
        self.title('MP3 Music Player')
        self.resizable(0, 0)

        # All the frames
        self.song_frame = LabelFrame(self, text='Current Song', bg='Blue', width=400, height=80)
        self.song_frame.place(x=0, y=0)

        self.button_frame = LabelFrame(self, text='Control Buttons', bg='Turquoise', width=400, height=120)
        self.button_frame.place(y=80)

        self.listbox_frame = LabelFrame(self, text='Playlist', bg='RoyalBlue')
        self.listbox_frame.place(x=400, y=0, height=200, width=300)

        # All StringVar variables
        self.current_song = StringVar(self, value='<Not selected>')

        self.song_status = StringVar(self, value='<Not Available>')

        # Playlist ListBox
        self.playlist = Listbox(self.listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

        self.scroll_bar = Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scroll_bar.pack(side=RIGHT, fill=BOTH)

        self.playlist.config(yscrollcommand=self.scroll_bar.set)

        self.scroll_bar.config(command=self.playlist.yview)

        self.playlist.pack(fill=BOTH, padx=5, pady=5)

        # SongFrame Labels
        Label(self.song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)

        self.song_lbl = Label(self.song_frame, textvariable=self.current_song, bg='Goldenrod',
                              font=("Times", 12), width=25)
        self.song_lbl.place(x=150, y=20)

        # Buttons in the main screen
        self.pause_btn = Button(self.button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=7,
                                command=self.pause_song)
        self.pause_btn.place(x=15, y=10)

        self.stop_btn = Button(self.button_frame, text='Stop', bg='Aqua', font=("Georgia", 13), width=7,
                               command=self.stop_song)
        self.stop_btn.place(x=105, y=10)

        self.play_btn = Button(self.button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=7,
                               command=self.play_song)
        self.play_btn.place(x=195, y=10)

        self.resume_btn = Button(self.button_frame, text='Resume', bg='Aqua', font=("Georgia", 13), width=7,
                                 command=self.resume_song)
        self.resume_btn.place(x=285, y=10)

        self.load_btn = Button(self.button_frame, text='Load Songs Folder' , bg='Aqua', font=("Georgia", 13), width=34,
                               command=self.load)
        self.load_btn.place(x=10, y=55)

        # Label at the bottom that displays the state of the music
        Label(self, textvariable=self.song_status, bg='SteelBlue', font=('Times', 9), justify=LEFT).pack(side=BOTTOM,
                                                                                                        fill=X)

    # Play, Stop, Load, Pause & Resume functions
    def play_song(self):
        self.current_song.set(self.playlist.get(ACTIVE))
        mixer.music.load(self.playlist.get(ACTIVE))
        mixer.music.play()
        self.song_status.set("Song PLAYING")

    def stop_song(self):
        mixer.music.stop()
        self.song_status.set("Song STOPPED")

    def load(self):
        os.chdir(filedialog.askdirectory(title='Open a songs directory'))
        tracks = os.listdir()
        for track in tracks:
            self.playlist.insert(END, track)

    def pause_song(self):
        mixer.music.pause()
        self.song_status.set("Song PAUSED")

    def resume_song(self):
        mixer.music.unpause()
        self.song_status.set("Song RESUMED")


# Creating an instance of the MusicPlayer class
if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()
