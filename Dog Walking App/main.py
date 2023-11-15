import random
import datetime

available_breeds = ["Labrador", "Poodle", "Golden Retriever", "Bulldog", "German Shepherd"]

dog_rate_per_walk = 10
rate_per_minute = 1

available_dog_walkers = ["John", "Emily", "William", "Sophia", "David"]

def get_future_walk_datetime():
    while True:
        try:
            date_str = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
            walk_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            current_datetime = datetime.datetime.now()
            
            if walk_datetime < current_datetime:
                print("Please select a future date and time.")
            else:
                return walk_datetime
        except ValueError:
            print("Invalid input. Please enter a valid date and time in the format 'YYYY-MM-DD HH:MM'.")

def select_dog_breeds():
    num_dogs = int(input("Enter the number of dogs to be walked: "))
    print("Select dog breeds to be walked:")
    
    selected_breeds = set()
    
    while len(selected_breeds) < num_dogs:
        print("\nAvailable breeds:")
        for i, breed in enumerate(available_breeds, start=1):
            print(f"{i}. {breed}")
        
        selection = int(input(f"Select breed for dog {len(selected_breeds) + 1}: "))
        
        if selection not in range(1, len(available_breeds) + 1):
            print("Invalid selection. Please try again.")
        elif available_breeds[selection - 1] in selected_breeds:
            print("That breed has already been selected. Please choose another.")
        else:
            selected_breeds.add(available_breeds[selection - 1])
    
    return list(selected_breeds)

walk_datetime = get_future_walk_datetime()
walk_duration = int(input("Enter duration of the walk in minutes: "))
selected_dog_breeds = select_dog_breeds()

total_fee = dog_rate_per_walk * len(selected_dog_breeds) + rate_per_minute * walk_duration
selected_dog_walker = random.choice(available_dog_walkers)

print("\nBooking details:")
print(f"Date/time: {walk_datetime}")
print(f"Duration of walk: {walk_duration} minutes")
print(f"Number of dogs: {len(selected_dog_breeds)}")
print("Dog breeds:")
for breed in selected_dog_breeds:
    print(f"- {breed}")
print(f"Total Fee: ${total_fee}")
print(f"Dog Walker: {selected_dog_walker}")
