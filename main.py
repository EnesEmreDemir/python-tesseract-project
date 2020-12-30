from interface import PyWindow
import PySimpleGUI as sg
import draw
import imgviewer
from pytesseract import image_to_string
from PIL import Image

window = PyWindow().window

while True:
    event, values = window.read()
    if event == '-EXIT-' or event == sg.WIN_CLOSED:
        break
    if event == "-CHECKFORCOORDINATES-":
        coordinates = draw.startDraw()
        window['-COORDINATE1-'].update(coordinates[0])
        window['-COORDINATE2-'].update(coordinates[1])
        window['-COORDINATEX-'].update(coordinates[2])
        window['-COORDINATEY-'].update(coordinates[3])
        window['-CAPTCHA-'].Update(
            data=imgviewer.get_img_data("D:\Desktop\captcha2.png", first=True))
        window['-DECODEDCAPTCHA-'].update(
            image_to_string(Image.open("D:\Desktop\captcha2.png"), lang="tur"))
        print(image_to_string(Image.open("D:\Desktop\captcha2.png"), lang="tur"))

window.close()
