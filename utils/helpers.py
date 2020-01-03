def is_str_int(input):
	try:
		int(input)
		return True
	except ValueError:
		return False