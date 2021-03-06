						Dimension Check
								автор Михаил Журавлёв


Программа "Dimension Check" создана для избавления от рутинной работы.
Она предназначена для удобного заполнения, быстрого генерирования и сохранения документов связанных с контролем измерений. 


3 режима работы:
	1) Главное окно:
		Заполнение документа "Контрольный Список Измерений" и его определение в соответствующую папку "Dimension Check"
	2) Split Scan окно:
		Обработка единого PDF файла отсканированных замеров, распределение каждого замера по "Dimension Check" папкам
		и соединение их с результатом из 1) режима работы в 2-х страничный PDF.
	3) Стыки по Спулам окно:
		Заполнение таблицы "Стыки по Спулам"


Требования к каждому режиму:
	Режим 1):
		- Шаблон Exel документа "Контрольный Список Измерений". По умолчанию: "repo/template_DimChecklist.xlsx"
		- Подпись в формате ".png". По умолчанию: "repo/DS signature blue.png"
		- Подключение к серверу CWT
	
	Режим 2):
		- Один файл ".pdf" отсканированных замеров (желательно горизонтально повёрнутый)
		- Тексковый файл ".txt" с упорядоченным списком идентификационных названий (типа CWT.MP21-77-10.01.00)
		  отсканированных замеров. По умолчанию этот список создаётся с названием "repo/successfully_generated_drawings.txt"
		  и пополняется при каждом успешном исходе 1) режима работы. Можно создать самому.
	
	Режим 3):
		- Тексковый файл ".txt" с упорядоченным списком идентификационных названий (типа CWT.MP21-77-10.01.00)
		  отсканированных замеров. По умолчанию этот список создаётся с названием "repo/successfully_generated_drawings.txt"
		  и пополняется при каждом успешном исходе 1) режима работы. Можно создать самому.

Сравнение 1) режима работы без и с программой:
	Без программы:
		1) Открыть шаблон Excel
		2) Вписать необходимые значения в разные ячейки Excel (некоторые значения вписываются повторно)
		3) Сохранить документ в формате ".xlsx" с соответствующем детали названием в соответствующую папку детали на сервере, типа:
			Z:\CWT Documents\2021\MP21-77 BP101_POX_CS\CWT.MP21-77-70\Dimension Check\
			При этом, нужно создать папку "\Dimension Check" в случае её отсутствия.
		4) Сконвертировать документ в формат ".pdf"
		5) Поставить подпись к замерам в документе (либо от руки, но быстрее электронную)
	Временные затраты: 1 страница - ~5 мин

	С программой:
		1) Выбрать папку проекта, типа
			Z:\CWT Documents\2021\MP21-77 BP101_POX_CS\
		2) Вписать необходимые значения (легко без использования мышки)
		3) Нажать на кнопку "Generate"
	Временные затраты: 1 страница - ~1 мин


Сравнение 2) режима работы без и с программой:
	Без программы:
		1) В случае если скан содержит множество замеров, "PDF" нужно разделить постранично.
		2) Одностраничный "PDF" соединить с соответствующим файлом "Контрольный Список Измерений" сгенерированным в режиме 1).
		3) Соответствующе назвать документ по названию детали и сохранить в соответствующую папку.
	Временные затраты: 40 страниц - ~30 мин труда

	С программой:
		1) Выбрать многостраничный скан замеров формата ".pdf"
		2) Выбрать соответствующий текстовый файл ".txt" с упорядоченным
		   списком идентификационных названий (типа CWT.MP21-77-10.01.00) в столбик
		3) Самостоятельно проверить файлы на соответствие, в случае неуверенности.
		4) Нажать и ждать.
	Временные затраты: 40 страниц - 2 мин 20 сек ожидания

Сравнение 3) режима работы без и с программой:
	Без программы:
		1) Открыть Excel документ в папке "Стыки по Спулам" с названием типа "MP21-77 BP101_POX_CS.xlsx"
		2) Заполнить столбики "Isometric" и "Date" для каждого обработанного замера
	Временные затраты: 30 строчек - ~10 мин труда

	С программой:
		1) Выбрать Excel документ в папке "Стыки по Спулам" с названием типа "MP21-77 BP101_POX_CS.xlsx"
		2) Выбрать автоматически сгенерированный (или в ручную созданный) текстовый файл ".txt" с упорядоченным
		   списком идентификационных названий (типа CWT.MP21-77-10.01.00) в столбик.
		3) Нажать кнопку и ждать
	Временные затраты: все строчки - ~1 секунда ожидания


Преимущества работы с программой:
	- За час работы можно обработать ~60 страниц, вместо ~15 традиционно. В учёт взят режим 1).
	- Нет необходимоти переключаться между окнами, вся работа ведётся в окне программы
	- Работа без мышки (в основном)
	- Список названий (типа CWT.MP21-77-10.01.00) обработанных документов сохраняются
	  в текстовый документ "successfully_generated_drawings.txt" в папке "repo/"
	- Режим 2) распределяет сканы по соответствующим папкам "Dimension Check" сам.
	- Режим 3) моментально заполняет таблицу "Cтыки по Cпулам"


Требования:
	- Excel
	- Подключение к серверу CWT
	- Разрешение антивирусу открывать Excel документы с сервера сразу в режиме редактирования.


Возможные проблемы:
	- Файлы Excel открываются в режиме чтения (read mode). Нажатие по кнопки в всплытой жёлкой строчке даёт разрешение
          редактировать файл. Чтобы обойти это, нужно дать антивирусу разрешение на открытие файла сразу в режиме чтения.
	- Может показаться, что программа зависла при нажатии на кнопку.
	  Она блокируется когда генерирует файлы и разблокируется по окончанию. Скорость также зависит от поключения к серверу.



source code: https://github.com/mixren/CW_Dimension_Check
github: @mixren
Version 1.0.0