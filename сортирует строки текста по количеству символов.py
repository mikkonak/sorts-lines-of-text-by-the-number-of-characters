import tkinter as tk
from tkinter import filedialog, messagebox
import os

class TextSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Sorter")

        self.label = tk.Label(root, text="Выберите текстовый файл для сортировки строк по количеству символов")
        self.label.pack(pady=10)

        self.load_button = tk.Button(root, text="Загрузить файл", command=self.load_file)
        self.load_button.pack(pady=5)

        self.sort_button = tk.Button(root, text="Сохранить отсортированный файл", command=self.sort_and_save_file, state=tk.DISABLED)
        self.sort_button.pack(pady=5)

        self.text_data = None

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text_data = file.readlines()
            messagebox.showinfo("Файл загружен", "Файл успешно загружен!")
            self.sort_button.config(state=tk.NORMAL)

    def sort_and_save_file(self):
        if self.text_data:
            sorted_text = sorted(self.text_data, key=len)
            save_path = os.path.join(os.path.dirname(__file__), "sorted_text.txt")
            with open(save_path, 'w', encoding='utf-8') as file:
                file.writelines(sorted_text)
            messagebox.showinfo("Файл сохранен", f"Отсортированный файл сохранен как {save_path}")
        else:
            messagebox.showwarning("Ошибка", "Сначала загрузите файл!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextSorterApp(root)
    root.mainloop()
