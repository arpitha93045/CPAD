import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from gtts import gTTS
import os
import pygame
import time
 
 
# Define a dictionary mapping text to image file paths
image_map = {
    "A": "C:/Assignment/VISEME/Lips/A_E_I.png",
    "B": "C:/Assignment/VISEME/Lips/B_M_P.png",
    "C": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "D": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "E": "C:/Assignment/VISEME/Lips/A_E_I.png",
    "F": "C:/Assignment/VISEME/Lips/F_V.png",
    "G": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "H": "C:/Assignment/VISEME/Lips/TH.png",
    "I": "C:/Assignment/VISEME/Lips/A_E_I.png",
    "J": "C:/Assignment/VISEME/Lips/CH_J_SH.png",
    "K": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "L": "C:/Assignment/VISEME/Lips/L.png",
    "M": "C:/Assignment/VISEME/Lips/B_M_P.png",
    "N": "C:/Assignment/VISEME/Lips/N.png",
    "O": "C:/Assignment/VISEME/Lips/O.png",
    "P": "C:/Assignment/VISEME/Lips/B_M_P.png",
    "Q": "C:/Assignment/VISEME/Lips/Q_W.png",
    "R": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "S": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "T": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "U": "C:/Assignment/VISEME/Lips/U.png",
    "V": "C:/Assignment/VISEME/Lips/F_V.png",
    "W": "C:/Assignment/VISEME/Lips/Q_W.png",
    "X": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "Y": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "Z": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "CH": "C:/Assignment/VISEME/Lips/CH_J_SH.png",
    "SH": "C:/Assignment/VISEME/Lips/CH_J_SH.png",
    "TH": "C:/Assignment/VISEME/Lips/TH.png",
    "a": "C:/Assignment/VISEME/Lips/A_E_I.png",
    "b": "C:/Assignment/VISEME/Lips/B_M_P.png",
    "c": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "d": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "e": "C:/Assignment/VISEME/Lips/A_E_I.png",
    "f": "C:/Assignment/VISEME/Lips/F_V.png",
    "g": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "h": "C:/Assignment/VISEME/Lips/TH.png",
    "i": "C:/Assignment/VISEME/Lips/A_E_I.png",
    "j": "C:/Assignment/VISEME/Lips/CH_J_SH.png",
    "k": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "l": "C:/Assignment/VISEME/Lips/L.png",
    "m": "C:/Assignment/VISEME/Lips/B_M_P.png",
    "n": "C:/Assignment/VISEME/Lips/N.png",
    "o": "C:/Assignment/VISEME/Lips/O.png",
    "p": "C:/Assignment/VISEME/Lips/B_M_P.png",
    "q": "C:/Assignment/VISEME/Lips/Q_W.png",
    "r": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "s": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "t": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "u": "C:/Assignment/VISEME/Lips/U.png",
    "v": "C:/Assignment/VISEME/Lips/F_V.png",
    "w": "C:/Assignment/VISEME/Lips/Q_W.png",
    "x": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "y": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "z": "C:/Assignment/VISEME/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "ch": "C:/Assignment/VISEME/Lips/CH_J_SH.png",
    "sh": "C:/Assignment/VISEME/Lips/CH_J_SH.png",
    "th": "C:/Assignment/VISEME/Lips/TH.png",
    "face": "C:/Assignment/VISEME/Lips/face.png"

}
 
 
# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))  # Correct the reference to __file__
audio_folder = os.path.join(script_dir, "Audio")
 
# Variable to store the last entered text
last_entered_text = ""
 
 
def speech_update():
    global last_entered_text
    text = text_entry.get()
 
    if text != last_entered_text:
        last_entered_text = text
 
        # Create the "Audio" folder if it doesn't exist
        try:
            if not os.path.exists(audio_folder):
                os.makedirs(audio_folder)
        except OSError as e:
            print(f"Error creating the 'Audio' folder: {e}")
 
        # Create a unique audio filename based on a timestamp
        timestamp = int(time.time())
        audio_filename = os.path.join(audio_folder, f"output_{timestamp}.mp3")
 
        # Create a gTTS object and save the text as audio
        try:
            tts = gTTS(text)
            tts.save(audio_filename)
        except Exception as e:
            print(f"Error creating audio: {e}")
 
 
def show_lips():
    text = text_entry.get()
    VISEME(text)
    play_audio()
 
 
def VISEME(text):
    # Remove any existing images
    image_label.pack_forget()
 
    # Split the text into individual letters
    letters = [letter for letter in text if letter in image_map]
 
    if letters:
        display_images(letters, 0)
 
 
def display_images(letters, index):
    if index < len(letters):
        letter = letters[index]
        image_path = image_map.get(letter)
        if image_path:
            try:
                face_path = image_map.get("face")
                face_image = Image.open(face_path).convert("RGBA")
                new_size = (300, 300)
                resized_face_image = face_image.resize(new_size)
                print(resized_face_image.mode)
                print(resized_face_image.info)
                # image_label1.config(image=face_photo)
                # image_label1.image = face_photo
                
                image = Image.open(image_path).convert("RGBA")
                new_size = (80, 35)
                resized_image = image.resize(new_size)
                print(resized_image.mode)
                print(resized_image.info)
                # photo = ImageTk.PhotoImage(resized_image)
                resized_face_image.paste(resized_image,(113,178),resized_image)
                face_photo = ImageTk.PhotoImage(resized_face_image)
 
                image_label.config(image=face_photo)
                image_label.image = face_photo
                # image_label1.pack()
                image_label.pack()
 
                # Schedule the next image after a delay (e.g., 500 milliseconds)
                app.after(100, display_images, letters, index + 1)
            except Exception as e:
                print(f"Error displaying image: {e}")
        else:
            print(f"Image not found for letter: {letter}")
 
    else:
        # Display the final image
        final_image_path = ""  # Replace with the path to your final image
        final_image = Image.open(final_image_path)
        new_size = (100, 100)
        resized_final_image = final_image.resize(new_size)
        final_photo = ImageTk.PhotoImage(resized_final_image)
 
        image_label.config(image=final_photo)
        image_label.image = final_photo
        image_label.pack()
 
 
def play_audio():
    speech_update()
    play_speech()
 
 
def play_speech():
    # List audio files in ascending order
    audio_files = sorted([f for f in os.listdir(audio_folder) if f.endswith(".mp3")])
 
    if audio_files:
        latest_audio_file = os.path.join(audio_folder, audio_files[-1])
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(latest_audio_file)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing audio: {e}")
 
 
# Create the main application window
app = tk.Tk()
app.title("Modern Image Viewer")
 
# Set the initial size of the window
app.geometry("600x400")  # Width x Height
 
# Use themed widgets (ttk)
style = ttk.Style()
style.configure('TButton', foreground='blue', padding=10)
style.configure('TLabel', foreground='green')
 
# Create a text input field
text_label = ttk.Label(app, text="Enter text:")
text_label.pack()
text_entry = ttk.Entry(app)
text_entry.pack()
 
# Bind the update_audio function to the <<FocusOut>> event
text_entry.bind("<FocusOut>", lambda e: speech_update())
 
# Create a label to display the image
image_label = ttk.Label(app)
 
# Create a button with updated style
speak_button = ttk.Button(app, text="Speak", command=show_lips, style='TButton')
speak_button.pack()
 
app.mainloop()