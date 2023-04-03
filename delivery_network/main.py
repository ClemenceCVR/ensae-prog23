from graph import Graph, trucks_from_file_list, sorted_trucks, choose_truck

camion = trucks_from_file_list(1)
#print('camion', camion)
camiontrie= sorted_trucks(camion)
#print('camiontrie', camiontrie)
choisi= choose_truck(2800000, camiontrie)
print(choisi)




