import sender_stand_request
import data

# Бодряков Дмитрий, 9-я когорта - Финальный проект. Инженер по тестированию плюс


# Тест 1.
def test_create_order_get_success_response():
    data_user_body = sender_stand_request.post_create_order().json


# Тест 2.
def test_order_info_get_track_number():
    track_number = sender_stand_request.get_order_info(data.user_body).json