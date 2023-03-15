import sys 
import time
sys.path.append("delivery_network")
from graph import estimated_time_kruskal

print("Le temps nécessaire est :",  estimated_time_kruskal(1), "s") 
print("Le temps nécessaire est :",  estimated_time_kruskal(2), "s") 
print("Le temps nécessaire est :",  estimated_time_kruskal(3), "s") 

#Le temps d'exécution annoncé est très long mais la fonction qui estime la durée s'exécute en moins d'une minute, même pour les grands graphes
