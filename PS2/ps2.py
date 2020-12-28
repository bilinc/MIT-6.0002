# 6.0002 Problem Set 5
# Graph optimization
# Name: Bilin Chen
# Collaborators: None
# Date: 2020-11-11

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer: The nodes represent the buildings and locations. The edges are the roads connecting the buildings and the distances is
# represented by the weight or cost.
#


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """

    # TODO
    print("Loading map from file...")
    
    f = open(map_filename, 'r')

    mit_digraph = Digraph()

    for line in f:
        # create a list of the numbers by splitting at the blank space
        values = line.split()

        # add the nodes to the digraph
        try:
            mit_digraph.add_node(values[0])
        except ValueError:
            # value error will be raised if the node already exists, so just do
            pass

        try:
            mit_digraph.add_node(values[1])
        except ValueError:
            # value error will be raised if the node already exists, so just do
            pass
            

        # created the weighted edge
        w_edge = WeightedEdge(values[0], values[1], values[2], values[3])

        # add weighted edge to digraph
        mit_digraph.add_edge(w_edge)
    
    return mit_digraph



# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out
test_map = load_map("test_load_map.txt")
'''
print('Test 1: The connected nodes and edges')
print(test_map)

print('Test 2: All the nodes')
print(test_map.nodes)

print('Test 3: All the edges')
print(test_map.edges)
'''

#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer:
# To minimize the total distance traveled

# Constraints:
# Cannot exceed maximum distance outdoors.


# My helper function for problem 3b
def printPath(path):
    """
    Assumes path is a list of nodes
    """
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path, toPrint = False):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. 
            Contains a list of node names, total distance traveled, and total distance outdoors.
        max_dist_outdoors: int (*constant)
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    # TODO
    # Creating global variable to keep track of the best distance over all local frames
    global shortest_dist
    shortest_dist = best_dist

    path_copy = path.copy()    

#    path[0]        the current path of nodes being traversed
#    path[1]        total distance traveled so far
#    path[2]        total distance ourdoors so far
    
    
    path_copy[0] = path_copy[0] + [start]
    
    if toPrint:
        print('Current DFS path:', printPath(path_copy[0]))
    
    # if start and end are not valid nodes:
    #       raise an error
    if not(digraph.has_node(start)) or not(digraph.has_node(end)):
        raise ValueError("Nodes does not exist in the graph!")
    
    elif start == end:
        if shortest_dist == None or path_copy[1] < shortest_dist:
            shortest_dist = path_copy[1]

        return tuple(path_copy[0])
    # else:
    #       for all the child nodes of start
    #           construct a path including that node
    #           recursively solve the rest of the path, from the child node to the end node
    
    # loop over all edges I can reach
    
    # Problem: does not reset properly after going up
    # does not reset distance, does not check for shortest distance
    for child_node in digraph.get_edges_for_node(start): # list containing WeightedEdge objects
        
#        print('Child node: ', child_node)
#        print('Source: ', child_node.src, 'Destination: ', child_node.dest)
        
        if child_node.dest not in path_copy[0]:  # avoid cycles
            path_copy[1] = path[1] + int(child_node.get_total_distance())
            path_copy[2] = path[2] + int(child_node.get_outdoor_distance())
            
            # if the outdoor contstraint is broken, return None path
            if path_copy[2] > max_dist_outdoors:
                return None
            
            # if a path is longer than the shortest path found so far, then you don't have to go further
            if shortest_dist != None and path_copy[1] > shortest_dist:
                break
            
            # Not checking the most optimal travelled distance correctly
            
            # If we don't have a solution or if we have a better solution than the currently best one
            if best_path == None or best_dist == None or path_copy[1] < shortest_dist: #len(path[0]) < len(best_path):
                
                # start to recursively find paths
                new_path = get_best_path(digraph, child_node.dest, end, path_copy, max_dist_outdoors, 
	                                             shortest_dist, best_path, toPrint = True)

                if new_path != None:
                    # need to find the shortest path and also least distance  
                    best_path = new_path
                    
            elif toPrint:
                print('Already visited', child_node.dest)
    
    return tuple(best_path)



print("---------Problem 3b: Implement get_best_path---------")
print("Test 1")
def shortest_path(graph, start, end, toPrint = False):
    return get_best_path(graph, start, end, [[], 0, 0], 3, None, None, toPrint)

def test_sp(graph, source, destination):
    sp = shortest_path(graph, graph.get_node(source), graph.get_node(destination), toPrint = True)
    
    if sp != None:
        print('Shortest path from', source, 'to', destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)
        
test_sp(test_map, 'a', 'c')



# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    # TODO
    shortest_path = get_best_path(digraph, start, end, [[], 0, 0], max_dist_outdoors, None, None, toPrint=True)
    
    if shortest_path == None:
        raise ValueError("No shortest path found following the constraints")
    else:
        return list(shortest_path)
    

# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
#
#    def test_path_one_step(self):
#        self._test_path(expectedPath=['32', '56'])
#
#    def test_path_no_outdoors(self):
#        self._test_path(
#            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)
#
#    def test_path_multi_step(self):
#        self._test_path(expectedPath=['2', '3', '7', '9'])
#
#    def test_path_multi_step_no_outdoors(self):
#        self._test_path(
#            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)
#
#    def test_path_multi_step2(self):
#        self._test_path(expectedPath=['1', '4', '12', '32'])
#
#    def test_path_multi_step_no_outdoors2(self):
#        self._test_path(
#            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
#            outdoor_dist=0)
#
#    def test_impossible_path1(self):
#        self._test_impossible_path('8', '50', outdoor_dist=0)
#
#    def test_impossible_path2(self):
#        self._test_impossible_path('10', '32', total_dist=100)


if __name__ == "__main__":
    unittest.main()
