import streamlit as st
from PIL import Image

# Зоголовок приложения
st.title("Пример приложения Streamlit")

# Текстовый блок
st.write("Это текстовый блок.")

# Кнопка
if st.button("Нажми меня"):
   st.write("Вы нажали кнопку!")


# Вывод изображения
image = Image.open("example_image.jpg") # замените "example_image.jpg" на свой путь к изображению
st.image(image, caption="Пример изображения", use_column_width=True)

# Вывод данных в таблице
import pandas as pd

data = {
        "Имя": ["Алиса", "Боб", "Карл"],
        "Возраст": [25, 30, 22],
}

df = pd.DataFrame(data)
st.write("Таблица данных:")
st.write(df)

