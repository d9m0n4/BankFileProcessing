import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class FileProcessor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Обработка реестра')
        self.window.minsize(width=300, height=100)
        self.create_button()

    def create_button(self):
        button = tk.Button(self.window, text='Выбрать файл', command=self.process_file)
        button.pack(pady=10)

    def process_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        with open(file_path, 'r') as file:
            lines = file.readlines()

        modified_lines = [line.replace('/', ';') for line in lines]

        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

        messagebox.showinfo('Готово', 'Файл успешно обработан')

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    file_processor = FileProcessor()
    file_processor.run()
