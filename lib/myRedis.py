import redis
import json


class MyRedis:
    def __init__(self, host, port, db_num, password):
        # инициализация - подключаемся к базе данных redis на локальном хосте
        self.redis_base = redis.StrictRedis(host=host, port=port, db=db_num, password=password)

    def set_dict(self, key, dictionary):
        # устанавливаем словарь-строку по ключу
        self.redis_base.set(key, str(dictionary))

    def get_dict(self, key):
        # получаем строку-словарь по ключу key и декодируем его в словарь питона
        result = self.redis_base.get(key)
        if result is not None:
            result = result.decode()
            result = json.loads(result.replace("'", '"'))
        return result

    def set(self, key, value):
        # установка ключа и значения
        self.redis_base.set(key, value)

    def get(self, key):
        # получение значения по ключу
        return self.redis_base.get(key)

    def scan_iter(self):
        # получение итератора
        return self.redis_base.scan_iter()

    def expire(self, key, timeout):
        # ключ key будет удален через timeout секунд
        self.redis_base.expire(key, timeout)

    def bgsave(self):
        # сохранить все данные в памяти на диск
        self.redis_base.bgsave()

    def delete(self, key):
        # ключ key и его значение будут удалены
        self.redis_base.delete(key)

    def flushdb(self):
        # очистить всю выбраную базу
        self.redis_base.flushdb()
