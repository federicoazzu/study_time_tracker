import helpers as h
import files
import time

# Load initial counter data
counter = 0


def refresh_counter():
    global counter
    counter = int(files.load())
    print("Total study time:", h.convert_hours(counter), "hours")


def study_time(minutes: int):
    global counter
    start = time.time()

    print("Timer started!")
    for second in range(0, minutes * 60):
        time.sleep(1)
        counter += 1

        # Save to file every 60 seconds
        if second % 60 == 0:
            files.save(counter)

    files.save(counter)
    end = time.time()

    time_studied = f"Studied for: {int((end - start) / 60)} minutes"
    h.notify("Session complete!", time_studied)


# Get counter details
refresh_counter()

# Check for achievements
h.achievements(h.convert_hours(counter))

# Get user input for the timer
user_input = int(input("How many minutes would you like to study for? >> "))
study_time(user_input)

# Display final data
refresh_counter()
