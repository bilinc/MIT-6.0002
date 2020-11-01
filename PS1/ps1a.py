###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Bilin Chen
# Collaborators: None
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
	"""
	Read the contents of the given file.  Assumes the file contents contain
	data in the form of comma-separated cow name, weight pairs, and return a
	dictionary containing cow names as keys and corresponding weights as values.

	Parameters:
	filename - the name of the data file as a string

	Returns:
	a dictionary of cow name (string), weight (int) pairs
	"""
	# TODO: Your code here
	f = open(filename, 'r')	# open file in read-only

	cows = {}
	for line in f:
		
		# Remove linebreak and split string at the comma
		line = line.strip('\n').split(',')
		
		cows[line[0]] = int(line[1])

	return cows

# Load cow data
cows = load_cows('ps1_cow_data.txt')

# Problem 2
def greedy_cow_transport(cows,limit=10):
	"""
	Uses a greedy heuristic to determine an allocation of cows that attempts to
	minimize the number of spaceship trips needed to transport all the cows. The
	returned allocation of cows may or may not be optimal.
	The greedy heuristic should follow the following method:

	1. As long as the current trip can fit another cow, add the largest cow that will fit
		to the trip
	2. Once the trip is full, begin a new trip to transport the remaining cows

	Does not mutate the given dictionary of cows.

	Parameters:
	cows - a dictionary of name (string), weight (int) pairs
	limit - weight limit of the spaceship (an int)
	
	Returns:
	A list of lists, with each inner list containing the names of cows
	transported on a particular trip and the overall list containing all the
	trips
	"""
	# TODO: Your code here
	# a transport contains multiple trips
	transport = []
	# a trip contains some cows
	trip = []

	available = limit

	# becomes a sorted list of the keys based on their values
	cows_sorted = sorted(cows, key=cows.get, reverse=True)
	cows_copy = cows_sorted.copy()

	# cows is a dict, by iterating through its objects it automatically does so with the keys
	while len(cows_sorted) > 0:
		for cow in cows_sorted:
			
			if cows[cow] <= available:
				trip.append(cow)
				# remove the weight of the cow from the available weight
				available -= cows[cow]
				# remove the cow from the list

		# How to make this a one-liner?
		for cow in trip:
			cows_sorted.remove(cow)
			
		transport.append(trip)
		trip = []
		available = limit

	# print(cows)
	# print(cows_copy)
	print(transport)

greedy_cow_transport(cows)


# Problem 3
def brute_force_cow_transport(cows,limit=10):
	"""
	Finds the allocation of cows that minimizes the number of spaceship trips
	via brute force.  The brute force algorithm should follow the following method:

	1. Enumerate all possible ways that the cows can be divided into separate trips 
		Use the given get_partitions function in ps1_partition.py to help you!
	2. Select the allocation that minimizes the number of trips without making any trip
		that does not obey the weight limitation
			
	Does not mutate the given dictionary of cows.

	Parameters:
	cows - a dictionary of name (string), weight (int) pairs
	limit - weight limit of the spaceship (an int)
	
	Returns:
	A list of lists, with each inner list containing the names of cows
	transported on a particular trip and the overall list containing all the
	trips
	"""
	# TODO: Your code here
	cows_sorted = sorted(cows, key=cows.get, reverse=True)
	
	# A generator object containing a list of lists
	cow_partitions = get_partitions(cows)
	
	best_alloc = []
	
	# parition is one list of lists from the generator
	for partition in cow_partitions:
		# loop through every trip (list) in the partition (list of lists)
		for trip in partition:
			trip_weight = 0
			# looping through each cow in the trip
			for i in range(len(trip)):
				# combining all the cow weights in a trip
				trip_weight += cows[trip[i]]
			# checking if the trip weight is outside of limit
			if trip_weight > limit:
				# exit this partition as it contains a trip outside the limit
				break
		
		if trip_weight > limit:
			continue
		# save the partition with all valid trips and choose the one that minimizes the amount of trips
		
		if len(best_alloc) == 0:
			best_alloc = partition
		else:
			if len(best_alloc) > len(partition):
				best_alloc = partition
		
	print(best_alloc)			
	
brute_force_cow_transport(cows)			

#partition = get_partitions(cows)
#
#print(next(partition))
#print(next(partition))
#print(next(partition))

	
# Problem 4
def compare_cow_transport_algorithms():
	"""
	Using the data from ps1_cow_data.txt and the specified weight limit, run your
	greedy_cow_transport and brute_force_cow_transport functions here. Use the
	default weight limits of 10 for both greedy_cow_transport and
	brute_force_cow_transport.
	
	Print out the number of trips returned by each method, and how long each
	method takes to run in seconds.

	Returns:
	Does not return anything.
	"""
	# TODO: Your code here
	pass
