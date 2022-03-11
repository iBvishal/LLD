from ride import Ride
from ride import RideStatus

class Rider():
    def __init__(self, name) -> None:
        self.name           = name
        self.completdRides  = []
        self.currentRide    = None
    
    def createRide(self, id, source, dest, seats):
        if source >= dest:
            print("Wrong values of Origin and Destination...")
            return

        self.currentRide = Ride(
            id = id,
            source = source,
            dest = dest,
            seats =seats
        )

    def updateRide(self, id, source, dest, seats):
        if self.currentRide == None:
            self.createRide(id, source, dest, seats)
            return
        
        if self.currentRide.rideStatus == RideStatus.CANCELLED.value:
            print("Cannot update ride for cancelled ride...")
            return
        
        if self.currentRide.rideStatus == RideStatus.COMPLETED.value:
            print("Cannot update ride for completed ride...")
            return

        if source >= dest:
            print("Wrong values of Origin and Destination...")
            return

        self.currentRide.id = id
        self.currentRide.source = source
        self.currentRide.dest = dest
        self.currentRide.seats = seats

    def withdrawRide(self, id):
        
        if self.currentRide == None:
            print("No ride created yet...")
            return

        if self.currentRide.id != id:
            print("Wrong id passed...")
            return
        
        if self.currentRide.rideStatus != RideStatus.BOOKED.value:
            print("Ride wasn't created. Can't withdraw...")
            return
        
        self.currentRide.rideStatus = RideStatus.CANCELLED.value

    def closeRide(self):
        if self.currentRide.rideStatus != RideStatus.BOOKED.value:
            print("Ride wasn't in progress. Can't close...")
            return 0
        
        self.currentRide.rideStatus = RideStatus.COMPLETED.value
        self.completdRides.append(self.currentRide)
        print(self.currentRide.calculateFare(len(self.completdRides)))




