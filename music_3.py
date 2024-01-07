import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self):
        self.file_paths = []
        self.current_song_index = 0

        pygame.init()
        pygame.mixer.init()

        self.window = tk.Tk()
        self.window.title("Music Player")
        self.window.configure(bg="#EEEEEE")
        self.window.geometry("400x200")

        self.create_buttons()

    def create_buttons(self):
        browse_button = tk.Button(self.window, text="Browse Folder", command=self.browse_folder)
        browse_button.grid(row=0, column=0, padx=10, pady=10)

        previous_button = tk.Button(self.window, text="Previous", command=self.play_previous_song)
        previous_button.grid(row=1, column=0, padx=10, pady=10)

        play_button = tk.Button(self.window, text="Play", command=self.play_music)
        play_button.grid(row=1, column=1, padx=10, pady=10)

        pause_button = tk.Button(self.window, text="Pause", command=self.pause_music)
        pause_button.grid(row=1, column=2, padx=10, pady=10)

        resume_button = tk.Button(self.window, text="Resume", command=self.resume_music)
        resume_button.grid(row=1, column=3, padx=10, pady=10)

        stop_button = tk.Button(self.window, text="Stop", command=self.stop_music)
        stop_button.grid(row=1, column=4, padx=10, pady=10)

        next_button = tk.Button(self.window, text="Next", command=self.play_next_song)
        next_button.grid(row=1, column=5, padx=10, pady=10)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.file_paths = self.get_mp3_files(folder_path)
            if self.file_paths:
                self.current_song_index = 0
                self.play_music()

    def get_mp3_files(self, folder_path):
        mp3_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".mp3"):
                    mp3_files.append(os.path.join(root, file))
        return mp3_files

    def play_music(self):
        pygame.mixer.music.load(self.file_paths[self.current_song_index])
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_next_song(self):
        self.current_song_index += 1
        if self.current_song_index >= len(self.file_paths):
            self.current_song_index = 0
        self.play_music()

    def play_previous_song(self):
        self.current_song_index -= 1
        if self.current_song_index < 0:
            self.current_song_index = len(self.file_paths) - 1
        self.play_music()

    def run(self):
        self.window.mainloop()
        pygame.quit()

if __name__ == "__main__":
    music_player = MusicPlayer()
    music_player.run()
