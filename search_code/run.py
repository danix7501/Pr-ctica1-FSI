# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
og = search.GPSProblem('O', 'G', search.romania)

print "Recorrido de A a B"

print "Breadth First"
print search.breadth_first_graph_search(ab).path()

print "Depth First"
print search.depth_first_graph_search(ab).path()

print "Branch and Bound"
print search.branch_and_bound_search(ab).path()

print "Branch and Bound Heuristic"
print search.branch_and_bound_heuristic_search(og).path()

print "-------------------------------------------------------------------"

print "Recorrido de O a G"

print "Breadth First"
print search.breadth_first_graph_search(og).path()

print "Depth First"
print search.depth_first_graph_search(og).path()

print "Branch and Bound"
print search.branch_and_bound_search(og).path()

print "Branch and Bound Heuristic"
print search.branch_and_bound_heuristic_search(og).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
