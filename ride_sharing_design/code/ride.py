import enum
import constants
import enum

class RideStatus(enum.Enum):
    BOOKED      = 1
    CANCELLED   = 2
    COMPLETED   = 3


class Ride():

    def __init__(self, id, source, dest, seats)-> None:
        self.id = id
        self.source = source
        self.dest = dest
        self.seats = seats
        self.rideStatus = RideStatus.BOOKED.value
    
    def calculateFare(self, totalRides):
        isPriorityRider = True if totalRides > 10 else False

        dist = self.dest - self.source
        
        if self.seats < 2:
            return dist * constants.AMT_PER_KM * (0.75 if isPriorityRider else 1)

        return dist * constants.AMT_PER_KM * self.seats * (0.5 if isPriorityRider else 0.75)
