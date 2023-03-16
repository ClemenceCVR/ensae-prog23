import sys 
import time
sys.path.append("delivery_network")
from graph import estimated_time_kruskal


for i in range(1,10):
   print("Le temps nécessaire pour routes.", str(i), ".in est :",  estimated_time_kruskal(i), "s") 

#S'exécute en moins d'une minute
