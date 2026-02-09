import os
from collections import defaultdict

class VehicleUnavailableError(Exception):
    pass

class InvalidDurationError(Exception):
    pass

class VehicleNotFoundError(Exception):
    pass

class FileError(Exception):
    pass


class Vehicle:
    def __init__(self, plate_id: str, make_model: str, category: str, daily_rate: float, is_available: bool = True):
        self.plate_id = plate_id
        self.make_model = make_model
        self.category = category
        self.daily_rate = daily_rate
        self.is_available = is_available

    def display_info(self) -> str:
        status = "[Available]" if self.is_available else "[Rented]"
        return f"{status} {self.make_model} ({self.category}) - ${self.daily_rate:.2f}/day"

    def set_rented(self):
        self.is_available = False

    def set_available(self):
        self.is_available = True

    def __str__(self):
        return f"{self.plate_id},{self.make_model},{self.category},{self.daily_rate},{self.is_available}"

    @staticmethod
    def from_string(data_string: str):
        try:
            plate_id, make_model, category, daily_rate_str, is_available_str = data_string.strip().split(',')
            daily_rate = float(daily_rate_str)
            is_available = is_available_str.lower() == 'true'
            return Vehicle(plate_id, make_model, category, daily_rate, is_available)
        except (ValueError, IndexError) as e:
            raise FileError(f"Corrupted Vehicle data: {data_string}") from e


class Rental:
    _next_rental_id = 1

    def __init__(self, customer_name: str, vehicle_plate: str, daily_rate: float, days_rented: int,
                 rental_id: int = None):
        if rental_id is None:
            self.rental_id = Rental._next_rental_id
            Rental._next_rental_id += 1
        else:
            self.rental_id = rental_id
            if rental_id >= Rental._next_rental_id:
                Rental._next_rental_id = rental_id + 1

        self.customer_name = customer_name
        self.vehicle_plate = vehicle_plate
        self.daily_rate = daily_rate
        self.days_rented = days_rented
        self.total_cost = daily_rate * days_rented

    def generate_receipt(self) -> str:
        return (
            f"\n--- RENTAL RECEIPT (ID: {self.rental_id}) ---\n"
            f"Customer: {self.customer_name}\n"
            f"Vehicle Plate: {self.vehicle_plate}\n"
            f"Daily Rate: ${self.daily_rate:.2f}\n"
            f"Days Rented: {self.days_rented}\n"
            f"Total Cost: ${self.total_cost:.2f}\n"
            f"-----------------------------------------"
        )

    def __str__(self):
        return f"{self.rental_id},{self.customer_name},{self.vehicle_plate},{self.daily_rate},{self.days_rented},{self.total_cost}"

    @staticmethod
    def from_string(data_string: str):
        try:
            parts = data_string.strip().split(',')
            if len(parts) != 6:
                raise FileError("Incomplete Rental data.")

            rental_id = int(parts[0])
            customer_name = parts[1]
            vehicle_plate = parts[2]
            daily_rate = float(parts[3])
            days_rented = int(parts[4])

            new_rental = Rental(customer_name, vehicle_plate, daily_rate, days_rented, rental_id=rental_id)
            return new_rental

        except (ValueError, IndexError, FileError) as e:
            raise FileError(f"Corrupted Rental data: {data_string}") from e

class FleetManager:
    def __init__(self):
        self.fleet: list[Vehicle] = []
        self.rentals: list[Rental] = []

    def _find_vehicle(self, plate_id: str) -> Vehicle:
        for vehicle in self.fleet:
            if vehicle.plate_id == plate_id:
                return vehicle
        raise VehicleNotFoundError(f"Vehicle with plate ID '{plate_id}' not found.")

    def add_vehicle(self, vehicle: Vehicle):
        try:
            self._find_vehicle(vehicle.plate_id)
            print(f"Warning: Vehicle with plate ID '{vehicle.plate_id}' already exists. Skipping addition.")
            return
        except VehicleNotFoundError:
            self.fleet.append(vehicle)

    def rent_vehicle(self, plate_id: str, customer: str, days: int) -> tuple[float, str]:
        if days <= 0:
            raise InvalidDurationError("Rental duration must be greater than zero.")

        vehicle = self._find_vehicle(plate_id)

        if not vehicle.is_available:
            raise VehicleUnavailableError(f"Vehicle {plate_id} is currently UNAVAILABLE.")

        vehicle.set_rented()

        new_rental = Rental(customer, plate_id, vehicle.daily_rate, days)
        self.rentals.append(new_rental)

        receipt = new_rental.generate_receipt()
        return new_rental.total_cost, receipt

    def return_vehicle(self, plate_id: str):
        vehicle = self._find_vehicle(plate_id)
        vehicle.set_available()

    def generate_revenue_report(self) -> str:
        total_revenue = sum(rental.total_cost for rental in self.rentals)

        category_revenue = defaultdict(float)

        for rental in self.rentals:
            try:
                vehicle = self._find_vehicle(rental.vehicle_plate)
                category_revenue[vehicle.category] += rental.total_cost
            except VehicleNotFoundError:
                pass

        if not category_revenue:
            most_popular_category = "N/A"
        else:
            most_popular_category = max(category_revenue, key=category_revenue.get)

        report = (
            "--- Revenue Report ---\n"
            f"Total Revenue: ${total_revenue:.2f}\n"
            f"Most Popular Category: {most_popular_category}"
        )
        return report

    def get_most_rented_category(self) -> str:
        category_revenue = defaultdict(float)

        for rental in self.rentals:
            try:
                vehicle = self._find_vehicle(rental.vehicle_plate)
                category_revenue[vehicle.category] += rental.total_cost
            except VehicleNotFoundError:
                continue

        if not category_revenue:
            return "No rentals recorded."

        return max(category_revenue, key=category_revenue.get)

    def save_state(self, filename: str):
        try:
            with open(filename, 'w') as f:
                f.write("---VEHICLES---\n")
                for vehicle in self.fleet:
                    f.write(f"V,{vehicle}\n")

                f.write("---RENTALS---\n")
                for rental in self.rentals:
                    f.write(f"R,{rental}\n")
        except IOError as e:
            raise FileError(f"Error saving state to {filename}: {e}")

    def load_state(self, filename: str):
        if not os.path.exists(filename):
            raise FileError(f"File not found: {filename}")

        self.fleet = []
        self.rentals = []
        in_vehicle_section = False
        in_rental_section = False

        try:
            with open(filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    if line == "---VEHICLES---":
                        in_vehicle_section = True
                        in_rental_section = False
                        continue
                    elif line == "---RENTALS---":
                        in_vehicle_section = False
                        in_rental_section = True
                        continue

                    if in_vehicle_section and line.startswith("V,"):
                        data_string = line[2:]
                        self.fleet.append(Vehicle.from_string(data_string))
                    elif in_rental_section and line.startswith("R,"):
                        data_string = line[2:]
                        self.rentals.append(Rental.from_string(data_string))

        except IOError as e:
            raise FileError(f"Error reading state file {filename}: {e}")
        except FileError as e:
            raise e
        except Exception as e:
            raise FileError(f"An unexpected error occurred while loading state: {e}")


def main_menu(manager: FleetManager, state_file: str):
    print("=== CityDrive Fleet Management System ===")

    try:
        manager.load_state(state_file)
        print(f">> State successfully loaded from {state_file}.")
    except FileError as e:
        print(f">> No previous state found or file error: {e}. Starting fresh.")

    while True:
        print("\n1. Add Vehicle")
        print("2. Rent Vehicle")
        print("3. Return Vehicle")
        print("4. Generate Reports")
        print("5. Save & Exit")

        choice = input("Select: ").strip()

        try:
            if choice == '1':
                print("Enter Vehicle Details:")
                plate = input("Plate: ").strip()
                model = input("Model: ").strip()
                category = input("Category: ").strip()
                daily_rate_input = input("Daily Rate: ").strip()

                daily_rate = float(daily_rate_input)

                vehicle = Vehicle(plate, model, category, daily_rate)
                manager.add_vehicle(vehicle)
                print(f">> Vehicle {plate} added to fleet.")

            elif choice == '2':
                plate = input("Enter Plate to Rent: ").strip()
                customer = input("Customer Name: ").strip()
                days_input = input("Days: ").strip()

                days = int(days_input)

                total_cost, receipt = manager.rent_vehicle(plate, customer, days)
                print(f">> Rental Successful! Total Cost: ${total_cost:.2f}")
                print(">> Receipt generated.")

            elif choice == '3':
                plate = input("Enter Plate to Return: ").strip()
                manager.return_vehicle(plate)
                print(">> Vehicle returned. Status updated to Available.")

            elif choice == '4':
                report = manager.generate_revenue_report()
                print(report)

            elif choice == '5':
                manager.save_state(state_file)
                print(f">> State saved to {state_file}.")
                print("Exiting System.")
                break

            else:
                print("Invalid selection. Please choose from 1-5.")

        except (ValueError) as e:
            print(f">> Error: Invalid input type. Please ensure Daily Rate is a number and Days is an integer. ({e})")
        except (FileError, InvalidDurationError, VehicleUnavailableError, VehicleNotFoundError) as e:
            print(f">> Error: {e}")
        except Exception as e:
            print(f">> An unexpected error occurred: {e}")


if __name__ == "__main__":
    fleet_manager = FleetManager()
    STATE_FILE = "fleet_state.txt"

    main_menu(fleet_manager, STATE_FILE)