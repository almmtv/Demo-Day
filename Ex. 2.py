import os
import datetime
import threading


# обработчик файлов с расширением .xml
# записывает время начала обработки и общее время, затраченное на обработку в файл log.txt
def xml_obr(xml_file):
    start = datetime.datetime.now()
    # имитация обработки файла
    count = 0
    with open(xml_file, 'r') as file:
        for line in file:
            count += 1
    delta = datetime.datetime.now() - start
    # блокировка других потоков
    t.acquire()
    with open('log.txt', 'a') as log_file:
        log_file.write(str(start) + ' ' + str(delta) + ' ' + str(count) + '\n')
    # снятие блокировки
    t.release()


# обработчик файлов с расширением .json
# записывает время начала обработки и общее время, затраченное на обработку в файл log.txt
def json_obr(json_file):
    start = datetime.datetime.now()
    count = 0
    with open(json_file, 'r') as file:
        for line in file:
            count += 1
    delta = datetime.datetime.now() - start
    t.acquire()
    with open('log.txt', 'a') as log_file:
        log_file.write(str(start) + ' ' + str(delta) + ' ' + str(count) + '\n')
    t.release()


# обработчик файлов с недопустимым расширением
# удаляет файлы
def something_else_obr(random_file):
    os.remove(random_file)


# функция остановки сканера
def stop():
    input('Введите любой символ для остановки программы: ')
    # ожидание остановки всех потоков
    while threading.active_count() > 2:
        continue


# считывание всего, что находится в текущей директории в момент начала работы программы
list_of_old_files = os.listdir()
# присвоение переменной t функции блокировки
t = threading.Lock()
# поток, контролирующий выключение сканера
t0 = threading.Thread(target=stop)
t0.start()
# запуск сканера
while t0.is_alive():
    # считывание того, что находится в директории
    list_of_new_files = os.listdir()
    # запуск цикла проверки для всех файлов
    for current_file in list_of_new_files:
        # проверка, является ли файл новым
        if current_file not in list_of_old_files and os.path.isfile(current_file):
            # запись имени файла, его расширения и даты создания в лог, если файл является новым
            filename, file_extension = os.path.splitext(current_file)
            date_of_creation_sec = os.stat(current_file).st_ctime
            date_of_creation = str(datetime.datetime.fromtimestamp(date_of_creation_sec))
            with open('log.txt', 'a') as log:
                log.write(filename + ' ' + file_extension + ' ' + date_of_creation + '\n')
            # в зависимости от расширения задаётся обработчик для нового потока
            if file_extension == '.xml' or file_extension == '.json':
                if file_extension == '.xml':
                    t1 = threading.Thread(target=xml_obr, args=(current_file, ))
                else:
                    t1 = threading.Thread(target=json_obr, args=(current_file, ))
            else:
                t1 = threading.Thread(target=something_else_obr, args=(current_file, ))
            # запуск нового потока
            t1.start()
    list_of_old_files = list_of_new_files
