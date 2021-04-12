Реализация приложения, которое будет сканировать директорию на предмет появление новых файлов. 
* При появлении нового файла необходимо вывести в лог имя файла, его расширение и дату создания. 
* После необходимо запустить в новом потоке его обработку, выбор обработчика осуществляется в зависимости от расширения. 
* Обработчик должен вывести в лог о времени начала обработки и общее время обработки файла. 
* Если файл по расширению не подходит под допустимый, необходимо запустить 
обработчик, который удалил бы данный файл.

Допустимы два расширения файлов: xml, json.
В качестве имитации обработки необходимо вывести в лог количество строк в файле.
Логирование должно осуществляться в файл на диске.