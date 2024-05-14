import os
import json
import requests
import tkinter as tk
from tkinter import ttk
import platform

try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
os = platform.system()

def simple_clean()
    if os == "Windows"
        path =
    if os == "Linux"
        path =
    if os == "Darwin"
        path =
root = tk.Tk()





ttk.label(root, text = 'Steam Cleaner').pack()
button = tk.Button(root, text +"Clean", command = clean)
root.mainloop()

