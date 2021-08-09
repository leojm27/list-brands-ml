class Brand:

    def __init__(self, brand_name, total_price, quantity):
        self.brand_name = brand_name
        self.total_price = total_price
        self.quantity = quantity
        self.average = total_price

    def get_info(self):
        info = ""
        info += f"Name: {self.brand_name}"
        info += f" - Total_price: {self.total_price}"
        info += f" - Quantity: {self.quantity}"
        info += f" - Average: {self.average}"

        return info
