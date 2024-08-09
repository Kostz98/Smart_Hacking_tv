import webview

def create_browser_window():
    # Создаем окно браузера
    window = webview.create_window(
        title='Smart Hacking tv',               # Заголовок окна
        url='https://w140.zona.plus/',          # URL для загрузки
        width=1255,                              # Ширина окна
        height=809,                             # Высота окна
        x=193,                                  # Позиция по оси X
        y=56,                                   # Позиция по оси Y
        resizable=True,                         # Возможность изменения размеров
        frameless=False                         # Окно с рамкой (если True, то без рамки)
    )
    
    # Запуск браузера
    webview.start(debug=False)  # Убедитесь, что debug=False

if __name__ == "__main__":
    create_browser_window()
