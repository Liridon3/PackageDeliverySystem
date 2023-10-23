from datetime import datetime

# Create class for the Package object. The object will be saved to the Hash Table using the package_id as the key
class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight, notes, delivery_status="At The Hub"):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        # Parse the deadline time
        if deadline == "EOD":
            self.deadline = datetime.strptime("5:00 PM", "%I:%M %p")
        else:
            self.deadline = datetime.strptime(deadline, "%I:%M %p")
        self.weight = weight
        self.notes = notes
        self.delivery_status = delivery_status

    # define the __hash__() method - returns the hash of the package_id
    def __hash__(self):
        return hash(self.package_id)

    # define the __eq__() method - checks if two objects are equal based on package_id
    def __eq__(self, other):
        if isinstance(other, Package):
            return self.package_id == other.package_id
        return False
