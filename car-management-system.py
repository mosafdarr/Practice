# Functional Documentation - is it remoneded to doument each function?
"""
    This function does XYZ.

    Parameters:
    - param1: Description of param1.
    - param2: Description of param2.

    Returns:
    Description of the return value.
"""

#Whole problem documentation - what is the best place to document this, above every thing? or below imports?

"""
Module/Script Name:

Brief description of the module or script and its purpose.

Problem Statement:

Brief description of the problem this code is solving. Include any context or scenario in which this code is intended to be used.

Requirements:
- Clearly list the requirements or functionalities that the codebase should fulfill.

Implementation Overview:
- Provide a high-level overview of how the code is structured and organized.
- Describe the major classes and their relationships.

Class 1:
- Brief description of Class 1 and its purpose.

Class 2:
- Brief description of Class 2 and its purpose.

...

Class N:
- Brief description of Class N and its purpose.

Usage:
- Provide an example of how to use the codebase.
- Include any important considerations or steps.

Example:
- Give an example use case or scenario to illustrate how the code addresses the problem.

Constraints:
- List any constraints or limitations associated with the code.

Assumptions:
- Enumerate any assumptions made in solving the problem.

Notes:
- Include any additional notes or considerations related to the code.

"""
from abc import ABC, abstractmethod


class CarFactory:
    robot_name = "Rb1.1"
    assembled_autos = []    # is it good practice to declare class static variable? or should we declare them outside our class?
    assembled_manuals = []

    def get_car(self, engine, car_type, info):
        engine_type = engine[0]
        engine_cc = engine[1]
        engine = Engine(engine_type, engine_cc)

        car_name = info[0]
        car_model = info[1]
        car_price = info[2]
        car_body = info[3]
        car_color = info[4]
        car_features = info[5]
        
        if car_type.lower() == "auto":
            car = Auto(car_name, car_model, car_price, car_body, car_color, car_features, engine)
            CarFactory.assembled_autos.append(car)
            return car
        
        if car_type.lower() == "manual":
            car = Manual(car_name, car_model, car_price, car_body, car_color, car_features, engine)
            CarFactory.assembled_manuals.append(car)
            return car

        return False
    
    @staticmethod
    def feature_specific(feature):
        cars = {
            "Autos": [],
            "Manuals": []
        }

        for car in CarFactory.assembled_autos:
            if feature in car.get_features():
                cars["Autos"].append(car)

        for car in CarFactory.assembled_manuals:
            if feature in car.get_features():
                cars["Manuals"].append(car)
        
        return car
    
    @staticmethod
    def showroom():
        auto_cars = [car.car_status() for car in CarFactory.assembled_autos]
        manual_cars = [car.car_status() for car in CarFactory.assembled_manuals]
        
        return auto_cars + manual_cars
    

class Car(ABC):
    def __init__(self, name, model, price, body_type, color):
        self.name = name
        self.model = model
        self.price = price
        self.body_type = body_type
        self.color = color

    @abstractmethod
    def current_status(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def shutdown_engine(self):
        pass


class Auto(Car):
    def __init__(self, name, model, price, body_type, color, features, engine):
        super().__init__(name, model, price, body_type, color)
        self.auto_engine = engine
        self.features = features

    def current_status(self):
        return self.auto_engine.get_engine_status()

    def start_engine(self):
        self.auto_engine.start_engine()

    def shutdown_engine(self):
        self.auto_engine.turn_off()
    
    def repaint(self, color):
        self.color = color

    def get_features(self):
        return self.features

    def car_status(self):
        return {
            "name": self.name,
            "model": self.model,
            "price": self.price,
            "body_type": self.body_type,
            "color": self.color,
            "Engine": self.auto_engine.engine_status(),
            "features": self.get_features(),
            "Status": "OFF" if self.current_status else "ON"
        }


class Manual(Car):
    def __init__(self, name, model, price, body_type, color, engine, features):
        super().__init__(name, model, price, body_type, color)
        self.manual_engine = engine
        self.features = features

    def current_status(self):
        return self.manual_engine.get_engine_status()

    def start_engine(self):
        self.manual_engine.start_engine()

    def shutdown_engine(self):
        self.manual_engine.turn_off()

    def car_status(self):
        return {
            "name": self.name,
            "model": self.model,
            "price": self.price,
            "body_type": self.body_type,
            "color": self.color,
            "Engine": self.auto_engine.engine_status(),
            "features": self.features(),
            "Status": "OFF" if self.current_status else "ON"
        }


class Engine:
    def __init__(self, engine_type, engine_cc):
        self.engine_type = engine_type
        self.engine_cc = engine_cc
        self.engine_state = False
        self.assembled = False

    def set_engine_type(self, engine_type):
        self.engine_type = engine_type
    
    def set_engine_cc(self, engine_cc):
        self.engine_cc = engine_cc

    def get_engine_cc(self):
        return self.engine_cc

    def get_engine_type(self):
        return self.engine_type

    def get_engine_status(self):
        return self.assembled

    def turn_on(self):
        if self.engine_state == True:
            return True
        
        self.engine_state = True
        return True
     
    def turn_off(self):
        if self.engine_state == False:
            return True
        
        self.engine_state = False
        return True
   
    def engine_status(self):
        return {
            "Horse Power": self.get_engine_cc(),
            "Engine type": self.get_engine_type(),
        }


def main():
    factory = CarFactory()

    info = ["BMW", "Dodge", 100000, "sedan", "Black", ["Cruise Control", "Heated Seats", "Self Driving"]]
    car = factory.get_car(["V1", 2500], "auto", info)
    
    print(CarFactory.get_all_cars())
        

main()
