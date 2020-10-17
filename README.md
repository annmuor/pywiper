# PyWiper
# Уничтожитель сообщений в telegram-группах
## Зачем
В последнее время в Интернете много всего пишут такого, что может быть интерпретировано согласно УК различных стран.
Данная утилита позволяет создавать безопасное пространство для диалога, так как все сообщения будут удалены после.
## Как работает
Администратор запускает утилиту, указывает ID чата и количество дней, за которые нужно удалить сообщения.
## Как лучше всего использовать
Запускать по расписанию в 00:00
# Установка
1. Сходить [сюда](https://my.telegram.org/apps) и получить ID и Secret для приложения
2. Установить [python3.6 и выше](https://www.python.org/downloads/)
3. Установить [pip для python 3.6](https://pip.pypa.io/en/stable/installing/)
4. Выполнить команду: ./pywiper.py
5. Следовать инструкции из приложения
# Использование
./pywiper.py -i <id из пункта 1> -s <hash из пункта 1> [-l|-w id [until days [since days]]|-e id]
## -l, --list
Показывает все ваши чаты ( группы и супергруппы ) в формате: ID   NAME
## -w, --wipe
Позволяет удалить сообщения по ID группы, полученном из команды *list*
Третий аргумент: ID группы
Четвертый аргумент ( опционально ): количество дней, которые нужно стереть. Считает от текущего момента.
## -e, --erase
Позволяет удалить **свои** сообщения из группы
Третий аргумент: ID группы

# Авторы
- Идея и реализация для [tg-cli](https://github.com/vysheng/tg) - @annmuor
- Python-реализация - @stenopolz
- PythonИзация - @random1st
