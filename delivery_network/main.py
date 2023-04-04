from graph import Graph, trucks_from_file_list, truck_choice, naive_algorithm, max_profit

camion = trucks_from_file_list(1)
#print('camion', camion)
camiontrie= sorted_trucks(camion)
#print('camiontrie', camiontrie)
choisi= choose_truck(2800000, camiontrie)
print(choisi)

'''camions = [(2000, 5), (1000, 3), (3000, 4), (4000, 7)]
liste_camions = sorted_trucks(camions)
print(liste_camions)

routes1 = [(None, 4, 1500), (None, 5, 1200),(None, 19, 3500)]
attrib1 = naive_algorithm(routes1, liste_camions, 10) 
print(attrib1)
routes2 = [(None, 19, 3500), (None, 4, 1500), (None, 5, 1500)]
attrib2 = naive_algorithm(routes2, liste_camions, 10) 
print(attrib2)
'''



