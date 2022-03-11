from rider import Rider
# from driver import Driver

def main():
    r1 = Rider("Vishal R")
    # Driver d1("Vishal d")
    print("--------------------Test 1--------------------")
    r1.createRide(1, 10, 20, 2)
    r1.closeRide()
    print("--------------------Test 2--------------------")
    r1.createRide(2, 10, 20, 2)
    r1.withdrawRide(3)
    r1.updateRide(2, 30, 20, 2)
    r1.closeRide()
    print("--------------------Test 3--------------------")
    r1.createRide(2, 10, 20, 2)
    r1.withdrawRide(2)
    r1.updateRide(3, 10, 110, 2)
    r1.closeRide()
    print("--------------------Test done--------------------")


if __name__ == "__main__":
    main()