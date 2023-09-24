# main.py
import tkinter as tk
from virtual_keyboard import VirtualKeyboardApp

def main():
    root = tk.Tk()
    app = VirtualKeyboardApp(root)  # Pass the master parameter here
    root.mainloop()

if __name__ == "__main__":
    main()
