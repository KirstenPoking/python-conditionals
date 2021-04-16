current_speed = float(input("Enter your current speed in km/hr: "))
average_allowed_speed = float(input("Enter average allowed speed of the road in km/hr: "))
points = (current_speed - average_allowed_speed)/5
if points >= 1:
    print(points, "Demerit points")
    if points > 12:
        print("Time to go to jail!")
if current_speed <= 60:
    print("OK")
