class Client:
    def __init__(self, name, phone, date_of_birth):
        self.name = name
        self.phone = phone
        self.date_of_birth = date_of_birth

        def __str__(self):
            return f"Name: {self.name} | Phone: {self.phone} | Date of Birth: {self.date_of_birth}"