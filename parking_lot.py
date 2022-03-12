import heapq
from collections import defaultdict, OrderedDict


class Car:
    def __init__(self, registration_number, color):
        self.registration_number = registration_number
        self.color = color

    def __str__(self):
        return "Car [registration_number=" + self.registration_number + ", color=" + self.color + "]"


class ParkingLot:
    def __init__(self, total_slots):
        self.registration_slot_mapping = dict()
        self.color_registration_mapping = defaultdict(list)
        self.slot_car_mapping = OrderedDict()
        self.available_parking_lots = []
        
        for i in range(1, total_slots + 1):
            heapq.heappush(self.available_parking_lots, i)

    def status(self):
        for slot, car in self.slot_car_mapping.items():
            print("Slot no: {} {}".format(slot, car))

    def get_nearest_slot(self):
        return heapq.heappop(self.available_parking_lots) if self.available_parking_lots else None

    def free_slot(self, slot_to_be_freed):
        found = None
        for registration_no, slot in self.registration_slot_mapping.items():
            if slot == slot_to_be_freed:
                found = registration_no

        
        if found:
            del self.registration_slot_mapping[found]
            car_to_leave = self.slot_car_mapping[slot_to_be_freed]
            self.color_registration_mapping[car_to_leave.color].remove(found)
            del self.slot_car_mapping[slot_to_be_freed]
            print("leave ", slot_to_be_freed)
        else:
            print("slot is not in use")

    def park_car(self, car):
        slot_no = self.get_nearest_slot()
        if slot_no is None:
            print("Sorry, parking lot is full")
            return
        self.slot_car_mapping[slot_no] = car
        self.registration_slot_mapping[car.registration_number] = slot_no
        self.color_registration_mapping[car.color].append(car.registration_number)

    
    def get_registration_nos_by_color(self, color):
        return self.color_registration_mapping[color]

    
    def get_slot_numbers_by_color(self, color):
        return [self.registration_slot_mapping[reg_no] for reg_no in self.color_registration_mapping[color]]
    def slot_number_for_registration_number(self, registration_number):
            slot_number = None
            if registration_number in self.registration_slot_mapping:
                slot_number = self.registration_slot_mapping[registration_number]
                print(slot_number)
                return slot_number
            else:
                print("Not found")
                return slot_number            