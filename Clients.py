from datetime import datetime
import json

class Clients:
    """
    A class to manage client information.

    Attributes:
    - clients (list): A list to store client information.

    Methods:
    - __init__: Initializes the Clients class and loads client information from a file.
    - add_clients: Adds a new client to the list and saves the updated information to a file.
    - delete_clients: Deletes a client from the list and saves the updated information to a file.
    - update_clients: Updates a client's information and saves the updated information to a file.
    - info_clients: Loads or saves client information to a file.
    - display_clients: Displays all clients in the list.
    - add_client: Interface method to add a new client.
    - delete_client: Interface method to delete a client.
    - update_client: Interface method to update a client's information.
    """
    def __init__(self):
        self._clients = []
        self._clients = self.info_clients(action='load')
    
    def add_clients(self, firstname, lastname, birthdate, phonenumber):
        client_id = len(self._clients) + 1
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
        new_client = {
            'client_id': client_id,
            'firstname': firstname,
            'lastname': lastname,
            'birthdate': birthdate.strftime('%Y-%m-%d'),
            'phonenumber': phonenumber,
        }
        self._clients.append(new_client)
        self.info_clients(action='save', data=self._clients)
        print(f"A new client has been created: client {client_id}")
        
        
    def delete_clients(self, client_id):
        client_id = int(client_id)
        for client in self._clients:
            if client['client_id'] == client_id:
                self._clients.remove(client)
                self.info_clients(action='save', data=self._clients)
                print(f"The client {client_id} has been deleted")
                return
            
        print(f"Client {client_id} not found")
        
    def update_clients(self, client_id, update_data):
        client_id = int(client_id)
        for client in self._clients:
            if client['client_id'] == client_id:
                for key, value in update_data.items():
                    if value != '':
                        client[key] = value
                self.info_clients(action='save', data=self._clients)
                print(f"Data of the client {client_id} updated")
                return
            
        print(f"Client {client_id} not found")
        

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
        for client in self._clients:
            print(client)
            
    def get_clients(self):
        return self._clients
            
## Display on the Interface(main)

    def add_client(self):
        print("Hello !")
        firstname = input("Enter the first name: ")
        lastname = input("Enter the last name: ")
        birthdate = input("Enter the birthdate (YYYY-MM-DD): ")
        phonenumber = input("Enter the phone number: ")

        self.add_clients(firstname, lastname, birthdate, phonenumber)

    def delete_client(self):
        client_id = int(input("Enter the client ID to delete: "))
        self.delete_clients(client_id)
        print("Bye bye")

    def update_client(self):
        client_id = int(input("Enter the client ID to update: "))
        update_data = {
            'firstname': input("Enter the new first name: "),
            'lastname': input("Enter the new last name: "),
            'birthdate': input("Enter the new birthdate (YYYY-MM-DD): "),
            'phonenumber': input("Enter the new phone number: "),
        }
        self.update_clients(client_id, update_data)
