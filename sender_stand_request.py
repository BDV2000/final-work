import configuration
import requests
import data



def post_create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_ORDERS,
                        json=data.user_body)


def get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER_PATH,
                        params={"t": track_number})