from configparser import ConfigParser
from pyrogram import Client, filters

config = ConfigParser()

config.read('config.ini')

api_id = config.get('pyrogram', 'api_id')
api_hash = config.get('pyrogram', 'api_hash')

app = Client(name='my_account', api_id=api_id, api_hash=api_hash)
text = 'Норм)'
@app.on_message(filters=filters.web_page)
async def auto_answer(event, message):
        await app.send_message(chat_id=message.chat.id, text=text)


app.run()
