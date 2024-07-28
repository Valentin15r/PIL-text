from PIL import Image, ImageDraw, ImageFont
import os

ширина = 200
высота = 200
фон = (255, 255, 255) 
цвет_шрифта = (0, 0, 0) 
шаг_шрифта = 5
мин_размер_шрифта = 10
макс_размер_шрифта = 50

def draw_text_on_image(text, font_path, width=ширина, height=высота):
    font_size = макс_размер_шрифта
    while True:
        font = ImageFont.truetype(font_path, font_size)
        text_width = font.getlength(text)
        text_height = font.size
        if text_width <= width and text_height <= height:
            break
        font_size -= шаг_шрифта
        if font_size < мин_размер_шрифта:
            print("Ошибка: текст не помещается на изображении.")
            return

    image = Image.new('RGB', (width, height), фон)
    draw = ImageDraw.Draw(image)

    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.text((x, y), text, font=font, fill=цвет_шрифта)

    image.save('фото.png')

def get_font_path():
    шрифты = []
    for filename in os.listdir('шрифты'):
        if filename.endswith('.ttf') or filename.endswith('.otf'):
            шрифты.append(os.path.join('шрифты', filename))
    print("Доступные шрифты:")
    for i, шрифт in enumerate(шрифты):
        print(f"{i+1}. {os.path.basename(шрифт)}")
    while True:
        font_choice = input("Введите номер шрифта, который вы хотите использовать: ")
        try:
            font_choice = int(font_choice) - 1
            if font_choice < 0 or font_choice >= len(шрифты):
                print("Ошибка: нет файла с таким номером.")
            else:
                return шрифты[font_choice]
        except ValueError:
            print("Ошибка: неверный формат ввода.")

text = input("Введите текст: ")
font_path = get_font_path()
draw_text_on_image(text, font_path)