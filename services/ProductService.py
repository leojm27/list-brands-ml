import requests
from entities.Product import Product


class ProductService:

    def api_request(self):
        list_product = []
        list_by_brand = []
        resp = requests.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA1763')
        data = resp.json()
        results = data['results']
        paging = data['paging']

        print("RESULTS: ")
        for item in results:
            product = self.product_json(item)
            list_product.append(product)

        for element in list_product:
            print(element.get_info())

        print("\nPAGING: ")
        print(paging)

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

        product_attributes = {
            "condition": condition,
            "brand": brand
        }

        return product_attributes
