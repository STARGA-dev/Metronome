import tkinter as tk
from tkinter import ttk
import time
import threading
import pygame
import os

class Metronome:
    def __init__(self, root):
        try:
            self.root = root
            self.root.title("Metrónomo / Metronome")
            
            # Variable para el BPM (beats per minute)
            self.bpm = tk.IntVar(value=60)
            
            # Inicializar pygame mixer
            pygame.mixer.init()
            
            # Proporcionar la ruta absoluta al archivo de sonido
            script_dir = os.path.dirname(os.path.abspath(__file__))
            sound_file = os.path.join(script_dir, "click.wav")
            self.tick_sound = pygame.mixer.Sound(sound_file)
            
            # Título de la aplicación
            ttk.Label(root, text="Metrónomo / Metronome", font=("Helvetica", 16)).pack(pady=10)
            
            # Slider para ajustar el BPM
            ttk.Label(root, text="BPM:").pack()
            self.bpm_slider = ttk.Scale(root, from_=30, to=300, orient='horizontal', variable=self.bpm)
            self.bpm_slider.pack(padx=10, pady=10)
            
            # Etiqueta para mostrar el BPM actual
            self.bpm_label = ttk.Label(root, text=f"Current BPM: {self.bpm.get()}")
            self.bpm_label.pack(pady=5)
            
            # Botón de inicio
            self.start_button = ttk.Button(root, text="Start", command=self.start_metronome)
            self.start_button.pack(pady=5)
            
            # Botón de parada
            self.stop_button = ttk.Button(root, text="Stop", command=self.stop_metronome)
            self.stop_button.pack(pady=5)
            
            # Variable para controlar el estado del metrónomo
            self.running = False
            
            # Actualizar la etiqueta de BPM cuando cambie el slider
            self.bpm_slider.bind("<Motion>", self.update_bpm_label)
            self.bpm_slider.bind("<ButtonRelease-1>", self.update_bpm_label)
        except Exception as e:
            print(f"Error initializing Metronome: {e}")

    def update_bpm_label(self, event):
        self.bpm_label.config(text=f"Current BPM: {self.bpm.get()}")
    
    def start_metronome(self):
        # Método para iniciar el metrónomo
        self.running = True
        threading.Thread(target=self.run_metronome).start()
    
    def stop_metronome(self):
        # Método para detener el metrónomo
        self.running = False
    
    def run_metronome(self):
        try:
            # Método que controla el ritmo del metrónomo
            while self.running:
                # Calcula el intervalo de tiempo en segundos para el BPM actual
                interval = 60.0 / self.bpm.get()
                # Reproduce el sonido del metrónomo
                self.tick_sound.play()
                # Espera el intervalo calculado
                time.sleep(interval)
        except Exception as e:
            print(f"Error running Metronome: {e}")
            self.running = False

# Configuración de la ventana principal de Tkinter
if __name__ == "__main__":
    try:
        root = tk.Tk()
        metronome = Metronome(root)
        root.mainloop()
    except Exception as e:
        print(f"Error: {e}")
