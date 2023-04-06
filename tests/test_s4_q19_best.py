import sys 
sys.path.append("delivery_network")
from graph import trucks_from_file_list, graph_from_file, kruskal, min_power_kruskal, oriented_tree, profit_best, truck_for_routes, truck_remove

print(profit_best("input/network.1.in", 1, 1))
print(profit_best("input/network.2.in", 2, 2))