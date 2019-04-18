import threading

import setup.settings as settings
import lib.myVkbotClass as myVkbot

# ---------------------------------------------------------------------------------------------------------------------
# инициализация классов для работы с вк и базой redis и хелпера
# ---------------------------------------------------------------------------------------------------------------------


vk_methods = myVkbot.VkMethods(settings.token, settings.vk_api_version)


# ---------------------------------------------------------------------------------------------------------------------
# Функции-утилиты
# ---------------------------------------------------------------------------------------------------------------------


# функция уведомляющая админа об ошибке
def error_notificator(error):
    if settings.error_receiver_id is not None:
        threading.Timer(1, vk_methods.send_message, args=[settings.error_receiver_id, error]).start()


# функция реагирующая на отписку
def checkunsub(data):
    pass


# функция реагирующая на подписку
def checksub(data):
    pass


# бесконечная функция
def notify():
    pass
