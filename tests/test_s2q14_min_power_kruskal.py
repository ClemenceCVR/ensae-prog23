import sys 
sys.path.append("delivery_network")
from graph import Graph, UnionFind, graph_from_file, kruskal, min_power_kruskal, oriented_tree
import time


g=Graph([1,2,3,4,5,6])
g.add_edge(1, 2, 3)
g.add_edge(2, 3, 4)
g.add_edge(1, 3, 4)
g.add_edge(1, 6, 7)
g.add_edge(3, 6, 1)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 9)
g.add_edge(4, 5, 5)

g1 = kruskal(g)
t_dep = time.perf_counter()
h = oriented_tree(g1)
min_pwg, traj_g = min_power_kruskal(g1, h, 4, 2)
t_fin = time.perf_counter()
t = t_fin-t_dep

print("Pour le petit graphe, la puissance minimale pour ce trajet est ", min_pwg,"et on passe par le chemin " , traj_g, "et le temps nécessaire est ", t , "sec")

# C'est bien cohérent avec l'arbre de poids couvrant donné


# Test sur les grands graphes: 
g = graph_from_file("input/network.2.in")
g2 = kruskal(g)
t_dep = time.perf_counter()
h=oriented_tree(g2)
min_pwg, traj_g = min_power_kruskal(g2, h, 1000, 30)
t_fin = time.perf_counter()
t = t_fin-t_dep
print("Pour le grand graphe, la puissance minimale pour ce trajet est ", min_pwg,"et on passe par le chemin " , traj_g, "et le temps nécessaire est ", t , "sec")


#le temps d'éxecution est raisonnable pour la version optimisée de max power kruskal