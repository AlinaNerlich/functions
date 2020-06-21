def steps_counter():
    distance = float(input("The distance walked in meter (e.g. 3.5): "))
    lenght = float(input("The lenght of my steps in meter (e.g. 0.2): "))
    return distance/lenght

print("You needed " + str(steps_counter) + "steps")