1. Активация env
   source ll_env/bin/activate (ll_env\Scripts\Activate для Win)
2. Деактивация env
   deactivate
3. Установка django
   pip install django
4. Создание проекта в django
   python django-admin.py startproject learning_log .
   Не забывайте про точку, иначе у вас могут возникнуть проблемы с конфигурацией при развертывании приложения. А если вы все же забыли, удалите 
   созданные файлы и папки (кроме ll_env) и снова выполните команду.
5. Создание баз данных
   python manage.py migrate
6. Запуск сервера
   python manage.py runserver
7. Генерация приложения learning_logs
   python manage.py startapp learning_logs
8. приказать Django изменить базу данных для хранения информации, относящейся к модели Topic
   python manage.py makemigrations learning_logs
9. Применить миграцию для внесения изменений в базу
   python manage.py migrate
10. Тестирование возможно в оболочке Jango.
   python manage.py shell