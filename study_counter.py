import helpers as h
import files
import time


class TimeCounter:
    def __init__(self, data):
        self.data = data
        self.counter = 0

    # Updates the counter
    def update_counter(self):
        self.counter = int(files.load(self.data))
        print("Total study time:", h.convert_hours(self.counter), "hours")

    # Lets the user study for a custom time
    def custom_time(self):
        start = time.time()
        print("Stopwatch started!")
        input("\nTap 'Enter' to stop >> ")
        print("")
        end = time.time()

        total_time = int((end - start))
        print("Studied for:", round(total_time / 60, 2), "minutes")
        self.counter += total_time
        files.save(self.counter, self.data)

    # Lets the user study for a scheduled time
    def study_time(self, minutes: int):
        start = time.time()

        print("Timer started!")
        for second in range(0, minutes * 60):
            time.sleep(1)
            self.counter += 1

            # Save to file every 60 seconds
            if second % 60 == 0:
                files.save(self.counter, self.data)

        files.save(self.counter, self.data)
        end = time.time()

        time_studied = f"Studied for: {int((end - start) / 60)} minutes"
        h.notify("Session complete!", time_studied)

    def study(self):
        self.update_counter()

        # Get user input for the timer
        user_input = input("How many minutes would you like to study for? >> ")
        if user_input == "":
            self.custom_time()
        else:
            try:
                self.study_time(int(user_input))
            except:
                print(user_input, "is not a valid input.")

        # Check for achievements
        self.update_counter()

        h.achievements(h.convert_hours(self.counter))


