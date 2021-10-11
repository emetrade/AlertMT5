import MetaTrader5 as mt
import smtplib
import time

class GetTick():
#Класс "Входные данные" содержит методы получения и обработки данных для нейросети

    def __init__(self, dict_input_field_values):
               
        self.dict_input_field_values = dict_input_field_values

        self.ConnectToMT5()
        
        self.i = 1
        while self.i == 1:
            self.TickRetrieval()

        self.DisconnectToMT5()

    def ConnectToMT5(self):
        # Подключение к торговой платформе Мета Трейдер 5
        
        # установим подключение к терминалу MetaTrader 5
        if not mt.initialize():
            print("initialize() failed, error code =", mt.last_error())
            quit()
        # подключимся к торговому счету без указания пароля и сервера
        self.account=83690
        authorized=mt.login(self.account)  # пароль будет взят из базы терминала, если указано помнить данные для подключения
        if authorized:
            print("Подключились к аккаунту #{}".format(self.account))
        else:
            print("failed to connect at account #{}, error code: {}".format(self.account, mt.last_error()))

    def DisconnectToMT5(self):
        # завершим подключение к терминалу MetaTrader 5
        mt.shutdown()
        print ("Подключение к торговому счету {} в MetaTrader 5 завершено".format(self.account) )

    def sendmail(self, message):
    
        self.HOST = "smtp.mail.ru"
        self.SUBJECT = "AlertMT5"
        self.TO = "margo.hiq@mail.ru"
        self.FROM = "emetrade@mail.ru"
        self.text = message
        
        self.BODY = "\r\n".join((
            "From: %s" % self.FROM,
            "To: %s" % self.TO,
            "Subject: %s" % self.SUBJECT ,
            "",
            self.text
        ))
        
        server = smtplib.SMTP(self.HOST)
        server.starttls()
        server.login('emetrade@mail.ru', 'wM5wx8S0Va')
        server.sendmail(self.FROM, ["margo.hiq@mail.ru", 'emetrade@mail.ru' ], self.BODY)
        server.quit()

    def TickRetrieval(self):
        # получение последнего тика по указанному инструменту из терминала по параметрам
        # тикер
        # выведем последний тик по символу self.ticker

    
        # Запускаем цикл перебора словаря со значениями для каждого инструмента введённых уровней для отслеживания пересечения графиком цены
        for self.item in self.dict_input_field_values.items():

            # отсеиваем пустые значения словаря
            self.ticker = self.item[0]

            if self.ticker !="":
                stick = ["//---------------------------", "--------//---------------------","-----------------//----------", "----------------------//-" ]
                for a in stick:
                    time.sleep(0.5)
                    print(f"\r AlertMT5: {a}", end="", flush=True)
           
                # print ("AlertMT5: ", self.dict_input_field_values )
                # печатаем значение уровня для отслеживания из словаря
                # print(self.dict_input_field_values[self.ticker])
                # передаём значение уровня в переменную
                # запрашиваем данные из MT5 по последнему тику по данному инструменту в виде словаря
                self.symbol_info_tick_dict = mt.symbol_info_tick(self.ticker)._asdict()
                # передаём значение цены Ask из словаря в переменную
                self.ask_price = self.symbol_info_tick_dict['ask']
                # проверяем количество значений в списке принадлежащем данному элементу словаря
                
                print(f"\r AlertMT5: {self.ask_price}", end="", flush=True)

                




                if self.item[1][1] == 0:
                    # присваиваем значение текущей цены ask_price в стартовую цену start_ask_price
                    self.start_ask_price = self.ask_price
                    # модернизируем значения ключа перменными priceLevel и start_ask_price
                    self.item[1][1] = self.start_ask_price


                # производим проверку ЕСЛИ start_ask_price < priceLevel И ask_price > priceLevel ТО произошло пересечение снизу вверх
                if self.item[1][1] < self.item[1][0] and self.ask_price > self.item[1][0] and self.item[1][2].get() == True:
                    self.message = str(self.item[0]) + ": crossing the level: " + str(self.item[1][0]) + "  from bottom to top"
                    print("{self.item[0]}: произошло пересечение снизу вверх")
                    self.sendmail(self.message)
                    self.item[1][2].set(False)

                # производим проверку ЕСЛИ start_ask_price < priceLevel И ask_price > priceLevel ТО произошло пересечение снизу вверх
                elif self.item[1][1] > self.item[1][0] and self.ask_price < self.item[1][0] and self.item[1][2].get() == True:
                    self.message = str(self.item[0]) + ": crossing the level: " + str(self.item[1][0]) + " from top to bottom"
                    print("{self.item[0]}: произошло пересечение сверху вниз")
                    self.sendmail(self.message)
                    self.item[1][2].set(False)

                # print(self.start_ask_price)
                # print (self.dict_input_field_values)








