import random
import json
import os

CUSTOMER_FILE = "customers.json"

pricing = {
    'SUVs': {'base': 1500, 'per_km': 25},
    'Compact SUVs': {'base': 1200, 'per_km': 20},
    'Sedans': {'base': 1000, 'per_km': 15},
    'Hatchbacks': {'base': 800, 'per_km': 12},
    'Autos': {'base': 500, 'per_km': 10},
    'E-rickshaws': {'base': 400, 'per_km': 8},
    'Motorcycles': {'base': 600, 'per_km': 12},
    'Scooters': {'base': 300, 'per_km': 6}
}

vehicles = {
    'SUVs': ['Scorpio Classic', 'Scorpio N', 'Toyota Fortuner', 'Tata Safari', 'Toyota Hilux',
             'MG Gloster', 'Mahindra XUV700', 'Skoda Kodiaq', 'Jeep Meridian', 'Thar Roxx', 'Innova Crysta'],
    'Compact SUVs': ['Tata Nexon', 'Hyundai Venue', 'Maruti Brezza', 'Kia Sonet', 'Nissan Magnite',
                     'Maruti Fronx', 'Tata Punch', 'Maruti Grand Vitara', 'Honda WRV'],
    'Sedans': ['Honda City', 'Honda Civic', 'Hyundai Verna', 'Skoda Slavia', 'Volkswagen Virtus',
               'Maruti Ciaz', 'Skoda Superb', 'Maruti Suzuki Desire', 'Toyota Camry'],
    'Hatchbacks': ['Maruti WagonR', 'Maruti Swift', 'Hyundai i20', 'Tata Altroz', 'Maruti Baleno',
                   'Toyota Glanza', 'Hyundai Grand i10', 'Renault Kwid'],
    'Autos': ['Auto'],
    'E-rickshaws': ['E-rickshaw'],
    'Motorcycles': ['Royal Enfield Super Meteor 650', 'Royal Enfield Shotgun 650',
                    'Royal Enfield Continental GT 650', 'Royal Enfield Himalayan', 'Royal Enfield Classic 350',
                    'Royal Enfield Hunter 350', 'TVS Apache RTR 160', 'TVS Ronin', 'Triumph Speed 400'],
    'Scooters': ['Activa 5G', 'Jupiter', 'Ola S1', 'Ather 450X']  # Duplicate 'Jupiter' removed
}

main_types = {
    'Four-wheeler': ['SUVs', 'Compact SUVs', 'Sedans', 'Hatchbacks'],
    'Three-wheeler': ['Autos', 'E-rickshaws'],
    'Two-wheeler': ['Motorcycles', 'Scooters']
}

DEPOSIT = 500

def load_customers():
    if os.path.exists(CUSTOMER_FILE):
        with open(CUSTOMER_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_customers():
    with open(CUSTOMER_FILE, 'w') as f:
        json.dump(customers, f, indent=4)

customers = load_customers()

class GPSTracker:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.latitude = round(random.uniform(19.0, 19.2), 6)
        self.longitude = round(random.uniform(72.8, 73.0), 6)
        self.is_tracking = True

    def get_location(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

    def update_location(self):
        self.latitude += round(random.uniform(-0.01, 0.01), 6)
        self.longitude += round(random.uniform(-0.01, 0.01), 6)

def display_options(options, title, allow_back=False, prices=None):
    print(f"\n{title}:")
    if allow_back:
        print("0. Go Back")
    for i, option in enumerate(options, 1):
        if prices and option in prices:
            base = prices[option]['base']
            per_km = prices[option]['per_km']
            print(f"{i}. {option} - Base Fare: ₹{base}, Per Km: ₹{per_km}")
        else:
            print(f"{i}. {option}")

def get_choice(options, allow_back=False):
    while True:
        try:
            choice = int(input("Enter your choice (number): "))
            if allow_back and choice == 0:
                return None
            choice -= 1
            if 0 <= choice < len(options):
                return options[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def get_pin(prompt):
    while True:
        pin = input(prompt).strip()
        if len(pin) == 6 and pin.isdigit():
            return pin
        else:
            print("PIN must be exactly 6 digits.")

def login():
    while True:
        print("\n--- Login ---")
        print("1. New Customer")
        print("2. Existing Customer")
        print("3. Admin")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            pin = get_pin("Set a 6-digit PIN: ")
            customer_id = f"{name}{random.randint(100, 999)}"
            customers[customer_id] = {'name': name, 'pin': pin, 'rentals': []}
            save_customers()
            print(f"Account created! Your Customer ID: {customer_id}")
            return customer_id, 'customer'
        
        elif choice == '2':
            customer_id = input("Enter your Customer ID: ").strip()
            if customer_id in customers:
                pin = input("Enter your 6-digit PIN: ").strip()
                if pin == customers[customer_id]['pin']:
                    print(f"Welcome back, {customers[customer_id]['name']}!")
                    return customer_id, 'customer'
                else:
                    print("Incorrect PIN.")
            else:
                print("Customer ID not found.")
        
        elif choice == '3':
            password = input("Enter Admin Password: ").strip()
            if password == "01092008":
                print("Admin access granted!")
                return 'admin', 'admin'
            else:
                print("Incorrect password.")
        
        elif choice == '4':
            print("Thank you for visiting! Goodbye.")
            exit()
        
        else:
            print("Invalid choice.")

def rent_vehicle(customer_id):
    print("\nGreetings! Let's rent a vehicle.")
    main_type_options = list(main_types.keys())
    while True:
        display_options(main_type_options, "Choose Vehicle Type", allow_back=True)
        main_type = get_choice(main_type_options, allow_back=True)
        if main_type is None:
            return  # Go back
        
        sub_type_options = main_types[main_type]
        display_options(sub_type_options, f"Choose {main_type} Subcategory", allow_back=True, prices=pricing)
        sub_type = get_choice(sub_type_options, allow_back=True)
        if sub_type is None:
            continue
        
        model_options = vehicles[sub_type]
        display_options(model_options, f"Choose {sub_type} Model", allow_back=True)
        model = get_choice(model_options, allow_back=True)
        if model is None:
            continue
        
        while True:
            kms_input = input("Enter the number of kilometers you plan to travel (or 0 to go back): ").strip()
            if kms_input == '0':
                break
            try:
                kms = float(kms_input)
                if kms > 0:
                    break
                else:
                    print("Kilometers must be positive.")
            except ValueError:
                print("Please enter a valid number for kilometers.")
        else:
            continue
        
        print(f"\nYou chose to rent: {model} ({sub_type}) for {kms} kilometers.")
        confirm = input("Confirm rental? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Rental cancelled. Starting over.")
            continue
        
        gps = GPSTracker(model)
        base = pricing[sub_type]['base']
        per_km = pricing[sub_type]['per_km']
        rental_cost = base + (kms * per_km)
        total_cost = rental_cost + DEPOSIT
        
        rental = {
            'vehicle': model,
            'sub_type': sub_type,
            'kms': kms,
            'gps': {'latitude': gps.latitude, 'longitude': gps.longitude},
            'cost': total_cost
        }
        customers[customer_id]['rentals'].append(rental)
        save_customers()
        
        print("\n--- Rental Confirmed ---")
        print(f"Vehicle: {model} ({sub_type})")
        print(f"Kilometers: {kms}")
        print(f"Total Cost: ₹{total_cost} (including ₹{DEPOSIT} deposit)")
        print(f"GPS Tracking started at Latitude: {gps.latitude}, Longitude: {gps.longitude}")
        return

def track_vehicle(customer_id):
    rentals = customers[customer_id]['rentals']
    if not rentals:
        print("No vehicles rented yet. Please rent a vehicle first to track its location.")
        return
    
    if len(rentals) == 1:
        selected_rental = rentals[0]
    else:
        while True:
            print("You have multiple rentals:")
            for i, rental in enumerate(rentals, 1):
                print(f"{i}. {rental['vehicle']} ({rental['sub_type']})")
            print("0. Go Back")
            try:
                choice = int(input("Choose which vehicle to track (number): "))
                if choice == 0:
                    return
                if 1 <= choice <= len(rentals):
                    selected_rental = rentals[choice - 1]
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
    
    lat = selected_rental['gps']['latitude']
    lon = selected_rental['gps']['longitude']
    print(f"\nTracking {selected_rental['vehicle']} ({selected_rental['sub_type']}):")
    print(f"Current Location: Latitude: {lat}, Longitude: {lon}")
    update = input("Simulate location update? (y/n): ").strip().lower()
    if update == 'y':
        lat += round(random.uniform(-0.01, 0.01), 6)
        lon += round(random.uniform(-0.01, 0.01), 6)
        selected_rental['gps']['latitude'] = lat
        selected_rental['gps']['longitude'] = lon
        save_customers()
        print(f"Updated Location: Latitude: {lat}, Longitude: {lon}")

def admin_view_customers():
    if not customers:
        print("No customers registered.")
    else:
        print("\n--- Customer List ---")
        for cid, data in customers.items():
            print(f"ID: {cid}, Name: {data['name']}")

def admin_view_vehicles():
    print("\n--- All Vehicles List ---")
    for sub_type, models in vehicles.items():
        print(f"{sub_type}:")
        if models:
            for model in models:
                print(f" - {model}")
        else:
            print(" (No vehicles in this subcategory)")

def admin_add_vehicle():
    while True:
        print("\n--- Add New Vehicle ---")
        sub_type_options = list(vehicles.keys())
        display_options(sub_type_options, "Choose Subcategory to Add Vehicle", allow_back=True)
        sub_type = get_choice(sub_type_options, allow_back=True)
        if sub_type is None:
            return
        new_vehicle = input("Enter the new vehicle model name (or '0' to go back): ").strip()
        if new_vehicle == '0':
            continue
        if new_vehicle and new_vehicle not in vehicles[sub_type]:
            vehicles[sub_type].append(new_vehicle)
            print(f"Vehicle '{new_vehicle}' added to {sub_type}.")
            return
        else:
            print("Vehicle already exists or invalid name.")

def admin_delete_vehicle():
    while True:
        print("\n--- Delete Vehicle ---")
        sub_type_options = list(vehicles.keys())
        display_options(sub_type_options, "Choose Subcategory to Delete From", allow_back=True)
        sub_type = get_choice(sub_type_options, allow_back=True)
        if sub_type is None:
            return
        if not vehicles[sub_type]:
            print("No vehicles in this subcategory.")
            return
        display_options(vehicles[sub_type], f"Choose Vehicle to Delete from {sub_type}", allow_back=True)
        vehicle = get_choice(vehicles[sub_type], allow_back=True)
        if vehicle is None:
            continue
        vehicles[sub_type].remove(vehicle)
        print(f"Vehicle '{vehicle}' deleted from {sub_type}.")
        return

def admin_edit_vehicle():
    while True:
        print("\n--- Edit Vehicle ---")
        sub_type_options = list(vehicles.keys())
        display_options(sub_type_options, "Choose Subcategory to Edit", allow_back=True)
        sub_type = get_choice(sub_type_options, allow_back=True)
        if sub_type is None:
            return
        if not vehicles[sub_type]:
            print("No vehicles in this subcategory.")
            return
        display_options(vehicles[sub_type], f"Choose Vehicle to Edit in {sub_type}", allow_back=True)
        old_vehicle = get_choice(vehicles[sub_type], allow_back=True)
        if old_vehicle is None:
            continue
        new_vehicle = input(f"Enter new name for '{old_vehicle}' (or '0' to cancel): ").strip()
        if new_vehicle == '0' or not new_vehicle:
            print("Edit cancelled.")
            return
        if new_vehicle and new_vehicle not in vehicles[sub_type]:
            index = vehicles[sub_type].index(old_vehicle)
            vehicles[sub_type][index] = new_vehicle
            print(f"Vehicle '{old_vehicle}' renamed to '{new_vehicle}'.")
            return
        else:
            print("Invalid or duplicate vehicle name.")

def admin_clear_customers():
    confirm = input("Are you sure you want to clear all customers? This action cannot be undone. (yes/no): ").strip().lower()
    if confirm == 'yes':
        customers.clear()
        save_customers()
        print("All customers cleared.")
    else:
        print("Action cancelled.")

def admin_track_all_vehicles():
    customers_with_rentals = {cid: data for cid, data in customers.items() if data.get('rentals')}
    if not customers_with_rentals:
        print("No rented vehicles found for any customer.")
        return

    while True:
        print("\n--- Customers with Rented Vehicles ---")
        cust_ids = list(customers_with_rentals.keys())
        for i, cid in enumerate(cust_ids, 1):
            print(f"{i}. {customers[cid]['name']} (ID: {cid})")
        print("0. Go Back")
        try:
            choice = int(input("Choose a customer to view rentals: "))
            if choice == 0:
                return
            if 1 <= choice <= len(cust_ids):
                selected_cust_id = cust_ids[choice - 1]
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    rentals = customers[selected_cust_id]['rentals']

    while True:
        if len(rentals) == 1:
            selected_rental = rentals[0]
        else:
            print(f"\nRented Vehicles for {customers[selected_cust_id]['name']}:")
            for i, r in enumerate(rentals, 1):
                print(f"{i}. {r['vehicle']} ({r['sub_type']})")
            print("0. Go Back")
            try:
                vchoice = int(input("Choose a vehicle to track: "))
                if vchoice == 0:
                    return
                if 1 <= vchoice <= len(rentals):
                    selected_rental = rentals[vchoice - 1]
                else:
                    print("Invalid choice.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

        lat = selected_rental['gps']['latitude']
        lon = selected_rental['gps']['longitude']
        print(f"\nTracking {selected_rental['vehicle']} ({selected_rental['sub_type']}):")
        print(f"Current Location: Latitude: {lat}, Longitude: {lon}")

        update = input("Simulate location update? (y/n): ").strip().lower()
        if update == 'y':
            lat += round(random.uniform(-0.01, 0.01), 6)
            lon += round(random.uniform(-0.01, 0.01), 6)
            selected_rental['gps']['latitude'] = lat
            selected_rental['gps']['longitude'] = lon
            save_customers()
            print(f"Updated Location: Latitude: {lat}, Longitude: {lon}")

        return

def main():
    print("Welcome to the Vehicle Rental System!")
    while True:
        current_user, role = login()
        while True:
            if role == 'admin':
                print("\n--- Admin Menu ---")
                print("1. View Customer List")
                print("2. Add New Vehicle")
                print("3. Delete Vehicle")
                print("4. Edit Vehicle")
                print("5. Clear Customer List")
                print("6. View All Vehicles")
                print("7. Track All Rented Vehicles")
                print("8. Logout")
                choice = input("Choose an option (1-8): ").strip()
                if choice == '1':
                    admin_view_customers()
                elif choice == '2':
                    admin_add_vehicle()
                elif choice == '3':
                    admin_delete_vehicle()
                elif choice == '4':
                    admin_edit_vehicle()
                elif choice == '5':
                    admin_clear_customers()
                elif choice == '6':
                    admin_view_vehicles()
                elif choice == '7':
                    admin_track_all_vehicles()
                elif choice == '8':
                    print("Logging out from admin account.")
                    break
                else:
                    print("Invalid choice.")
            elif role == 'customer':
                print(f"\n--- Customer Menu for {customers[current_user]['name']} ---")
                print("1. Rent a Vehicle")
                print("2. Track Rented Vehicle")
                print("3. Logout")
                choice = input("Choose an option (1-3): ").strip()
                if choice == '1':
                    rent_vehicle(current_user)
                elif choice == '2':
                    track_vehicle(current_user)
                elif choice == '3':
                    print(f"Goodbye, {customers[current_user]['name']}! Thank you for using our service. Safe travels!")
                    break
                else:
                    print("Invalid choice.")

if __name__ == "__main__":
    main()
