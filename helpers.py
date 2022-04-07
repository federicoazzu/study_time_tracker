import os


def convert_hours(counter):
    return round(counter / 60 / 60, 2)


def achievements(counter_hours):
    if counter_hours >= 1000:
        print("+ 1000 hours studied! - New Laptop")
    if counter_hours >= 500:
        print("+ 500 hours studied, amazing!")
    if counter_hours >= 100:
        print("+ 100 hours studied! - iPhone SE (3rd Gen)")
    if counter_hours >= 10:
        print("+ 10 hours studied, nice!")


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" sound name "default"'
              """.format(text, title))
