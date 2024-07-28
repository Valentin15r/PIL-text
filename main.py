from PIL import Image, ImageDraw, ImageFont
import os

def draw_text_on_image(text, font_path, width=200, height=200):
    font_size = 50
    while True:
        font = ImageFont.truetype(font_path, font_size)
        text_width = font.getlength(text)
        text_height = font.size
        if text_width <= width and text_height <= height:
            break
        font_size -= 5

    white_background = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(white_background)

    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.text((x, y), text, font=font, fill=(0, 0, 0))

    white_background.save('фото.png')

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