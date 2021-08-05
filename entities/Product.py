class Product:

    def __init__(self, id_product, title, price, condition, brand):
        self.id_product = id_product
        self.title = title
        self.price = price
        self.condition = condition
        self.brand = brand

    def get_info(self):
        info = "---Product---"
        info += f"\nID: {self.id_product}"
        info += f"\nTitle: {self.title}"
        info += f"\nPrice: {self.price}"
        info += f"\nCondition: {self.condition}"
        info += f"\nBrand: {self.brand}"

        return info
