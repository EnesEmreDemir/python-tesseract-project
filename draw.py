import win32api
from win32api import GetSystemMetrics
import win32con
import pygame
import win32gui
import pyautogui
import array
from PIL import Image
import cv2


def startDraw():
    pygame.init()
    n, m = array.array('i', (0,)*2000), array.array('i', (0,)*2000)
    screen = pygame.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(
        1)), pygame.FULLSCREEN, pygame.NOFRAME)  # For borderless, use pygame.NOFRAME
    done = False
    fuchsia = (255, 0, 128)  # Transparency color
    dark_red = (139, 0, 0)
    green = (127, 255, 0)

    # Set window transparency color
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(
        hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

    # Some controls
    block = 0
    block1 = 0

    # You can render some text
    white = (255, 255, 255)
    blue = (0, 0, 255)
    font = pygame.font.Font('freesansbold.ttf', 32)
    texto = font.render(
        'Press "z" to define one corner and again to define the rectangle, it will take a screenshot', True, white, dark_red)
    while not done:

        keys = pygame.key.get_pressed()
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # This controls the actions at starting and end point
        if block1 == 0:
            if keys[pygame.K_z]:
                if block == 0:
                    block = 1
                    n = win32gui.GetCursorPos()
                else:
                    done = True
                    break
                # this prevents double checks, can be handle also by using events
                block1 = 10

            else:
                m = win32gui.GetCursorPos()
        else:
            block1 -= 1

        screen.fill(fuchsia)  # Transparent background
        # this will render some text
        screen.blit(texto, (0, 0))
        # This will draw your rectangle
        if block == 1:
            pygame.draw.line(screen, green, (n[0], n[1]), (m[0], n[1]), 1)
            pygame.draw.line(screen, green, (n[0], m[1]), (m[0], m[1]), 1)
            pygame.draw.line(screen, green, (n[0], n[1]), (n[0], m[1]), 1)
            pygame.draw.line(screen, green, (m[0], n[1]), (m[0], m[1]), 1)
            #    Drawing the independent lines is still a little faster than drawing a rectangle
            pygame.draw.rect(screen, green, (min(n[0], m[0]), min(
                n[1], m[1]), abs(m[0]-n[0]), abs(m[1]-n[1])), 1)
        pygame.display.update()

    pygame.display.quit()

    _image = pyautogui.screenshot(region=(min(n[0], m[0]), min(
        n[1], m[1]), abs(m[0]-n[0]), abs(m[1]-n[1])))

    _image.save("D:\Desktop\captcha1.png", dpi=(300, 300))

    __img = Image.open("D:\Desktop\captcha1.png").convert('LA')
    __img.save('greyscale.png')

    __image = cv2.imread("greyscale.png")
    rsz = cv2.resize(__image, None, fx=1, fy=1,
                     interpolation=cv2.INTER_CUBIC)

    cv2.imwrite("D:\Desktop\captcha2.png", rsz)

    return((min(n[0], m[0]), min(
        n[1], m[1]), abs(m[0]-n[0]), abs(m[1]-n[1])))
