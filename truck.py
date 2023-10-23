from hashtable import HashTable

#Class for the Truck object to keep track of the driver, max packages, average speed, minutes traveled, and hash table of packages on the truck
class Truck:
    def __init__(self, truck_id, driver, max_packages=16, avg_speed=18, minutes_traveled=0):
        self.truck_id = truck_id
        self.driver = driver
        self.max_packages = max_packages
        self.avg_speed = avg_speed
        self.minutes_traveled = minutes_traveled
        self.packages = HashTable(20)

    def add_package_to_truck(self, package):
        # Use the package_id as the key and the package object as the value.
        self.packages.set(package.package_id, package)
