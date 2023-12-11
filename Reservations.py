from datetime import datetime
import csv
import json
from Chambers import Chambers

class Reservations:
    """
    A class to manage reservations in a hostel.

    Attributes:
    - reservations: a list to store reservation information.
    - chambers: an instance of the Chambers class.

    Methods:
    - __init__: initializes the Reservations class, loads reservation data from a file, and initializes the Chambers class.
    - make_reservations: creates a new reservation and saves the data to a file.
    - save_payment: saves the payment information for a reservation.
    - show_availability: checks the availability of chambers for a given time period.
    - export: exports reservation information to a CSV file.
    - delete_reservations: deletes a reservation from the list and updates the file.
    - info_reservations: loads or saves reservation data from/to a JSON file.
    - make_reservation: provides an interface to make a new reservation.
    - payment: provides an interface to save payment for a reservation.
    - export_reservations: provides an interface to export reservation information to a CSV file.
    - show_chambers: displays available chambers for a specified time period.
    - display_reservations: displays the details of all reservations.
    - delete_reservation: provides an interface to delete a reservation.
    """
    def __init__(self):
        self._reservations = []
        self._reservations = self.info_reservations(action='load')
        self._chambers = Chambers()
    
    def make_reservations(self, client_id, number,starttime, endtime, payment=False):
        reservation_id = len(self._reservations)+1
        starttime = datetime.strptime(starttime, '%Y-%m-%d').date() ## attention ne pas utiliser strftime ici
        endtime = datetime.strptime(endtime, '%Y-%m-%d').date()
        
        new_reservation = {
            'id': reservation_id,
            'client_id': client_id,
            'number': number,
            'starttime':starttime.strftime('%Y-%m-%d'),
            'endtime': endtime.strftime('%Y-%m-%d'),
            'payment': False
        }
        if not self.show_availability(number, starttime, endtime):
            print("Chamber not available")
            return
        self._reservations.append(new_reservation)
        self.info_reservations(action='save', data= self._reservations)
        print(f"The reservation has been created with the ID: {reservation_id}")      
        
    def save_payment(self, reservation_id):
        reservation = next((r for r in self._reservations if r['id'] == reservation_id), None)
        if reservation:
            reservation['payment'] = True
            self.info_reservations(action='save', data=self._reservations)
            print(f"Payment saved for {reservation_id}")
        else:
            print(f"Reservation {reservation_id} not found")
        
    def show_availability(self, number, starttime, endtime):
        for reservation in self._reservations:
            if reservation['number']==number:
                reservation_start = datetime.strptime(reservation['starttime'], '%Y-%m-%d').date()
                reservation_end = datetime.strptime(reservation['endtime'], '%Y-%m-%d').date()
                if starttime < reservation_end and endtime > reservation_start:
                    return False
        return True

        
    def export(self, reservation_id, filename='reservations.csv'):
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'client_id', 'number', 'starttime', 'endtime', 'payment']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            reservation = next((r for r in self._reservations if r['id'] == reservation_id), None)
            if reservation:
                writer.writerow(reservation)
                print(f"Reservation with the ID {reservation_id} export to {filename}")
            else:
                print(f"Reservation with the ID {reservation_id} not found")
                
    def delete_reservations(self, reservation_id):
        reservation = next((r for r in self._reservations if r ['id']== reservation_id), None)
        if reservation:
            self._reservations.remove(reservation)
            self.info_reservations(action='save', data = self._reservations)
            print(f"Reservation with ID {reservation_id} deleted")
        else:
            print(f"Reservation with ID {reservation_id} not found")
            
                
    def info_reservations(self, action='load', data=None):
        filename = 'reservation.json'
        if action == 'load':
            try:
                with open(filename, 'r') as file:
                    reservations_data = json.load(file)
                    if not reservations_data:
                        return[]
                    return reservations_data
            except FileNotFoundError:
                return[]
        elif action == 'save':
            with open(filename, 'w') as file:
                json.dump(data, file, indent=2)
    
    def display_reservations(self):
        print("List of reservations:")
        for reservation in self._reservations:
            print(reservation)
            
    def get_reservations(self):
        return self._reservations
                

## Display Interface(main)

    def make_reservation(self):
        print("Hello ! ")
        client_id = int(input("Enter the client ID: "))
        number = int(input("Enter the chamber number: "))
        starttime = input("Enter the start time (YYYY-MM-DD): ")
        endtime = input("Enter the end time (YYYY-MM-DD): ")

        self.make_reservations(client_id, number, starttime, endtime)

    def payment(self):
        reservation_id = int(input("Enter the reservation ID to save payment: "))
        self.save_payment(reservation_id)
    
    def export_reservations(self):
        reservation_id_to_export = int(input("Enter the ID of the reservation to export: "))
        filename = input("Enter the name of the file to export(by default: reservations.csv): ") or "reservations.csv"
        self.export(reservation_id_to_export, filename)
    
    def show_chambers(self):
        starttime = input("Enter the start date (YYYY-MM-DD): ")
        endtime = input("Enter the end date (YYYY-MM-DD): ")

        available_chambers = [chamber for chamber in self._chambers.list_chambers() if self.show_availability(chamber['number'], starttime, endtime)]
        if not available_chambers:
            print("No available chambers for the specified dates")
        else:
            print("Available Chambers:")
            for chamber in available_chambers:
                print(f"Chamber {chamber['number']}, {chamber['type']}, Price: {chamber['price']}")
                
    def delete_reservation(self):
        reservation_id = int(input("Enter the ID of the reservation to delete: "))
        self.delete_reservations(reservation_id)