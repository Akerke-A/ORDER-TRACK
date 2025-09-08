import sender_stand_request
import data

# Функция для проверки позитивного сценария:
# если заказ существует (создан заранее), 
# то при запросе по его трек-номеру сервер вернёт код ответа 200 (успешно)
def positive_assert():                   
    # 1. Создаём новый заказ через POST-запрос
    #   - data.user_body содержит тело запроса (данные пользователя для заказа)
    order_response = sender_stand_request.post_new_order(data.user_body)

    # 2. Из ответа на создание заказа берём трек-номер
    #   - order_response.json() возвращает тело ответа в формате JSON 
    #   - ключ "track" содержит уникальный номер заказа
    track_number = order_response.json()["track"]

    # 3. Формируем параметры для GET-запроса по трек-номеру
    #   - API ожидает параметр с ключом "t"
    params = {
        "t": track_number
    }

    # 4. Делаем GET-запрос, чтобы получить заказ по его трек-номеру
    track_response = sender_stand_request.get_order_by_track(params)

    # 5. Проверяем, что сервер вернул статус-код 200
    #   - это значит, что заказ успешно найден
    assert track_response.status_code == 200


# Тест-кейс: проверка работы функции positive_assert
# Чек-лист: здесь можно будет добавить дополнительные тесты, например:
#   - Передача другого типа параметра (число вместо строки)
#   - Отправка пустого значения
#   - Запрос по несуществующему номеру
def test__get_order_by_track_number():
    positive_assert()