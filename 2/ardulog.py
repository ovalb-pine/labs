#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
# 

#Основной скрипт для считывания, визуализации и записи данных в файл

import logging
from time import localtime, strftime, time, sleep
from utility import *

import matplotlib.pyplot as plt
import statistics

def main(args):
	# Настраиваем порт при помощи функции config_port из utility.py
	arduino = config_port()
	t_start = time()
	if not arduino == None:
		# Если с портом все получилось, то просим имя выходного файла
		f_name = input('Введите имя выходного файла (default=\'data\'+timestamp): ')
		if f_name == '':
			# Если пользователь ничего не ввел, то даем файлу default-имя
			f_name='data'+make_timestamp()+'.txt'
		
		# Инициализируем переменные для построения графика
		fig = plt.figure()
		ax1 = fig.add_subplot(211)
		ax2 = fig.add_subplot(212)
		x, y = [], []
		n=range(0,14,1)
		logging.info(f'n={n}')
		# Сколько точек будет отображаться на графике
		# Если слишком много - все начнет тормозить
		maxlen = 150
		
		while True:
			# Пытаемся читать данные из порта в бесконечном цикле
			# Это не очень умно - хорошо бы читать данные только тогда, когда появляются новые
			# try-except блок, чтобы программа не падала по любому поводу
			try:
				# Этот вариант быстрее
				bytesToRead = arduino.inWaiting()
				line = arduino.read(bytesToRead).decode().strip()
				#Этот вариант медленнее
				#line = arduino.readline().decode().strip()
			except Exception:
				#Если что-то идет не так - ругаемся в консоли:)
				logging.exception(f'[main] Не получилось считать данные из порта')
				# И отправляемся в начало петли цикла
				continue
			if not line == '':
				# Если строка не пустая, то разбираем ее на список
				# числовых данных при помощи функции parse_data из utility.py
				new_data = parse_data(line)
				if not new_data == '':
					
					# Счетчик времени
					t = round(time()-t_start,2)
					# try-except блок, чтобы программа не падала по любому поводу
					try:
						#Пробуем добавить точку на график
						y.append(float(new_data[0]))
						x.append(t)
						y[-1] = statistics.mean(y[-3:])  # Сглаживание
						if len(x) > maxlen:
							del x[0]
							del y[0]
					
						ax1.clear()
						ax1.plot(x, y, 'o-', color='g', linewidth=1)
						ax2.clear()
						ax2.plot(n, new_data, 'o-', color='r', linewidth=1)

						fig.canvas.draw()
						fig.canvas.flush_events()
						plt.pause(0.05)
			
						# Здесь выводим данные в терминал
						logging.info(f"[main] time:{t}, data:{print_list(new_data,',')}")
						# И записываем их в файл
						with open(f_name, 'a') as fh:
							fh.write(f"{t}\t{print_list(new_data,'\t')}\n")
					except Exception:
						#Если что-то идет не так - ругаемся в консоли:)
						logging.exception(f'[main] Не удалось обработать данные')
				#Спим, если не нужно слишком много точек
			sleep(1)	
	return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
