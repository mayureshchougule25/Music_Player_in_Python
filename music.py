import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")

        self.playlist = []
        self.current_index = 0

        pygame.init()
        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.playlist_box = tk.Listbox(self.frame, selectmode=tk.SINGLE, bg="black", fg="white", selectbackground="blue")
        self.playlist_box.pack(fill=tk.BOTH, expand=True)

        add_button = ttk.Button(self.frame, text="Add Songs", command=self.add_songs)
        add_button.pack()

        play_button = ttk.Button(self.frame, text="Play", command=self.play)
        play_button.pack()

        pause_button = ttk.Button(self.frame, text="Pause", command=self.pause)
        pause_button.pack()

        stop_button = ttk.Button(self.frame, text="Stop", command=self.stop)
        stop_button.pack()

        self.volume_label = ttk.Label(self.frame, text="Volume")
        self.volume_label.pack()

        self.volume_scale = ttk.Scale(self.frame, from_=0, to=1, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_songs(self):
        files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
        for file in files:
            self.playlist.append(file)
            self.playlist_box.insert(tk.END, os.path.basename(file))

    def play(self):
        if self.playlist:
            current_song = self.playlist[self.current_index]
            pygame.mixer.music.load(current_song)
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))

    def on_closing(self):
        pygame.mixer.music.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
