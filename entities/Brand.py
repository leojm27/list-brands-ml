class Brand:

    def __init__(self, brand_name, total_price, quantity):
        self.brand_name = brand_name
        self.total_price = total_price
        self.quantity = quantity
        self.average = total_price

    def get_info(self):
        info = "---Brand---"
        info += f"\nName: {self.brand_name}"
        info += f"\nTotal_price: {self.total_price}"
        info += f"\nQuantity: {self.quantity}"
        info += f"\nAverage: {self.average}"

        return info
