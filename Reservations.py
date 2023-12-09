from datetime import datetime
import csv
import json

class Reservations:
    def __init__(self):
        self.reservations = []
        self.reservations = self.info_reservations(action='load')
    
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
            'payment': False
        }
        if not self.show_availability(number, starttime, endtime):
            print("Chambre non disponible")
            return
        self.reservations.append(new_reservation)
        self.info_reservations(action='save', data= self.reservations)
        print(f"La reservation a été crée avec l'ID: {reservation_id}")      
        
    def save_payment(self, reservation_id):
        for reservation in self.reservations:
            if reservation['id']== reservation_id:
                reservation['payment'] = True
                self.info_reservations(action='save', data=self.reservations)
                print(f"Paiement enregistré pour {reservation_id}")
                return
            print(f"Reservation {reservation_id} not found")
        
    def show_availability(self, number, starttime, endtime):
        for reservation in self.reservations:
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
            
            reservation = next((r for r in self.reservations if r['id'] == reservation_id), None)
            if reservation:
                writer.writerow(reservation)
                print(f"Reervation with the ID {reservation_id} export to {filename}")
            else:
                print(f"Reservation with the ID {reservation_id} not found")
                
    def delete_reservations(self, reservation_id):
        reservation = next((r for r in self.reservations if r ['id']==reservation_id), None)
        if reservation:
            self.reservations.remove(reservation)
            self.info_reservations(action='save', data = self.reservations)
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
        reservation_id_to_export = int(input("Entrez l'ID de la réservation à exporter: "))
        filename = input("Entrez le nom du fichier pour l'export (par défaut: reservations.csv): ") or "reservations.csv"
        self.export(reservation_id_to_export, filename)
    
    def show_chambers(self):
        number = int(input("Enter the chamber number: "))
        starttime = input("Enter the start time (YYYY-MM-DD): ")
        endtime = input("Enter the end time (YYYY-MM-DD): ")

        available = self.show_availability(number, starttime, endtime)
        print("Chamber is available" if available else "Chamber is not available")
    
    def display_reservations(self):
        print("Liste des réservations:")
        for reservation in self.reservations:
            print(reservation)
                
    def delete_reservation(self):
        reservation_id = int(input("Entrez l'ID de la reservation à supprimer: "))
        self.delete_reservations(reservation_id)
