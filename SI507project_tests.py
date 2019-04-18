from SI507project_tools import *

#Test to see if information can be pulled from the 343 Industries API
new_object = get_halo_info("Player")
#print(new_object)

#Test to see if Class instance is constructed correctly
print(Stats(new_object))
