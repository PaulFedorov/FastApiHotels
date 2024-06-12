# Импорт необходимых модулей и классов из FastAPI, typing и других библиотек
from fastapi import FastAPI, Query, Depends  # Query - для ограничения переменной, Depends - для внедрения зависимостей
from typing import Optional  # Для указания необязательных типов
from datetime import date  # Для работы с датами
from pydantic import BaseModel  # Для создания моделей данных

# Создание экземпляра FastAPI
app = FastAPI()

# Определение класса для аргументов поиска отелей
class HotelsSearchArgs:
    def __init__(
            self,
            location: str,  # Местоположение отеля
            date_from: date,  # Дата начала периода
            date_to: date,  # Дата конца периода
            has_spa: bool = None,  # Наличие спа (необязательный параметр)
            stars: int = Query(None, ge=1, le=5),  # Количество звезд от 1 до 5 (с использованием Query для ограничения)
    ):
            # Инициализация атрибутов класса
            self.location = location
            self.date_from = date_from
            self.date_to = date_to
            self.has_spa = has_spa
            self.stars = stars

# Определение маршрута для получения списка отелей
@app.get("/hotels")
def get_hotels(
        search_args: HotelsSearchArgs = Depends()  # Внедрение зависимостей с использованием Depends
):
    return search_args  # Возврат аргументов поиска

# Определение модели данных для бронирования
class SBooking(BaseModel):
    room_id: int  # Идентификатор комнаты
    date_from: date  # Дата начала бронирования
    date_to: date  # Дата окончания бронирования

# Определение маршрута для добавления бронирования
@app.post("/bookings")
def add_booking(booking: SBooking):
    pass  # Заглушка для функции, которая будет добавлять бронирование
