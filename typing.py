import tkinter as tk
from tkinter import scrolledtext, ttk
import pyautogui
import threading
import time
import keyboard

class AutoTypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Typing Tool")
        self.root.geometry("500x400")  # Ukuran lebih compact
        self.root.resizable(True, True)
        
        # Mengatur tema tampilan
        self.configure_styles()
        
        # Membuat jendela selalu tampil di atas aplikasi lain
        self.root.attributes("-topmost", True)
        
        # Variabel untuk mengontrol pengetikan
        self.is_typing = False
        self.delay_before_typing = tk.IntVar(value=3)
        self.typing_speed = tk.DoubleVar(value=0.001)
        self.batch_size = tk.IntVar(value=20)
        self.batch_delay = tk.DoubleVar(value=0.005)
        self.typing_method = tk.StringVar(value="batch")
        self.always_on_top = tk.BooleanVar(value=True)
        
        self.create_widgets()
        
    def configure_styles(self):
        # Konfigurasi style untuk tampilan yang lebih modern
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Segoe UI", 9))
        style.configure("TButton", font=("Segoe UI", 9))
        style.configure("TRadiobutton", background="#f0f0f0", font=("Segoe UI", 9))
        style.configure("TCheckbutton", background="#f0f0f0", font=("Segoe UI", 9))
        style.configure("TSpinbox", arrowsize=10)
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        
        # Custom style untuk notebook
        style.configure("TNotebook", background="#f0f0f0", tabmargin=0)
        style.configure("TNotebook.Tab", padding=[5, 2], font=("Segoe UI", 9))
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="5")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Notebook untuk tab
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Tab Editor
        editor_tab = ttk.Frame(self.notebook, padding=5)
        self.notebook.add(editor_tab, text="Editor")
        
        # Text editor dengan desain lebih compact
        editor_frame = ttk.Frame(editor_tab)
        editor_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(editor_frame, text="Teks untuk diketik:", style="Header.TLabel").pack(anchor=tk.W, pady=(0, 5))
        
        self.text_input = scrolledtext.ScrolledText(editor_frame, wrap=tk.WORD, width=60, height=10)
        self.text_input.pack(fill=tk.BOTH, expand=True)
        
        # Control frame di bawah editor
        control_frame = ttk.Frame(editor_tab)
        control_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Button frame 
        button_frame = ttk.Frame(control_frame)
        button_frame.pack(fill=tk.X)
        
        # Tombol-tombol dengan ikon dan warna modern
        self.start_button = tk.Button(button_frame, text="Mulai", 
                                      command=self.start_typing, 
                                      bg="#4CAF50", fg="white", 
                                      height=1, width=8)
        self.start_button.pack(side=tk.LEFT, padx=2)
        
        self.stop_button = tk.Button(button_frame, text="Stop", 
                                     command=self.stop_typing, 
                                     bg="#F44336", fg="white", 
                                     height=1, width=8, 
                                     state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=2)
        
        clear_button = tk.Button(button_frame, text="Bersihkan", 
                                 command=self.clear_text, 
                                 bg="#2196F3", fg="white", 
                                 height=1, width=8)
        clear_button.pack(side=tk.LEFT, padx=2)
        
        on_top_check = ttk.Checkbutton(button_frame, text="Always on Top", 
                                        variable=self.always_on_top, 
                                        command=self.toggle_always_on_top)
        on_top_check.pack(side=tk.RIGHT, padx=2)
        
        # Countdown label
        countdown_frame = ttk.Frame(control_frame)
        countdown_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Label(countdown_frame, text="Delay:").pack(side=tk.LEFT, padx=2)
        ttk.Spinbox(countdown_frame, from_=1, to=10, textvariable=self.delay_before_typing, 
                   width=3).pack(side=tk.LEFT, padx=2)
        ttk.Label(countdown_frame, text="detik").pack(side=tk.LEFT, padx=2)
        
        # Tab Pengaturan
        settings_tab = ttk.Frame(self.notebook, padding=5)
        self.notebook.add(settings_tab, text="Pengaturan")
        
        # Metode pengetikan frame
        method_frame = ttk.LabelFrame(settings_tab, text="Metode Pengetikan", padding=5)
        method_frame.pack(fill=tk.X, expand=False, pady=5)
        
        ttk.Radiobutton(method_frame, text="Karakter (lambat tapi stabil)", 
                       variable=self.typing_method, value="char").pack(anchor=tk.W, padx=5)
        ttk.Radiobutton(method_frame, text="Batch (cepat, sedikit buffer)", 
                       variable=self.typing_method, value="batch").pack(anchor=tk.W, padx=5)
        ttk.Radiobutton(method_frame, text="Keyboard API (sangat cepat)", 
                       variable=self.typing_method, value="keyboard").pack(anchor=tk.W, padx=5)
        
        # Settings grid
        settings_grid = ttk.Frame(settings_tab)
        settings_grid.pack(fill=tk.X, expand=False, pady=5)
        
        # Karakter settings
        char_frame = ttk.LabelFrame(settings_grid, text="Pengaturan Karakter", padding=5)
        char_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(char_frame, text="Delay per karakter:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Spinbox(char_frame, from_=0.0001, to=0.1, increment=0.001, 
                   textvariable=self.typing_speed, width=6).grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(char_frame, text="detik").grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
        
        # Batch settings
        batch_frame = ttk.LabelFrame(settings_grid, text="Pengaturan Batch", padding=5)
        batch_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(batch_frame, text="Ukuran batch:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Spinbox(batch_frame, from_=5, to=50, textvariable=self.batch_size, width=6).grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(batch_frame, text="karakter").grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(batch_frame, text="Delay antar batch:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Spinbox(batch_frame, from_=0.001, to=0.1, increment=0.001, 
                   textvariable=self.batch_delay, width=6).grid(row=1, column=1, padx=5, pady=2)
        ttk.Label(batch_frame, text="detik").grid(row=1, column=2, sticky=tk.W, padx=5, pady=2)
        
        # Status bar
        self.status_label = tk.Label(self.root, text="Siap untuk mengetik", 
                                   bd=1, relief=tk.SUNKEN, anchor=tk.W, 
                                   bg="#f0f0f0", font=("Segoe UI", 8))
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def toggle_always_on_top(self):
        self.root.attributes("-topmost", self.always_on_top.get())
    
    def start_typing(self):
        if not self.text_input.get("1.0", tk.END).strip():
            self.status_label.config(text="Error: Tidak ada teks untuk diketik!")
            return
        
        self.is_typing = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        # Memulai thread terpisah untuk pengetikan
        typing_thread = threading.Thread(target=self.perform_typing)
        typing_thread.daemon = True
        typing_thread.start()
    
    def perform_typing(self):
        text_to_type = self.text_input.get("1.0", tk.END)
        delay = self.delay_before_typing.get()
        
        self.status_label.config(text=f"Siapkan kursor - mulai dalam {delay} detik...")
        
        # Countdown
        for i in range(delay, 0, -1):
            if not self.is_typing:
                return
            self.status_label.config(text=f"Mulai mengetik dalam {i} detik...")
            time.sleep(1)
        
        self.status_label.config(text="Sedang mengetik...")
        
        # Pilih metode pengetikan
        method = self.typing_method.get()
        
        if method == "char":
            self.type_char_by_char(text_to_type)
        elif method == "batch":
            self.type_by_batch(text_to_type)
        elif method == "keyboard":
            self.type_with_keyboard_api(text_to_type)
        
        if self.is_typing:  # Hanya update status jika tidak dihentikan
            self.is_typing = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_label.config(text="Pengetikan selesai!")
    
    def type_char_by_char(self, text):
        """Mengetik karakter satu persatu"""
        for char in text:
            if not self.is_typing:
                return
            
            pyautogui.write(char)
            time.sleep(self.typing_speed.get())
    
    def type_by_batch(self, text):
        """Mengetik dalam batch untuk mengurangi lag"""
        chars = list(text)
        batch_size = self.batch_size.get()
        
        # Bagi teks menjadi batch-batch
        for i in range(0, len(chars), batch_size):
            if not self.is_typing:
                return
                
            # Ambil batch karakter
            batch = ''.join(chars[i:i+batch_size])
            
            # Ketik batch
            pyautogui.write(batch)
            
            # Delay antar batch
            time.sleep(self.batch_delay.get())
    
    def type_with_keyboard_api(self, text):
        """Mengetik menggunakan library keyboard yang lebih cepat"""
        for char in text:
            if not self.is_typing:
                return
            
            keyboard.write(char)
            # Hampir tidak ada delay, sangat cepat
    
    def stop_typing(self):
        self.is_typing = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Pengetikan dihentikan!")
    
    def clear_text(self):
        self.text_input.delete("1.0", tk.END)
        self.status_label.config(text="Teks dibersihkan")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoTypingApp(root)
    root.mainloop()