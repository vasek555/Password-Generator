import tkinter as tk
from tkinter import filedialog
import random
import string
import pyperclip

# Определяем наборы символов, которые будут использоваться в пароле
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

# Объединение наборов символов в одну строку
characters = lowercase_letters + uppercase_letters + digits + punctuation

# Определение функции для генерации случайного пароля
def generate_password():
    # Получение длины пароля из поля ввода
    password_length = int(length_entry.get())

    # Сгенерируйте случайный пароль
    password = ''.join(random.choice(characters) for i in range(password_length))

    # Отображение сгенерированного пароля в текстовом поле
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    # Скопируйте сгенерированный пароль в буфер обмена
    pyperclip.copy(password)

# Определиение функции для сохранения сгенерированного пароля в текстовый файл
def save_password():
    # Получене сгенерированного пароля из текстового поля
    password = password_entry.get()

    # Откройте диалоговое окно для выбора места сохранения
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        # Сохраните пароль в выбранном файле
        with open(file_path, "w") as f:
            f.write(password)

# Определите функцию для копирования сгенерированного пароля в буфер обмена
def copy_password():
    # Получите сгенерированный пароль из текстового поля
    password = password_entry.get()

    # Копирование пароля в буфер обмена
    pyperclip.copy(password)
    
# Создание окна графического интерфейса
window = tk.Tk()
window.title("Генератор паролей")
window.geometry("400x300")

# Создание метки для длины пароля
length_label = tk.Label(window, text="Длина пароля:")
length_label.grid(row=0, column=0)

# Создание поля для ввода длины пароля.
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1)

# Создание кнопки для пользователя, чтобы сгенерировать пароль
generate_button = tk.Button(window, text="Сгенерировать пароль", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2)

# Создание кнопки, с помощью которой пользователь может скопировать сгенерированный пароль в буфер обмена
copy_button = tk.Button(window, text="Копирование в буфер обмена", command=copy_password)
copy_button.grid(row=2, column=0, columnspan=2)

# Создание кнопки, с помощью которой пользователь сможет сохранить сгенерированный пароль в текстовом файле
save_button = tk.Button(window, text="Сохраните пароль в файл txt", command=save_password)
save_button.grid(row=3, column=0, columnspan=2)

# Создание ярлыка для отображения сгенерированного пароля
password_label = tk.Label(window, text="Сгенерированный пароль:")
password_label.grid(row=4, column=0)

# Создание текстового поляЫ для отображения сгенерированного пароля
password_entry = tk.Entry(window, width=50)
password_entry.grid(row=4, column=1)

# Запустите цикл событий графического интерфейса
window.mainloop()