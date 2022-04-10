from rider import Rider
from ride import RideStatus

def test_create_valid_ride():
    rider = Rider("Vishal R")
    is_created, reason = rider.createRide(1, 10, 20, 2)
    assert is_created == True
    assert reason == None

    assert rider.currentRide.id == 1
    assert rider.currentRide.source == 10
    assert rider.currentRide.dest == 20
    assert rider.currentRide.seats == 2

def test_close_valid_ride():
    rider = Rider("Vishal R")
    
    is_created, reason = rider.createRide(1, 10, 20, 2)
    assert is_created == True
    assert reason == None

    calculated_fare, reason = rider.closeRide()
    assert calculated_fare != None
    assert calculated_fare == 300.0
    assert reason == None

def test_invalid_update_for_ride():
    rider = Rider("Vishal R")
    is_created, reason = rider.createRide(1, 10, 20, 2)
    assert is_created == True
    assert reason == None

    is_updated, reason = rider.updateRide(2, 30, 20, 3)
    assert is_updated == False
    assert reason == "Wrong values of Origin and Destination."

def test_update_valid_ride():
    rider = Rider("Vishal R")
    is_created, reason = rider.createRide(1, 10, 20, 2)

    is_updated, reason = rider.updateRide(2, 30, 40, 3)
    assert is_updated == True
    assert reason == None

def test_withdraw_ride():
    rider = Rider("Vishal R")
    rider.createRide(1, 10, 20, 2)

    assert rider.currentRide.rideStatus == RideStatus.BOOKED.value
    is_withdrawn, reason = rider.withdrawRide(1)
    assert is_withdrawn == True
    assert reason == None
    assert rider.currentRide.rideStatus == RideStatus.CANCELLED.value

def test_cant_update_withdrawn_ride():
    rider = Rider("Vishal R")
    rider.createRide(1, 10, 20, 2)
    is_withdrawn, reason =  rider.withdrawRide(1)
    assert is_withdrawn == True
    is_updated, reason =  rider.updateRide(2, 30, 50, 3)
    assert is_updated == False
    assert reason == "Cannot update ride for cancelled ride."

def test_cant_close_withdrawn_ride():
    rider = Rider("Vishal R")
    is_created, reason = rider.createRide(1, 10, 20, 2)
    is_withdrawn, reason =  rider.withdrawRide(1)
    assert is_withdrawn == True
    calculated_fare, reason = rider.closeRide()
    assert calculated_fare == 0
    assert reason == "Ride wasn't in progress. Can't close."

def test_cant_close_ride_without_creating_ride():
    rider = Rider("Vishal R")
    calculated_fare, reason = rider.closeRide()
    assert calculated_fare == 0
    assert reason == "No ride active for Rider."
