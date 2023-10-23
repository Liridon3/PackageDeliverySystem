# 010722931
import csv

from hashtable import HashTable
from package import Package
from truck import Truck

# set global variable for the maximum travel distance allowed and the number of packages that need to be delivered
max_mileage = 140
goal_packages_delivered = 40

# create hashtable for storing the distance between addresses. Create it with 702 records so that the table is O(1)
distanceDataTable = HashTable(702)

# create hashtable for storing the packages. Since it is known that there are 40 packages, the table will be created
# with 40 records so that it's O(1)
packageDataTable = HashTable(40)

# Instantiate the three trucks. Assign the two drivers to truck 1 and truck 2
truck1 = Truck(1, "A")
truck2 = Truck(2, "B")
truck3 = Truck(3, None)

# Read data from the CSV file
with open('Distance.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header

    for row in csv_reader:
        Address1, City1, State1, Zip1, Address2, City2, State2, Zip2, distance = row
        composite_key = Address1 + "," + City1 + "," + State1 + "," + Zip1 + "," + Address2 + "," + City2 + "," + State2 + "," + Zip2  # create composite key to use as key for hashtable
        distance = float(distance)  # Convert distance to a float
        distanceDataTable.set(composite_key,
                              distance)  # Store the distance in the hash table using the composite key

# Read data from the package CSV file
with open('packages.csv', 'r') as csv_file_packages:
    csv_reader_packages = csv.reader(csv_file_packages)
    next(csv_reader_packages)  # Skip the header

    for row in csv_reader_packages:
        ID, Address, City, State, Zip, Deadline, Weight, notes = row
        key = ID
        value = Package(ID, Address, City, State, Zip, Deadline, Weight, notes)
        packageDataTable.set(key, value)  # Store the id as the key and the package object as the value


