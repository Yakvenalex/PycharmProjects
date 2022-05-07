from pyrogram import Client
app = Client('account')

@app.on_message()
def echo(client, message):
    print(message)
app.run()