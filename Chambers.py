import json

class Chambers:
    """
    A class to manage chambers in a hotel.

    Attributes:
    - chambers: a list to store chamber information.

    Methods:
    - __init__: initializes the Chambers class and loads chamber data from a file.
    - add_chambers: adds a new chamber to the list and saves the data to a file.
    - delete_chambers: deletes a chamber from the list and updates the file.
    - update_chambers: updates the information of a chamber and saves the changes to the file.
    - info_chambers: loads or saves chamber data from/to a JSON file.
    - display_chambers: displays the details of all chambers.
    - list_chambers: returns a list of chamber details.
    - add_chamber: provides an interface to add a new chamber.
    - delete_chamber: provides an interface to delete a chamber.
    - update_chamber: provides an interface to update chamber information.
    """
    def  __init__(self):
        self.chambers = []
        self.chambers = self.info_chambers(action='load')
        
    def add_chambers(self, number, type, price):
        new_chamber = {
            'number': number,
            'type': type,
            'price': price,
        }
        self.chambers.append(new_chamber)
        self.info_chambers(action='save', data=self.chambers)
        print(f"A new chamber has been created: {number}")
        
    def delete_chambers(self, number):
        number = str(number)
        for chamber in self.chambers:
            if chamber['number']== number: 
                self.chambers.remove(chamber)
                self.info_chambers(action='save', data=self.chambers)
                print(f"The chamber {number} has been deleted")
                return
        print(f"Chamber {number} not found")
            
    def update_chambers(self, number, update_data):
        number = str(number)
        for chamber in self.chambers:
            if chamber['number'] == number:
                chamber.update(update_data)
                self.info_chambers(action='save', data=self.chambers)
                print(f"Chamber {number} updated")
                return
        print(f"Chamber {number} not found") 
    
    def info_chambers(self, action='load', data=None):
        filename = 'chambers.json'
        if action == 'load':
            try:
                with open(filename, 'r') as file:
                    chambers_data = json.load(file)
                    if not chambers_data:
                        return []
                    return chambers_data
            except FileNotFoundError:
                return []
        elif action == 'save':
            with open(filename, 'w') as file:
                json.dump(data, file, indent=2)
                
    def display_chambers(self):
        for chamber in self.chambers:
            print(f"Number: {chamber['number']}, Type: {chamber['type']}, Price per night: {chamber['price']}")

    
    def list_chambers(self):
        details_chamber = []
        for chamber in self.chambers:
            details_chamber.append({
                'number': chamber['number'],
                'type': chamber['type'],
                'price': chamber['price']
            })
        return details_chamber
    
## Display Interface(main)

    def add_chamber(self):
        number = input("Enter the chamber number: ")
        type = input("Enter the chamber type(simple, double, suite): ")
        price = input("Enter the price per night: ")
        
        self.add_chambers(number, type, price)
        
    def delete_chamber(self):
        number = int(input("Enter the chamber number to delete: "))
        self.delete_chambers(number)
        
    def update_chamber(self):
        number = int(input("Enter the chamber number to update: "))
        update_data = {
            'type': input("Enter the new type: "),
            'price': input("Enter the new price: "),
        }
        self.update_chambers(number, update_data)