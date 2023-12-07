from datetime import datetime
import csv

class Reservations:
    def __init__(self):
        self.reservations = []
    
    def make_reservations(self, client_id, number,starttime, endtime, payment=False):
        reservation_id = len(self.reservations)+1
        starttime = datetime.strptime(starttime, '%Y-%m-%d').date()
        endtime = datetime.strptime(endtime, '%Y-%m-%d').date()
        
        new_reservation = {
            'id': reservation_id,
            'client_id': client_id,
            'number': number,
            'starttime':starttime.strftime('%Y-%m-%d'),
            'endtime': endtime.strftime('%Y-%m-%d'),
            'payment': payment
        }
        if not self.show_availability(number, starttime, endtime):
            print("Chambre non disponible")
            return
        self.reservations.append(new_reservation)
        print("La reservation a été crée")
        
        
    def save_payment(self, reservation_id):
        for reservation in self.reservations:
            if reservation['id']== reservation_id:
                reservation['payment'] = True
                print(f"Paiement enregistré pour {reservation_id}")
                return
            print("Paiement non accepté")
        
        
    def show_availability(self, number, starttime, endtime):
        for reservation in self.reservations:
            if reservation['number']==number:
                reservation_start = datetime.strptime(reservation['starttime'], '%Y-%m-%d').date()
                reservation_end = datetime.strptime(reservation['endtime'], '%Y-%m-%d').date()
                if starttime < reservation_end and endtime > reservation_start:
                    return False
                return True
        
    def export(self, starttime, endtime, filename='reservations.csv'):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'client_id', 'number', 'starttime', 'endtime', 'payment']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for reservation in self.reservations:
                reservation_start = datetime.strptime(reservation['start_time'], '%Y-%m-%d').date()
                reservation_end = datetime.strptime(reservation['end_time'], '%Y-%m-%d').date()
                
                if starttime <= reservation_start <= endtime or starttime <= reservation_end <= endtime:
                    writer.writerow(reservation)

        print(f"Réservations exportées vers {filename} pour la période du {starttime} au {endtime}")
        
## affiche interface

    def make_reservation(self):
        client_id = int(input("Enter the client ID: "))
        number = int(input("Enter the chamber number: "))
        starttime = input("Enter the start time (YYYY-MM-DD): ")
        endtime = input("Enter the end time (YYYY-MM-DD): ")

        self.make_reservations(client_id, number, starttime, endtime)

    def payment(self):
        reservation_id = int(input("Enter the reservation ID to save payment: "))
        self.save_payment(reservation_id)

    def export_reservations(self):
        starttime = input("Enter the start time (YYYY-MM-DD): ")
        endtime = input("Enter the end time (YYYY-MM-DD): ")
        filename = input("Enter the filename for export (default: reservations.csv): ") or "reservations.csv"

        self.export(starttime, endtime, filename)

    def show_chambers(self):
        number = int(input("Enter the chamber number: "))
        starttime = input("Enter the start time (YYYY-MM-DD): ")
        endtime = input("Enter the end time (YYYY-MM-DD): ")

        available = self.show_availability(number, starttime, endtime)
        print("Chamber is available" if available else "Chamber is not available")
