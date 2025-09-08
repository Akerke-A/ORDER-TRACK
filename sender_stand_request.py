import requests
import configuration
import data


# Запрос на создание нового заказа
def post_new_order(user_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, 
        json=user_body
    )

# Получить заказ по его номеру
def get_order_by_track(track_number):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
        params=track_number
    )