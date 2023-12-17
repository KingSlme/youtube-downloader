import customtkinter
import downloader

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.url_entry = None
        self.options_combobox = None
        self.progress_label = None
        self.result_label = None
        self.progress_bar = None
        self.create_main_window()

    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}") 

    def download_button_callback(self):
        self.root.focus_force()
        self.result_label.configure(text=f"{downloader.download_video(self.url_entry.get(), self.progress_bar_callback, self.options_combobox.get())}")

    def progress_bar_callback(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        self.progress_label.configure(text=str(int(percentage_of_completion)) + "%")
        self.progress_label.update()
        self.progress_bar.set(float(percentage_of_completion / 100))

    def create_main_window(self):
        # Main Window
        self.root.title("Youtube Downloader")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        MainWindow.center_window(self.root, 410, 220)
        self.root.resizable(width=False, height=False)
        # Frames
        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=10, padx=10, fill="both", expand=True)
        input_frame = customtkinter.CTkFrame(master=frame, bg_color=['gray92', 'gray14'], fg_color=['gray90', 'gray13'], corner_radius=0)
        input_frame.grid(row=0, column=0, pady=10)
        # Entry
        self.url_entry = customtkinter.CTkEntry(master=input_frame, width=300, height=40, placeholder_text="Please insert a valid Youtube video URL", font=customtkinter.CTkFont("Inter", 15)) # 350
        self.url_entry.grid(row=0, column=0, padx=(10, 5))
        # Combobox
        self.options_combobox = customtkinter.CTkComboBox(master=input_frame, width=65, height=28, values=["mp3", "mp4"], font=customtkinter.CTkFont("Inter", 12))
        self.options_combobox.grid(row=0, column=1, padx=(0, 5))
        # Button
        download_button = customtkinter.CTkButton(master=frame, width=100, height=40, text="Download", font=customtkinter.CTkFont("Inter", 20, weight="bold"), command=self.download_button_callback)
        download_button.grid(row=1, column=0, pady=(0, 10))
        # Labels
        self.progress_label = customtkinter.CTkLabel(master=frame, text="N/A", font=customtkinter.CTkFont("Inter", 20))
        self.progress_label.grid(row=2, column=0, pady=(0, 5))
        self.result_label = customtkinter.CTkLabel(master=frame, text="", font=customtkinter.CTkFont("Inter", 20))
        self.result_label.grid(row=5, column=0, pady=10)
        # Progress Bar
        self.progress_bar = customtkinter.CTkProgressBar(master=frame, width=360)
        self.progress_bar.set(0)
        self.progress_bar.grid(row=3, column=0)