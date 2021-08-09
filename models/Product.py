class Product:

    def __init__(self, id_product, title, price, condition, brand):
        self.id_product = id_product
        self.title = title
        self.price = price
        self.condition = condition
        self.brand = brand

    def get_info(self):
        info = ""
        info += f"ID: {self.id_product}"
        info += f" - Title: {self.title}"
        info += f" - Price: {self.price}"
        info += f" - Condition: {self.condition}"
        info += f" - Brand: {self.brand}"

        return info
