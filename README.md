# bot_docker
### Это телеграм бот
Он создан, чтобы переводить из кириллицы в латиницу

Чтобы запустить бот через докер, нужно:
- скачать [докер](https://docs.docker.com/desktop/install/mac-install/)
- в терминале ввести: 
    $ docker build .
- затем: 
    $ docker run -d -p 80:80 imageID
imageID можно получить командой docker images
