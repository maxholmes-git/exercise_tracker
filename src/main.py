import json
import os
from datetime import datetime

def get_last_workout_details(chosen_workout: str, workout_jsons_dir: str) -> dict:

    files = os.listdir(workout_jsons_dir)

    latest_date = None
    for file_name in files:
        if chosen_workout in file_name:
            date_str = file_name.split("_")[-1].split(".")[0]
            date_obj = datetime.strptime(date_str, "%d%m%Y")
            if latest_date is None:
                latest_date = date_obj
            elif date_obj > latest_date:
                latest_date = date_obj
        
    file_path = f"{workout_jsons_dir}/{chosen_workout}_{latest_date.strftime('%d%m%Y')}.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    return data

if __name__ == "__main__":
    workout_jsons_dir = f"{os.getcwd()}/json_files"
    chosen_workout_int = "1"
    
    workout_values_dict = {
        "1": "chest_and_tris",
        "2": "back_and_bis",
        "3": "shoulders",
        "4": "legs"
    }

    if not chosen_workout_int:
        print("Choose a workout: \n"
          "1: chest_and_tris\n"
          "2: back_and_bis\n"
          "3: shoulders\n"
          "4: legs\n\n")
        chosen_workout_int = input("Input: ")

    chosen_workout = workout_values_dict[chosen_workout_int]

    last_workout_details = get_last_workout_details(chosen_workout, workout_jsons_dir)
    date_str = last_workout_details['date']

    current_workout_details = last_workout_details.copy()

    print(f"\nLast {chosen_workout} Workout: {datetime.strptime(date_str,'%d%m%Y')}\n")

    for j, exercise in enumerate(last_workout_details["exercises"]):
        print(exercise['name'] + ":")
        print(f"Max reps (Weight: {exercise['weight']}kg): {exercise['max_reps']}")
        print(f"Last reps (Weight: {exercise['weight']}kg): {exercise['reps']}")
        if exercise['notes']:
            print(f"Notes: {exercise['notes']}")
        all_reps = []
        print("\n")
        for i, set in enumerate(exercise["reps"]):
            reps = input(f"Set {i + 1} ({set}): ")
            all_reps.append(int(reps))
        
        current_workout_details["exercises"][j]["reps"] = all_reps

        last_sum_reps = sum(exercise["max_reps"])
        current_sum_reps = sum(all_reps)
        if current_sum_reps > last_sum_reps:
            current_workout_details["exercises"][j]["max_reps"] = all_reps
            print(f"\nNew max reps for {exercise['name']} ({exercise['weight']}kg): {current_sum_reps}")
        print("\n\n")

    current_workout_details["date"] = datetime.now().strftime("%d%m%Y")
    
    with open(f"{workout_jsons_dir}/{chosen_workout}_{current_workout_details['date']}.json", "w") as file:
        json.dump(current_workout_details, file, indent=4)
