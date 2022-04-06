from ride import Ride
from ride import RideStatus

class Rider():
    def __init__(self, name) -> None:
        self.name           = name
        self.completdRides  = []
        self.currentRide    = None
    
    def createRide(self, id, source, dest, seats):
        reason = None
        if source >= dest:
            reason = "Wrong values of Origin and Destination."
            return False, reason

        self.currentRide = Ride(
            id = id,
            source = source,
            dest = dest,
            seats =seats
        )
        return True, reason

    def updateRide(self, id, source, dest, seats):
        reason = None
        if self.currentRide == None:
            return self.createRide(id, source, dest, seats)
        
        if self.currentRide.rideStatus == RideStatus.CANCELLED.value:
            reason = "Cannot update ride for cancelled ride."
            return False, reason
        
        if self.currentRide.rideStatus == RideStatus.COMPLETED.value:
            reason = "Cannot update ride for completed ride."
            return False, reason

        if source >= dest:
            reason = "Wrong values of Origin and Destination."
            return False, reason

        self.currentRide.id = id
        self.currentRide.source = source
        self.currentRide.dest = dest
        self.currentRide.seats = seats
        return True, reason

    def withdrawRide(self, id):
        reason = None
        if self.currentRide == None:
            reason = "No ride created yet."
            return False, reason

        if self.currentRide.id != id:
            reason = "Wrong id passed."
            return False, reason
        
        if self.currentRide.rideStatus != RideStatus.BOOKED.value:
            reason = "Ride wasn't created. Can't withdraw."
            return False, reason
        
        self.currentRide.rideStatus = RideStatus.CANCELLED.value
        return True, reason

    def closeRide(self):
        reason = None
        if(self.currentRide == None):
            reason = "No ride active for Rider."
            return 0, reason

        if self.currentRide.rideStatus != RideStatus.BOOKED.value:
            reason = "Ride wasn't in progress. Can't close."
            return 0, reason
        
        self.currentRide.rideStatus = RideStatus.COMPLETED.value
        self.completdRides.append(self.currentRide)
        return self.currentRide.calculateFare(len(self.completdRides)), reason




