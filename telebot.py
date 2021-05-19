import telegram, json
import pprint
import os

bot = telegram.Bot(token=os.environ.get('TELEGRAM_TOTO_KEY'))

chat_id = os.environ.get('CHAT_ID')
group_chat_id = os.environ.get('TOTO_CHAT_ID')


def send_message(message):
    try:
        global bot, chat_id, group_chat_id
        # Get your chat id using these lines
        # updates = json.loads(bot.get_updates()[-1].to_json())
        # chat_id = updates['message']['chat']['id']
        # pprint.pprint(updates)
        # print(chat_id)
        bot.send_message(chat_id=group_chat_id, text=message, )

    except Exception as e:
        bot.send_message(chat_id=chat_id, text='Something went wrong... message:{}'.format(e))
        print(e)


def send_check_message(message):
    try:
        global bot, group_chat_id
        # Get your chat id using these lines
        updates = json.loads(bot.get_updates()[-1].to_json())
        chat_id = updates['message']['chat']['id']
        pprint.pprint(updates)
        print(chat_id)
        bot.send_message(chat_id=chat_id, text=message, )

    except Exception as e:
        bot.send_message(chat_id=chat_id, text='Something went wrong... message:{}'.format(e))
        print(e)


if __name__ == '__main__':
    send_check_message("HELLO WORLD")
