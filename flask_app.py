from flask import Flask, request
import traceback
import json

import main
import utilities
import lib.repeater as repeater
import setup.settings as settings

app = Flask(__name__)

# ---------------------------------------------------------------------------------------------------------------------
# граб пост запросов с серверов ВК
# ---------------------------------------------------------------------------------------------------------------------


@app.route('/', methods=['POST'])
def processing():
    try:
        data = json.loads(request.data)
        if 'type' not in data.keys():
            return 'not vk'
        else:
            return main.response_handler(data)
    except json.decoder.JSONDecodeError:
        return 'ok'


# ---------------------------------------------------------------------------------------------------------------------
# граб ошибок и отправка их в лс админу
# ---------------------------------------------------------------------------------------------------------------------


@app.errorhandler(500)
def error_handler(e):
    # уведомляете админа об ошибке
    utilities.error_notificator(traceback.format_exc())
    # возвращаете ВК ok
    return 'ok'


# ---------------------------------------------------------------------------------------------------------------------
# бесконечная функция для подгрузки чего-либо
# ---------------------------------------------------------------------------------------------------------------------


repeater.RepeatTimer(settings.update_timer, utilities.notify).start()
