def universal_plant(plant_name):
	if can_harvest():#harvest without errors
		harvest()
	if get_ground_type() != Grounds.Soil:#till for palnt
		till()
	plant(plant_name)
	if num_items(Items.Water) > 1:#do not use water if don't have
		if get_water() < 0.5:
			use_item(Items.Water)
