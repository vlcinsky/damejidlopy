class Customer:
	"""Class which stores information about customer
	Arguments:
		name(str): Name of the customer,
		surname(str): Surname of customer,
		email(str): Email of customer,
		address(str): Address of customer

	"""
	def __init__(self, name, surname, email, address):
		"""Gets information using arguments and then prints it"""
		self.name = name
		self.surname = surname
		self.email = email
		self.address = address
		print(f"Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Address: {self.address}")
