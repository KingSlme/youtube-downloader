import customtkinter
from main_window import MainWindow
import ssl

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_stdlib_context
    root = customtkinter.CTk()
    main_window = MainWindow(root)
    root.mainloop()