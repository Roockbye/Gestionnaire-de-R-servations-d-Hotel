from datetime import datetime
import json


class Clients:
    def __init__(self):
        self.clients = []
        self.clients = self.info_clients(action='load')
    
    def add_clients(self, firstname, lastname, birthdate, phonenumber):
        client_id = len(self.clients) + 1
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
        new_client = {
            'client_id': client_id,
            'firstname': firstname,
            'lastname': lastname,
            'birthdate': birthdate.strftime('%Y-%m-%d'),
            'phonenumber': phonenumber,
        }
        self.clients.append(new_client)
        self.info_clients(action='save', data=self.clients)
        print(f"Un nouveau client à été créé: client {client_id}")
        
        
    def delete_clients(self, client_id):
        client_id = int(client_id)
        for client in self.clients:
            if client['id'] == client_id:
                self.clients.remove(client)
                self.info_clients(action='save', data=self.clients)
                print(f"Le client {client_id} à été supprimé:")
                return
            
        print(f"Client {client_id} non trouvé")
        
    def update_clients(self, client_id, update_data):
        client_id = int(client_id)
        for client in self.clients:
            client_id_in_dict = client.get('client_id')
            if client_id_in_dict is not None and client_id_in_dict == client_id:
            #if client['id'] == client_id:
                client.update(update_data)
                self.info_clients(action='save', data=self.clients)
                print(f"Données du client {client_id} mis à jour")
                return
            
        print(f"Client {client_id} non trouvé")
        

    def info_clients(self, action='load', data=None):
        filename = 'clients.json'
        if action == 'load':
            try:
                with open(filename, 'r') as file:
                    clients_data = json.load(file)
                    if not clients_data:
                        return[]
                    return clients_data
            except FileNotFoundError:
                return[]
        elif action=='save':
            with open(filename, 'w')as file:
                json.dump(data, file, indent=2)
                
    def display_clients(self):
        for client in self.clients:
            print(client)
            
##pour affiche main

    def add_client(self):
        firstname = input("Enter the first name: ")
        lastname = input("Enter the last name: ")
        birthdate = input("Enter the birthdate (YYYY-MM-DD): ")
        phonenumber = input("Enter the phone number: ")

        self.add_clients(firstname, lastname, birthdate, phonenumber)

    def delete_client(self):
        client_id = int(input("Enter the client ID to delete: "))
        self.delete_clients(client_id)

    def update_client(self):
        client_id = int(input("Enter the client ID to update: "))
        update_data = {
            'firstname': input("Enter the new first name: "),
            'lastname': input("Enter the new last name: "),
            'birthdate': input("Enter the new birthdate (YYYY-MM-DD): "),
            'phonenumber': input("Enter the new phone number: "),
        }
        self.update_clients(client_id, update_data)
