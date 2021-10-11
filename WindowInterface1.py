from tkinter import *
import numpy as np
from tempfile import TemporaryFile

var = False
dict_input_field_values ={}

class WindowInterface():
    # Главное окно программы

    def __init__(self, window):

        self.stop = False
        
        self.window = window

        # self.outfile = 'save.npy'

        self.cycle_filling_fields()

        self.create_button()
     
    def create_label_entry (self, label_for_field):
        # Создаём наименование поля ввода
        self.label_for_field = label_for_field
        self.label_name = Label(
                self.window,  # родительское окно
                text = label_for_field,
                foreground="white",  # Устанавливает белый текст
                background="black"  # Устанавливает черный фон
                                )
        return (self.label_name)

    def create_field_entry(self):
        # Создаём поле ввода данных
        self.entry_field = Entry(
                self.window,  # родительское окно
                width = 20,   # ширина поля ввода
                foreground="white",  # Устанавливает белый текст
                background="gray22"  # Устанавливает черный фон

                                )
        return (self.entry_field)

    def create_flag(self, variable_flag):
        # создаём флаг
        
        self.cb = Checkbutton(self.window, text="Уведомлять", variable=variable_flag, foreground="white", background="black", selectcolor="grey", command= self.onClick_flag)

        # Включаем флаг по умолчанию
        # self.cb.select()
        return (self.cb)

    def onClick_flag(self):
        pass

    def create_button (self):
        # Создаём кнопку подтверждения введённых данных 
        # В command передаём метод output_data для передачи данных (из полей ввода) в классы (например NeuroData) для последующей обработки
        self.button_entry = Button(self.window, text = "Ввод", command = self.output_data)
        self.button_entry.place(relx=.5, rely=.5, anchor="c")
   
    def insert_default_value(self):
        # Установим значения по умолчанию для полей ввода
        pass

        # # Load
        
        # self.read_dictionary = np.load(self.outfile)

        # for self.item in self.read_dictionary.items():
        #     if self.item[0] !="":
        #         self.pole1.insert(0,self.item[0])
        #         self.pole2.insert(0,self.item[1][1])


    def cycle_filling_fields(self):
        # Цикл для заполнения полями ввода и подписями полей главного окна программы
    
        
        self.row1 = 1
        self.label0 = self.create_label_entry("                              ")
        self.label0.grid(row = self.row1, column = 1)

        # Создаём пустые списки для заполнения 
        self.list_field_entry1 = []
        self.list_field_entry2 = []
        self.list_flag = []

        self.quantity_tickers = list(range(0, 10))

        # Запускаем цикл заполнения окна полями и лэйблами к ним

        for self.quantity_ticker in  self.quantity_tickers:
                
                self.row1 += 1

                self.list_flag.append(BooleanVar())
                
                self.label0 = self.create_label_entry("                              ")    
                self.pole1 = self.create_field_entry()
                self.label1 = self.create_label_entry("Ticker")

                self.pole2 = self.create_field_entry()
                self.label2 = self.create_label_entry("Price")

                self.flag1 = self.create_flag(self.list_flag[self.quantity_ticker])

                # Установим значения по умолчанию для полей ввода
                self.insert_default_value()

                self.label0.grid(row = self.row1, column = 1, sticky="e")
                self.label1.grid(row = self.row1, column = 2, sticky="e")
                self.pole1.grid(row = self.row1, column = 3, sticky="e")

                self.label2.grid(row = self.row1, column = 4, sticky="e")
                self.pole2.grid(row = self.row1, column = 5, sticky="e")

                self.flag1.grid(row = self.row1, column = 6, sticky="e")

                self.list_field_entry1.append(self.pole1)
                self.list_field_entry2.append(self.pole2)
        
    def output_data (self):

        self.dict_input_field_values_for_save = {}

        for i in self.list_flag:
            print(i.get())

        for (a,b,c) in zip(self.list_field_entry1, self.list_field_entry2, self.list_flag ):

            if b.get()!="":
                dict_input_field_values [a.get()] = [float(b.get()), 0, c]

                self.dict_input_field_values_for_save [a.get()] = [float(b.get())]

        print(dict_input_field_values)

        for self.ticker in dict_input_field_values:

            print(self.ticker)

        

        # # Save
        
        # np.save(self.outfile, self.dict_input_field_values_for_save) 
        # print ("Новый массив весов создан и сохранён в файл: ", self.outfile)


        global var
        var = True


        
    
    


           

    

       







    






