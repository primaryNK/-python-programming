import cars

def show_cars():
    benz = cars.benz(0, "red")
    oudi = cars.oudi(0, "blue")

    benz.speed_up()
    benz.show()

    oudi.speed_up()
    oudi.show()

show_cars()