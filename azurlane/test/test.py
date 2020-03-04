import azurapi as api

azurapi = api.AzurAPI()

# try:
# 	# print(azurapi.get_ship_by_id("077"))
# 	# print(azurapi.get_ship_by_id("999"))
# 	# print(azurapi.get_ship_by_name("エンタープライズ"))
# 	print(azurapi.get_ship("Enterprise"))
# except (ValueError, api.exceptions.UnknownShipException) as e:
# 	print(f"{type(e).__name__}: {e}")
 

# A pointless way of using this feature but ey... I needed to test it somehow
enterprise = [ship for ship in azurapi.get_all_ships_by_en_names() if ship.get("id") == "077"]
if len(enterprise) < 1:
	print("not found") # happens if the name of the ship is not available in that language
else:
	enterprise = enterprise[0]