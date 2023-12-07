from Clients import Clients
from Chambers import Chambers
from Reservations import Reservations

class InterfaceUtilisateur:
    def __init__(self):
        self.clients = Clients()
        self.chambers = Chambers()
        self.reservations = Reservations()
        
    def display_banner(self):
        print("---------------------------------")
        print("Welcome to the Millenium Hostel")
        print("---------------------------------")

    def users(self):
        print("Are you an employee or a visitor?")
        print("1. Employee")
        print("2. Visitor")

        choice = input("Select 1 for employee or 2 for visitor: ")

        match choice:
            case "1":
                self.employee()
            case "2":
                self.visitor()
            case _:
                print("Invalid choice. Please select 1 or 2.")
                
    def employee(self):
    
        while True:
            print("\nEmployee menu:")
            print("1. Display the clients list") #ok
            print("2. Display the chambers list") #ok
            print("3. Add a new client") #ok
            print("4. Update a client info") #ok
            print("5. Delete a client") #ok
            print("6. Make a reservation") #no
            print("7. Save a payment") #no
            print("8. Export the reservations") #no
            print("0. Quit")

            choice = input("Select an option: ")
            match choice:
                case "0":
                    break
                case "1":
                    self.clients.display_clients()
                case "2":
                    self.chambers.display_chambers()
                case "3":
                    self.clients.add_client()
                case "4":
                    self.clients.update_client()
                case "5":
                    self.clients.delete_client()
                case "6":
                    self.reservations.make_reservations()
                case "7":
                    self.reservations.payment
                case "8":
                    self.reservations.export_reservations()
                case _:
                    print("Invalid option. Select a valid option.")

    def visitor(self):
        
        while True:
            print("\nVisitor menu:")
            print("1. Display the list of chambers available") #no
            print("0. Quit")

            choice = input("Select an option: ")

            match choice:
                case "0":
                    break
                case "1":
                    self.reservations.show_chambers()
                case _:
                    print("Invalid option. Select a valid option.")

    def run(self):
        self.display_banner()
        self.users()

if __name__ == "__main__":
    interface = InterfaceUtilisateur()
    interface.run()