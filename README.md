# GPT3-Telegram-Chatbot
OpenAI chatbot for Telegram using GPT-3

To run telegram bot you have to:
1. Rename `sample.env` to `.env`
2. Fill all the requirement fields in `.env`, such as `TELEGRAM_KEY` etc.
      - `TELEGRAM_KEY` you can get from [@BotFather](https://t.me/BotFather)
      - To get `MAIN_USER_ID` etc Just Simply Forward a message from your group/channel to [@JsonDumpBot](https://t.me/JsonDumpBot) or [@getidsbot](https://t.me/getidsbot)
3. Build the docker image using `docker build -t bots/telegram .`
4. Run the docker image using `docker run -h telegram --name telegram -d bots/telegram`