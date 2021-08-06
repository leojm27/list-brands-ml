import requests
from entities.Product import Product
from entities.Brand import Brand


class ProductService:

    def get_api_request(self):
        list_product = []
        resp = requests.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA1763')
        data = resp.json()
        results = data['results']
        paging = data['paging']

        for item in results:
            product = self.product_json(item)
            list_product.append(product)

        self.list_brands(list_product)

        # print("\nPAGING: ")
        # print(paging)

    def product_json(self, item):
        product_attributes = self.find_condition_brand(item['attributes'])
        product = Product(
            item['id'],
            item['title'],
            item['price'],
            product_attributes['condition'],
            product_attributes['brand']
        )
        return product

    def find_condition_brand(self, attributes):
        brand = None
        condition = None
        for attribute in attributes:
            if 'ITEM_CONDITION' == attribute['id']:
                condition = attribute['value_name']

            if 'BRAND' == attribute['id']:
                brand = attribute['value_name']

        product_attributes = {"condition": condition, "brand": brand}
        return product_attributes

    def find_product(self, list_by_brand, item):
        res = None
        for element in list_by_brand:
            if element.brand_name == item:
                res = element
        return res

    def list_brands(self, list_product):
        list_by_brand = []
        for product in list_product:
            if 'Nuevo' == product.condition:
                brand_temp = self.find_product(list_by_brand, product.brand)

                if brand_temp is not None:
                    # print("Elemento existente. Se actualiza campo 'total_price', 'quantity' y 'average'")
                    brand_temp: Brand
                    index = list_by_brand.index(brand_temp)
                    list_by_brand[index].total_price += product.price
                    list_by_brand[index].quantity += 1
                    list_by_brand[index].average = list_by_brand[index].total_price / list_by_brand[index].quantity
                else:
                    # print("Se añadio elemento a la lista")
                    brand = Brand(product.brand, product.price, 1)
                    list_by_brand.append(brand)

        print("---LISTADO DE MARCAS---")
        for brand in list_by_brand:
            # print(f"Marca: {brand.brand_name} - Promedio: {brand.average} - Total: {brand.total_price} - Q:
            # {brand.quantity}")
            print(f"Marca: {brand.brand_name} - Precio Promedio: {brand.average}")
