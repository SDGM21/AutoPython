import pathlib
import time
from os import path
import pyautogui
from get_table import exec_Table
#getting Data

if __name__ == '__main__':
    while True:
        navegatorToUse = pyautogui.confirm(text='Which navegator will you use?', title='Select Navegator', buttons=['Chrome', 'Edge', 'Opera', 'Mozilla']) # type: ignore
        if navegatorToUse != None:
            break
    while True:
        emailService = pyautogui.confirm(text='Which email service will you use?', title='Select Service', buttons=['Gmail', 'Outlook/Hotmail']) # type: ignore
        if type(emailService) != 'NoneType':
            break

    gastos, quantia, media = exec_Table (pathlib.Path('Login e Analisis/Compras.csv').absolute().__str__())

    #time for each execution
    pyautogui.PAUSE = 2.5
    pyautogui.press('win')
    pyautogui.write(navegatorToUse)
    pyautogui.press('enter')

    time.sleep(5)

    pyautogui.hotkey("ctrl", "t")
    if emailService == 'Gmail':
        pyautogui.write('https://mail.google.com/mail')
        pass
    elif emailService == 'Outlook/Hotmail':
        pyautogui.write('https://outlook.live.com/')
        pass

    pyautogui.press('enter')                                            
    time.sleep(10)
    pyautogui.leftClick(x=122, y=194)
    time.sleep(5)
    pyautogui.write("emailtest@mail.test")
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(5)
    pyautogui.write("TEST-RESUME")
    pyautogui.press('tab')
    time.sleep(5)
    pyautogui.write(f"""
    Gastos da Empresa: {gastos}
    Quantidade de items: {quantia}
    Media de gastos: {media}
    """)
    pyautogui.hotkey("ctrl",'enter')
pass