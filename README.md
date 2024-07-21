# hit_bot - скрипт для Telegram
## Скрипт для телеграм бота созданный для того, чтобы прописать смачный чеполах собеседнику во время переписки.


## Запуск на машине
### Для того чтобы загрузить иходники:
```bash
git clone https://github.com/Sperankij/hit_bot.git
```

### Устанавливаем зависимости:
```bash
pip install -r requirements.txt
```

### Настройка API ключа:
Здесь заменяем `api_key` на API ключ, который получили у `@BotFather` при создании бота.
```bash
touch .env | echo "TELEGRAM_BOT_API_KEY=api_key" >> .env
```

### Запускаем бота:
```bash
python3 main.py
```

## Как пользоваться
### Добавление в группу:
Бота нужно добавить в группу как администратора с правами на удаления сообщений (это нужно для удаления сообщения с командой /hit).

### Команда `/hit`
Команда `/hit` принимет параметр \<имя>\ (имя нужно писать в дательном падеже).
Пример использования:
```
/hit загрязнению окружающей среды
```
Бот удалит это сообщение и заместо него напишет: `Черный Bластелин прописал смачный чеполах загрязнению окружающей среды` если Вас завут Черный Властелин, кончено же.

