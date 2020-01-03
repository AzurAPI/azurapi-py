import azurapi as api

azurapi = api.AzurAPI()

try:
	# print(azurapi.get_ship_by_id("077"))
	# print(azurapi.get_ship_by_id("999"))
	# print(azurapi.get_ship_by_name("エンタープライズ"))
	print(azurapi.get_ship("Enterprise"))
except (ValueError, api.exceptions.UnknownShipException) as e:
	print(f"{type(e).__name__}: {e}")