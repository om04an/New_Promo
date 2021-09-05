from PIL import Image, ImageDraw, ImageFont  # импорт библиотек.

im = Image.open('Null_voucher.jpg')  # импорт изображение.

new_promo = input("Введите промокод: ").upper()  # ввод нового значения промокода.

font = ImageFont.truetype('Montserrat-Bold.ttf', size=57)  # текстовые параметры нового промокода.
draw_text = ImageDraw.Draw(im)
draw_text.text(    # расположение текста на изображение
    (432, 1150),
    new_promo,
    font=font,
    fill='#0B0C1E'
)

im.save(new_promo + '_voucher.jpg')  # сохранение изображения с новым промокодом.
