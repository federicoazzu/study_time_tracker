import study_counter as sc

while True:
    counter = sc.TimeCounter(data="data.txt")
    counter.study()
    input("\nTap 'Enter' to continue >> ")
    print("")

