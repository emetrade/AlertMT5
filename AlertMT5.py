import threading
import WindowInterface1
import GetTick
from threading import *
from tkinter import *
import time

# Пробуем GitHub

def make_window():

    def Main_Window():
            # Создаём главное окно программы
        
            # Создаём окно программы
            window = Tk()

            # Задаём цвет фона главного окна
            window ["bg"] = "black"

            # Задаём размер окна с помощью .geometry
            window.geometry("800x600")
            window.title("Ввод данных для загрузки торговых данных по инструменту")           
            
            # Возвращаем после выполнения функции ссылку window на объект tk.Tk() 
            # именно это поможет зациклить (зафиксировать окно tk.Tk()) с помощью метода mainloop() 
            return (window)
    
    root = Main_Window() 

    wi1 = WindowInterface1.WindowInterface(root)

    root.mainloop()

thread1 = Thread(target= make_window)

thread1.start()


while WindowInterface1.var == False:
    # time.sleep(3)
    # print ("var == False")
    if WindowInterface1.var == True:
        time.sleep(3)
        
        print ("var == True")

        thread2 = Thread(target= GetTick.GetTick(WindowInterface1.dict_input_field_values), name= "intersection_search" )
        # thread2.name("intersection_search")
        thread2.start()
        # WindowInterface1.var = False

        print (WindowInterface1.var)

        print (threading.enumerate())



