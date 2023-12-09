from Clients import Clients
from Chambers import Chambers
from Reservations import Reservations

class InterfaceUtilisateur:
    """
    A class to represent the user interface for the Millenium Hostel management system.

    Attributes:
    clients (Clients): An instance of the Clients class.
    chambers (Chambers): An instance of the Chambers class.
    reservations (Reservations): An instance of the Reservations class.
    """
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
            print("1. Display the clients list") #OK
            print("2. Display the chambers list") #OK
            print("3. Display reservations") #OK
            print("4. Add a new client") #OK
            print("5. Update a client info") #OK
            print("6. Delete a client") #OK
            print("7. Add a new chamber") #OK
            print("8. Update a chamber") #OK
            print("9. Delete a chamber") #OK
            print("10. Make a reservation") #OK
            print("11. Save a payment") #OK
            print("12. Delete a reservation")#OK
            print("13. Export the reservations") #OK
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
                    self.reservations.display_reservations()
                case "4":
                    self.clients.add_client()
                case "5":
                    self.clients.update_client()
                case "6":
                    self.clients.delete_client()
                case "7":
                    self.chambers.add_chamber()
                case "8":
                    self.chambers.update_chamber()
                case "9":
                    self.chambers.delete_chamber()
                case "10":
                    self.reservations.make_reservation()
                case "11":
                    self.reservations.payment()
                case "12":
                    self.reservations.delete_reservation()
                case "13":
                    self.reservations.export_reservations()
                case _:
                    print("Invalid option. Select a valid option.")

    def visitor(self):
        
        while True:
            print("\nVisitor menu:")
            print("1. Display the list of chambers available") #NO
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