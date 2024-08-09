import subprocess
import webbrowser
import tkinter as tk
from PIL import Image, ImageTk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Hacking tv")
        self.geometry("1200x700")
        self.configure(bg='#1e1e1e')

        # Левое меню
        self.create_sidebar()

        # Верхняя панель с названием и поиском
        self.create_topbar()

        # Область с контентом
        self.create_content_area()

        # Открытие окна в развернутом режиме
        self.state('zoomed')

    def create_sidebar(self):
        sidebar = tk.Frame(self, bg='#2c2c2c', width=200, height=700)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Название в левом верхнем углу
        title_label = tk.Label(sidebar, text="Smart Hacking tv", bg='#2c2c2c', fg='white', font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=20, padx=10, anchor='w')

        # Привязываем метод menu к клику по title_label
        title_label.bind("<Button-1>", lambda event: self.menu())

        # Меню без границ
        menu_items = ["Zona", "YouTube", "ТВ-каналы", "Я.Музыка", "Погода", "Радио", "ChatGPT", "Уведомления", "Настройки", "О программе", "Убрать рекламу"]
        for item in menu_items:
            if item == "Zona":
                btn = tk.Button(sidebar, text=item, bg='#2c2c2c', fg='white', font=('Helvetica', 14), bd=0, anchor='w', highlightthickness=0, command=self.open_zona)
            elif item == "Убрать рекламу":
                btn = tk.Button(sidebar, text=item, bg='#2c2c2c', fg='orange', font=('Helvetica', 14), bd=0, anchor='w', highlightthickness=0, command=self.remove_ads)
            elif item == "О программе":
                btn = tk.Button(sidebar, text=item, bg='#2c2c2c', fg='white', font=('Helvetica', 14), bd=0, anchor='w', highlightthickness=0, command=self.programs)
            elif item == "YouTube":
                btn = tk.Button(sidebar, text=item, bg='#2c2c2c', fg='white', font=('Helvetica', 14), bd=0, anchor='w', highlightthickness=0, command=self.YouTube)
            else:
                btn = tk.Button(sidebar, text=item, bg='#2c2c2c', fg='white', font=('Helvetica', 14), bd=0, anchor='w', highlightthickness=0)
            btn.pack(fill=tk.X, pady=5, padx=10)

    def create_topbar(self):
        topbar = tk.Frame(self, bg='#1e1e1e', height=50)
        topbar.pack(side=tk.TOP, fill=tk.X)

        back_button = tk.Button(topbar, text="Назад", bg='#1e1e1e', fg='white', font=('Helvetica', 14), bd=0, highlightthickness=0)
        back_button.pack(side=tk.LEFT, padx=10)

        search_entry = tk.Entry(topbar, width=50, font=('Helvetica', 14), bg='#3c3c3c', fg='white', bd=0, highlightthickness=0)
        search_entry.pack(side=tk.LEFT, padx=10)

        user_label = tk.Label(topbar, text="тут будет ваш аккаунт", bg='#1e1e1e', fg='white', font=('Helvetica', 14))
        user_label.pack(side=tk.RIGHT, padx=10)

    def create_content_area(self):
        self.content_area = tk.Frame(self, bg='#1e1e1e')
        self.content_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Пример простого содержимого (замените этот код на ваше собственное содержимое)
        self.example_label = tk.Label(self.content_area, text="Добро пожаловать в Smart Hacking TV!", bg='#1e1e1e', fg='white', font=('Helvetica', 18))
        self.example_label.pack(pady=20)

    def open_zona(self):
        """Открыть файл zona.pyw"""
        subprocess.Popen(["python", "zona.pyw"])  

    def YouTube(self):
        """Открыть файл youtube.pyw"""
        subprocess.Popen(["python", "youtube.pyw"])

    def remove_ads(self):
        """Изменить текст на 'Рекламы нету :)'"""
        self.example_label.config(text="Рекламы нету :)")

    def programs(self):
        """Изменить текст на 'О программе'"""
        # Очистить предыдущие виджеты
        for widget in self.content_area.winfo_children():
            widget.destroy()

        # Добавляем текст с описанием
        description = tk.Label(self.content_area, text="Программа сделана, чтобы улучшить выходные :)\nVersion 1.0", bg='#1e1e1e', fg='white', font=('Helvetica', 18))
        description.pack(pady=10)

        # Добавляем кликабельную ссылку
        link = tk.Label(self.content_area, text="GitHub: https://github.com/Kostz98/Smart_Hacking_tv", bg='#1e1e1e', fg='blue', cursor="hand2", font=('Helvetica', 18, 'underline'))
        link.pack(pady=10)

        # Привязываем к ссылке открытие браузера
        link.bind("<Button-1>", lambda e: self.open_link("https://github.com/Kostz98/Smart_Hacking_tv"))

    def open_link(self, url):
        """Открыть ссылку в браузере"""
        webbrowser.open_new(url)

    def menu(self):
        """Изменить текст на 'Добро пожаловать в Smart Hacking TV!'"""
        self.example_label.config(text="Добро пожаловать в Smart Hacking TV!")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
