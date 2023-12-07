import json

class Chambers:
    def  __init__(self):
        self.chambers = []
        self.chambers = self.info_chambers(action='load')
        
    def add_chambers(self, number, type, price):
        #number = len(self.chambers) + 1
        new_chamber = {
            'number': number,
            'type': type,
            'price': price,
        }
        self.chambers.append(new_chamber)
        self.info_chambers(action='save', data=self.chambers)
        print(f"Une nouvelle chambre à été créée: {number}")
        
    def delete_chambers(self, number):
        for chamber in self.chambers:
            if chamber['number']== number: 
                self.chambers.remove(chamber)
                self.info_chambers(action='save', data=self.chambers)
                print(f"La chambre {number} à été supprimée")
                return
            print(f"Chambre {number} non trouvée")
            
    def update_chambers(self, number, update_data):
        for chamber in self.chambers:
            if chamber['number']==number:
                chamber.update(update_data)
                self.info_chambers(action='save', data=self.chambers)
                print(f"Chambre {number} mise à jour")
                return
            print(f"Chambre {number} non trouvée") 
    
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
            print(f"Numéro: {chamber['number']}, Type: {chamber['type']}, Prix par nuit: {chamber['price']}")
