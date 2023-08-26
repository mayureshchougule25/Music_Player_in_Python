# Music_Player_in_Python

The code creates a simple music player GUI using the Tkinter library in Python.
The MusicPlayer class is defined, initializing the GUI window and setting its dimensions.
It initializes a playlist to store song filenames and sets the current song index to 0.
Pygame library is used for audio playback, and both Pygame and Pygame.mixer are initialized.
The GUI widgets, including a listbox for the playlist, buttons for adding songs, playing, pausing, and stopping, and a volume scale, are created.
The add_songs method opens a file dialog to select MP3 files and adds their filenames to the playlist.
The play method loads and plays the current song from the playlist using Pygame.mixer.music.
The pause method pauses the playback using Pygame.mixer.music.pause().
The stop method stops the playback using Pygame.mixer.music.stop().
The set_volume method adjusts the playback volume using Pygame.mixer.music.set_volume().
The on_closing method stops the playback and closes the GUI window when the user closes the window.
In the main block, a Tkinter window is created, and an instance of the MusicPlayer class is created within it.
The main event loop is started using root.mainloop(), allowing the GUI to respond to user interactions.



