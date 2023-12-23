class Boat:
    def __init__(self, boat_number, money_taken, total_hours_hired, return_time):
        self.boat_number = boat_number
        self.money_taken = money_taken
        self.total_hours_hired = total_hours_hired
        self.return_time = return_time

HOURLY_RATE = 20.0
HALF_HOUR_RATE = 12.0
NUM_BOATS = 10
OPEN_TIME = "10:00"
CLOSE_TIME = "17:00"

def calculate_money_for_boat(boat):
    print(f"Enter the hours you want to hire Boat {boat.boat_number} (between 0.5 and 7): ")
    hours_to_hire = float(input())

    while hours_to_hire < 0.5 or hours_to_hire > 7 or boat.return_time >= CLOSE_TIME:
        print(f"Invalid hours or boat cannot be hired after {CLOSE_TIME}. Please enter a valid duration: ")
        hours_to_hire = float(input())

    if hours_to_hire <= 1:
        cost = HOURLY_RATE * hours_to_hire
    else:
        cost = HALF_HOUR_RATE * hours_to_hire

    boat.money_taken += cost
    boat.total_hours_hired += hours_to_hire

    current_hour, current_minute = map(int, boat.return_time.split(':'))
    current_hour += int(hours_to_hire)
    boat.return_time = f"{current_hour:02d}:{current_minute:02d}"

    print(f"Boat {boat.boat_number} hired for {hours_to_hire} hours. Total cost: ${cost:.2f}")

def find_available_boats(boats, current_time):
    print("\n--- Available Boats and Slots ---")
    for boat in boats:
        if boat.return_time <= current_time:
            print(f"Boat {boat.boat_number} is available until {boat.return_time}")

def calculate_total_money(boats):
    total_money = 0.0
    total_hours = 0.0
    unused_boats = 0
    most_used_boat = 1
    max_hours_hired = boats[0].total_hours_hired

    for boat in boats:
        total_money += boat.money_taken
        total_hours += boat.total_hours_hired

        if boat.total_hours_hired == 0:
            unused_boats += 1

        if boat.total_hours_hired > max_hours_hired:
            most_used_boat = boat.boat_number
            max_hours_hired = boat.total_hours_hired

    print("\n--- End of Day Report ---")
    print(f"Total revenue from all boats: ${total_money:.2f}")
    print(f"Total hours boats were hired: {total_hours:.2f} hours")
    print(f"Number of boats not used today: {unused_boats}")
    print(f"Boat #{most_used_boat} was used the most, with {max_hours_hired:.2f} hours hired.")

def main():
    boats = [Boat(i, 0.0, 0.0, OPEN_TIME) for i in range(1, NUM_BOATS + 1)]

    print("Enter the current time (24-hour format, e.g., 14:30): ")
    current_time = input()

    while True:
        print("\nOptions:")
        print("1. Hire a boat")
        print("2. View available boats and slots")
        print("3. View end-of-day report")
        print("4. End the program")
        print("Enter your choice (1-4): ")

        choice = int(input())

        if choice == 1:
            print("Enter the boat number you want to hire: ")
            boat_number = int(input())
            if 1 <= boat_number <= NUM_BOATS:
                calculate_money_for_boat(boats[boat_number - 1])
            else:
                print(f"Invalid boat number. Please enter a number between 1 and {NUM_BOATS}.")
        elif choice == 2:
            find_available_boats(boats, current_time)
        elif choice == 3:
            calculate_total_money(boats)
            break  # End the program after generating the report
        elif choice == 4:
            break  # End the program
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

#Coded by Zohra Batool
