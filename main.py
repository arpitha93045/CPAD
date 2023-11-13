import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from gtts import gTTS
import os
import pygame
import time


# Define a dictionary mapping text to image file paths
image_map = {
    "A": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/A_E_I.png",
    "B": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/B_M_P.png",
    "C": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "D": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "E": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/A_E_I.png",
    "F": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/F_V.png",
    "G": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "H": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/TH.png",
    "I": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/A_E_I.png",
    "J": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/CH_J_SH.png",
    "K": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "L": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/L.png",
    "M": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/B_M_P.png",
    "N": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/N.png",
    "O": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/O.png",
    "P": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/B_M_P.png",
    "Q": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/Q_W.png",
    "R": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "S": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "T": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "U": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/U.png",
    "V": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/F_V.png",
    "W": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/Q_W.png",
    "X": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "Y": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "Z": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "CH": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/CH_J_SH.png",
    "SH": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/CH_J_SH.png",
    "TH": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/TH.png",
    "a": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/A_E_I.png",
    "b": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/B_M_P.png",
    "c": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "d": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "e": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/A_E_I.png",
    "f": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/F_V.png",
    "g": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "h": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/TH.png",
    "i": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/A_E_I.png",
    "j": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/CH_J_SH.png",
    "k": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "l": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/L.png",
    "m": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/B_M_P.png",
    "n": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/N.png",
    "o": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/O.png",
    "p": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/B_M_P.png",
    "q": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/Q_W.png",
    "r": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "s": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "t": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "u": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/U.png",
    "v": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/F_V.png",
    "w": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/Q_W.png",
    "x": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "y": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "z": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "ch": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/CH_J_SH.png",
    "sh": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/CH_J_SH.png",
    "th": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/TH.png",
    "face": "/Users/I527878/Documents/CPAD/project/lip_sync/Lips1/face.png"

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
    lip_sync(text)
    play_audio()


def lip_sync(text):
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
                resized_face_image.paste(resized_image,(113,177),resized_image)
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
