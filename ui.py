import tkinter as tk
from tkinter import filedialog
def select_file(self):
    file_path = filedialog.askopenfilename()
    if file_path:
        self.file_path = file_path
        self.label.config(text=f"Selected file: {file_path}")

class EncodeWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Encode Window")
        
        self.label = tk.Label(master, text="Select a file to encode:")
        self.label.pack(pady=10)

        self.button = tk.Button(master, text="Select File", command=lambda: select_file(self))
        self.button.pack(pady=5)
        
        self.button = tk.Button(master, text="Close", command=self.master.destroy)
        self.button.pack(pady=5)

    
class DecodeWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Decode Window")
        
        self.label = tk.Label(master, text="Select a file to decode:")
        self.label.pack(pady=10)

        self.button = tk.Button(master, text="Select File", command=lambda: select_file(self))
        self.button.pack(pady=5)

        self.button = tk.Button(master, text="Close", command=self.master.destroy)
        self.button.pack(pady=5)


class FileDialog:
    def __init__(self, master):
        self.master = master
        self.master.title("File Dialog Example")
        
        self.label = tk.Label(master, text="Select a option:")
        self.label.pack(pady=10)
        
        self.button = tk.Button(master, text="Encode", command=self.encode_window)
        self.button.pack(pady=5)

        self.button = tk.Button(master, text="Decode", command=self.decode_window)
        self.button.pack(pady=5)
        
        self.file_path = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.file_path, width=50)
        self.entry.pack(pady=10)
        
    def encode_window(self):
        encode_window = tk.Toplevel(self.master)
        EncodeWindow(encode_window)

    def decode_window(self):
        decode_window = tk.Toplevel(self.master)
        DecodeWindow(decode_window)

if __name__ == "__main__":
    root = tk.Tk()
    file_dialog = FileDialog(root)
    root.mainloop()