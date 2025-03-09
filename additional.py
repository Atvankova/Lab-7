import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk
import tempfile


def load_new_image():
    response = requests.get("https://randomfox.ca/floof/")
    data = response.json()
    image_url = data["image"]
    image_response = requests.get(image_url)
    image_data = Image.open(BytesIO(image_response.content))
    image_data = image_data.resize((300, 300), Image.Resampling.LANCZOS)
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
        image_data.save(tmp_file, format="PNG")
        tmp_file_path = tmp_file.name
    photo = tk.PhotoImage(file=tmp_file_path)
    image_label.config(image=photo)
    image_label.image = photo


window = tk.Tk()
window.geometry('500x500')
window.resizable(width=False, height=False)
window.title("Генератор картинок")


lbl_title = tk.Label(window, text='Генератор картинок', font=('Arial', 30), fg='black')
lbl_title.pack(pady=10)


image_label = tk.Label(window)
image_label.pack(pady=20)


btn_update = tk.Button(window, text='Обновить', command=load_new_image, font=('Arial', 16))
btn_update.pack(pady=10)


load_new_image()


window.mainloop()
