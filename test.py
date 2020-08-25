import time
import numpy as np
from time import sleep
import pyautogui as pg
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import subprocess
import os
import pytesseract
import re
import psutil
import sqlite3


# pg.click(1248, 11)
# sleep(5)
# c = pg.moveTo(1306, 55)
# pg.click(c)  # îòêðûâàåì áëîêèðàòîð äæàâû
# sleep(5)
# y = pg.moveTo(1240, 89)
# pg.click(y)
# sleep(35)
# pg.hotkey('ctrl', 'w')  # çàêðûòü âêëàäêó áðàóçåðà

# def SeeCapcha():
#     filename = 'Im.png'
#     x = 1
#     last_time = time.time()
#
#     while (True):
#         screen = np.array(ImageGrab.grab(bbox=(214, 395, 297, 458)))
#         #print('loop took {} seconds'.format(time.time() - last_time))
#         last_time = time.time()
#         #cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
#         cv2.imwrite(filename, screen)
#         x = x + 1
#         # print(x)
#         # if x == 2:
#         #     cv2.destroyAllWindows()
#         #     break
#
#     img = cv2.imread('Im.png')
#     text = pytesseract.image_to_string(img)
#     # print(text)
#
#     index = text.find("egor")
#     # print(index)
#
#     if index == -1:
#         print("ÒÀÊÎÃÎ ÑËÎÂÀ ÍÅÒÜ!!!")
#         # sleep(25)
#         #SeeYou()
#     else:
#         print("ß ÍÀØÅËÜ ÅÍÒÎ ÑËÎÂÎ!!!")
#         # # pg.hotkey('ctrl', 'w')  # çàêðûòü âêëàäêó áðàóçåðà
#         # sleep(5)
#         # c = pg.moveTo(1306, 55)
#         # pg.click(c)  # îòêðûâàåì áëîêèðàòîð äæàâû
#         # sleep(5)
#         # y = pg.moveTo(1240, 89)
#         # pg.click(y)
#         # sleep(35)
#         # pg.hotkey('ctrl', 'w')  # çàêðûòü âêëàäêó áðàóçåðà
#         # i = pg.moveTo(1248, 9)
#         # pg.click(i)  # ñâîðà÷èâàåì áðàóçåð


# SeeCapcha()
# filename = 'Im.png'
# x = 1
# last_time = time.time()
#
# while (True):
#
#     screen = np.array(ImageGrab.grab(bbox=(214, 395, 294, 489)))
#         #print('loop took {} seconds'.format(time.time() - last_time))
#     last_time = time.time()
#     # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
#     cv2.imwrite(filename, screen)
#     x = x + 1
#     # print(x)
#     # if x == 2:
#     #     cv2.destroyAllWindows()
#     #     break
#
#     img = cv2.imread('Im.png')
#     text = pytesseract.image_to_string(img)
#     print(text)
#
#     index = text.find("egor")
#     # print(index)
#
#     if index == -1:
#         print("ÒÀÊÎÃÎ ÑËÎÂÀ ÍÅÒÜ!!!")
#         # sleep(25)
#         #SeeYou()
#     else:
#         print("ß ÍÀØÅËÜ ÅÍÒÎ ÑËÎÂÎ!!!")

# while True:
#     filename = 'Im.png'
#     x = 1
#     last_time = time.time()
#
#     while True:
#
#         screen = np.array(ImageGrab.grab(bbox=(600, 662, 666, 695)))
#         # print('loop took {} seconds'.format(time.time() - last_time))
#         last_time = time.time()
#         # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
#         cv2.imwrite(filename, screen)
#         x = x + 1
#         # print(x)
#         # if x == 2:
#         #     cv2.destroyAllWindows()
#         #     break
#
#         img = cv2.imread('Im.png')
#         text = pytesseract.image_to_string(img)
#         print(text)
#
#         index = text.find("Python")
#         # print(index)
#
#         if index == -1:
#             print("ÒÀÊÎÃÎ ÑËÎÂÀ ÍÅÒÜ!!!")
#             # sleep(25)
#             # SeeYou()
#         else:
#             print("ß ÍÀØÅËÜ ÅÍÒÎ ÑËÎÂÎ!!!")

def SeeYou():
    filename = 'Image1.png'
    x = 1
    last_time = time.time()

    while (True):
        screen = np.array(ImageGrab.grab(bbox=(485, 221, 881, 450)))
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite(filename, screen)
        x = x + 1
        print(x)
        if x == 2:
            cv2.destroyAllWindows()
            break

    img = cv2.imread('Image1.png')
    text = pytesseract.image_to_string(img)
    # print(text)

    index = text.find("reCAPTCHA")
    # print(index)

    if index == -1:
        print("ÒÀÊÎÃÎ ÑËÎÂÀ ÍÅÒÜ!!!")
        MyLp()

        # sleep(25)
        # pg.hotkey('ctrl', 'w')  # çàêðûòü âêëàäêó áðàóçåðà
        # c = pg.moveTo(1248, 9)
        # pg.click(c)  # ñâîðà÷èâàåì áðàóçåð
        # SeeTelegram()
    else:
        print("ß ÍÀØÅËÜ ÅÍÒÎ ÑËÎÂÎ!!!")
        Brauser()
        # pg.hotkey('ctrl', 'w')  # çàêðûòü âêëàäêó áðàóçåðà
        # c = pg.moveTo(1248, 9)
        # pg.click(c)  # ñâîðà÷èâàåì áðàóçåð
        sleep(3)
        q = pg.moveTo(639, 649)
        pg.click(q)  # æìåì ïðîïóñòèòü
        sleep(5)
        q = pg.moveTo(1292, 558, 0.5)
        pg.click(q)  # ñâîðà÷èâàåì ìåíþ
        # pg.click(e)


def SeeYou2():
    filename = 'Image1.png'
    x = 1
    last_time = time.time()

    while (True):
        screen = np.array(ImageGrab.grab(bbox=(485, 221, 881, 450)))
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite(filename, screen)
        x = x + 1
        print(x)
        if x == 2:
            cv2.destroyAllWindows()
            break

    img = cv2.imread('Image1.png')
    text = pytesseract.image_to_string(img)
    # print(text)

    index = text.find("reCAPTCHA")
    # print(index)

    if index == -1:
        print("ÒÀÊÎÃÎ ÑËÎÂÀ ÍÅÒÜ!!!")
        MyLp()

        # sleep(25)
        # pg.hotkey('ctrl', 'w')  # çàêðûòü âêëàäêó áðàóçåðà
        # c = pg.moveTo(1248, 9)
        # pg.click(c)  # ñâîðà÷èâàåì áðàóçåð
        # SeeTelegram()
    else:
        print("ß ÍÀØÅËÜ ÅÍÒÎ ÑËÎÂÎ!!!")
        Brauser()
        # pg.hotkey('ctrl', 'w')  # çàêðûòü âêëàäêó áðàóçåðà
        # c = pg.moveTo(1248, 9)
        # pg.click(c)  # ñâîðà÷èâàåì áðàóçåð
        sleep(5)
        q = pg.moveTo(661, 631)
        pg.click(q)  # æìåì ïðîïóñòèòü
        sleep(5)
        q = pg.moveTo(1292, 558, 0.5)
        pg.click(q)  # ñâîðà÷èâàåì ìåíþ
        # pg.click(e)


def down():
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('down')


def SeeNewAvailable():
    filename = 'Image4.png'
    x = 1
    last_time = time.time()

    while (True):
        screen = np.array(ImageGrab.grab(bbox=(414, 551, 810, 668)))
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite(filename, screen)
        x = x + 1
        print(x)
        if x == 2:
            cv2.destroyAllWindows()
            break

    img = cv2.imread('Image4.png')
    text = pytesseract.image_to_string(img)
    # print(text)

    index = text.find("Sorry")
    # print(index)

    if index == -1:
        print("ß íå ÍÀØÅËÜ ÅÍÒÎ ÑËÎÂÎ!!!")


    else:
        print("ß ÍÀØÅËÜ ÅÍÒÎ ÑËÎÂÎ!!!")
        # exit()
    return index



def SeeJava():
    filename = 'Image.png'
    x = 1
    last_time = time.time()

    while (True):
        screen = np.array(ImageGrab.grab(bbox=(8, 91, 106, 125)))
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite(filename, screen)
        x = x + 1
        print(x)
        if x == 2:
            cv2.destroyAllWindows()
            break

    img = cv2.imread('Image.png')
    text = pytesseract.image_to_string(img)
    # print(text)

    index = text.find("Loading")
    # print(index)

    if index == -1:
        print("ÒÀÊÎÃÎ ÑËÎÂÀ ÍÅÒÜ!!!")
        # sleep(25)
        SeeYou()
    else:
        print("ß ÍÀØÅËÜ ÅÍÒÎ ÑËÎÂÎ!!!")
        # pg.hotkey('ctrl', 'w')  # çàêðûòü âêëàäêó áðàóçåðà
        sleep(5)
        c = pg.moveTo(1306, 55)
        pg.click(c)  # îòêðûâàåì áëîêèðàòîð äæàâû
        sleep(5)
        y = pg.moveTo(1240, 89)
        pg.click(y)
        sleep(7)
        SeeYou2()

        # sleep(40)
        # pg.hotkey('ctrl', 'w')  # çàêðûòü âêëàäêó áðàóçåðà
        # i = pg.moveTo(1248, 9)
        # pg.click(i)  # ñâîðà÷èâàåì áðàóçåð


def Brauser():
    pg.hotkey('ctrl', 'w')  # çàêðûòü âêëàäêó áðàóçåðà
    i = pg.moveTo(1248, 9)
    pg.click(i)  # ñâîðà÷èâàåì áðàóçåð


def MyLp():  # ñìîòðèò è èùåò ñîîáùåíèå î ïîëó÷åíèè ñðåäñòâ
    while True:
        filename = 'Im.png'
        x = 1
        last_time = time.time()

        while True:

            screen = np.array(ImageGrab.grab(bbox=(1115, 582, 1332, 603)))
            # print('loop took {} seconds'.format(time.time() - last_time))
            last_time = time.time()
            # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
            cv2.imwrite(filename, screen)
            x = x + 1
            # print(x)
            # if x == 2:
            #     cv2.destroyAllWindows()
            #     break

            img = cv2.imread('Im.png')
            text = pytesseract.image_to_string(img)
            print(text)

            index = text.find("earned")
            # print(index)

            if index != -1:
                print("ß   ÍÀØÅËÜ ÅÍÒÎ ÑËÎÂÎ!!!")
                sleep(5)
                Brauser()
                break
        break

        # else:
        #     print("ß ÍÀØÅËÜ ÅÍÒÎ ÑËÎÂÎ!!!")
        #     sleep(5)
        #     Brauser()

        # sleep(10)
        # a = pg.moveTo(1342, 13)
        # pg.click(a)


def AnalogMyLp():
    boom = 35
    while boom > 0:
        time.sleep(1)
        # print(boom)
        boom -= 1
    Brauser()

# i = 0
#
# while i < 11:
#
#     pg.click(1248, 11)
#     down()
#     SeeNewAvailable()
#     a = pg.moveTo(444, 600, 0.5)
#     pg.click(a)
#     b = pg.moveTo(777, 426, 0.6)
#     pg.click(b)
#
#     sleep(10)
#     SeeJava()
#     i += 1


# conn = sqlite3.connect('adr1.db')
# cur = conn.cursor()
#
# cur.execute("CREATE TABLE IF NOT EXISTS users(id INT, path TEXT);")
# conn.commit()
#
#
# # cur.execute("DELETE FROM users WHERE path='C:\\Windows.old\\Users\\old-corp\\AppData\\Roaming\\Telegram Desktop\\telegram2\\telegram.exe';")
# # conn.commit()
#
#
# cur.execute("SELECT * FROM users;")
# all_results = cur.fetchall()
# a = all_results[2][1]
# # print(all_results)
# print(a)
# os.startfile(a)


y = 0

while y < 3:

    conn = sqlite3.connect('adr1.db')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users(id INT, path TEXT);")
    conn.commit()
    cur.execute("SELECT * FROM users;")
    all_results = cur.fetchall()
    a = all_results[y][1]
    #subprocess.call(a)
    os.startfile(a)
    sleep(15)
    pg.typewrite(' LTC Click Bot\n', 0.5)
    pg.typewrite(' /visit\n', 0.5)
    n = pg.moveTo(1294, 556)
    pg.click(n)
    sleep(5)
    i = 0

    while i < 15:

        pg.click(1248, 11)
        down()
        SeeNewAvailable()
        rtr = SeeNewAvailable()
        if rtr != -1:
            print(rtr)
            break
        a = pg.moveTo(444, 600, 0.5)
        pg.click(a)
        b = pg.moveTo(777, 426, 0.6)
        pg.click(b)

        sleep(10)
        SeeJava()
        i += 1
    y += 1


