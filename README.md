# bot_docker
### Это телеграм бот
Он создан, чтобы переводить из кириллицы в латиницу.

Перевод осуществляется в соответствии с [Приказом МИД по транслитерации](http://www.consultant.ru/document/cons_doc_LAW_360580/9eb761ae644ec1e283b3a50ef232330b924577cb/). 

Чтобы запустить бот через докер, нужно:
- скачать [докер](https://docs.docker.com/desktop/install/mac-install/)
- в терминале ввести: `$ docker build .`

- затем: `$ docker run -d -p 80:80 imageID`

*imageID* можно получить командой `docker images`.
