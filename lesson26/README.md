# Пример запуска для Windows:

1. Скачиваем десктопное приложение Docker, в настройках FileSharing прописываем путь к используемым дискам
Для команд в терминале используем ```$current = $PWD -replace "\\", "/" -replace "C", "c"```

2. Скачиваем бинарный файл селеноида, запускаем его из папки:
```
cd ~/Downloads
./cm_darwin_amd64 selenoid start 
./cm_darwin_amd64 selenoid-ui start
```

3. Проверяем появились ли изображения, запустились ли контейнеры
```
docker images
./cm_darwin_amd64 selenoid status
./cm_darwin_amd64 selenoid-ui status
```

4. Добавляем по необходимости нужные браузеры в файл .aerokube/selenoid/browsers.json
Или скачиваем нужные Images, браузеры при старте добавляются автоматически

5. Пререходим в директорию с файлом Dockerfile, собираем image с нашими тестами, проверяем наличие
```
cd ~\Python_qa_Engeneer\lesson26\tests
docker build -t tests .
docker images
```

6. Запуск тестов в докере с параметрами по умолчанию (по необходимости аргументы командной строки можно добавить)
```
docker run --rm tests
```

7. Для просмотра allure отчёта:
```
docker run --name my_run tests --browser chrome -n 2
docker cp my_run:/app/allure-report .
allure serve lesson26/allure-report
```