import vk

import setup.settings as settings
import lib.myVkbotClass as myVkbot
import utilities

# создание объекта класса VkMethods для работы со всеми нужными методами для вк
vk_methods = myVkbot.VkMethods(settings.token, settings.vk_api_version)


# -----------------------------------------------------------------------------------------------
# обработчик входящих запросов от ВК
# -----------------------------------------------------------------------------------------------


def response_handler(data):
    if data['type'] == 'confirmation':
        return settings.confirmation_token
    elif data['type'] == 'message_new' or data['type'] == 'message_edit':
        create_answer(data['object'])
    elif data['type'] == 'group_leave':
        utilities.checkunsub(data['object'])
    elif data['type'] == 'group_join':
        utilities.checksub(data['object'])

    # возвращаем ок для серверов вк
    return 'ok'


# ------------------------------------------------------------------------------------------------
# логика бота.
# ------------------------------------------------------------------------------------------------
# напоминалка, что есть что
# user_id = data['from_id'], text = data['text'], payload = json.loads(data['payload'])['command']
# ------------------------------------------------------------------------------------------------


# основная функция - формировальщик ответа пользователю
def create_answer(data):
    # автоответчик
    send_message(data['from_id'], data['text'])


# -----------------------------------------------------------------------------------------------
# функция отправки сообщений. связанна с функцией флудконтроля
# -----------------------------------------------------------------------------------------------


# функция отправки сообщений, нужна для того чтобы вести учет и уведомлять о предстоящей блокировке
def send_message(from_id, message='', keyboard=None, attachment=()):
    try:
        vk_methods.send_message(from_id, message, keyboard, attachment)
    # если пользователь нас заблокировал, уведомляем об этом админа
    except vk.exceptions.VkAPIError as e:
        # генерируем и отправляем админу сообщение о том что сообщение не было доставлено
        user = vk_methods.linked_user_name(from_id)
        utilities.error_notificator('Error %s\n\n%s %s mes=%s' % (str(e), user[0], user[1], message))
