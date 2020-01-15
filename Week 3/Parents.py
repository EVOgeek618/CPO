import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    def get_photo_file_ext(self):
        print(os.path.splitext(self.photo_file_name))

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand,photo_file_name,carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_length, self.body_width, self.body_height = tuple(body_whl.split("x"))
    def get_body_volume(self):
        return float(self.body_length)*float(self.body_width)*float(self.body_height)

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row[0]=="car":
                car=Car(row[1],row[3],row[5],row[2])
            elif row[0]=="track":
                car=Car(row[1],row[3],row[5],row[4])
            elif row[0]=="spec_machine":
                car=Car(row[1],row[3],row[5],row[6])
            car_list.append(car)
     return car_list
    
