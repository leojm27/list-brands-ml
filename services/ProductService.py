import requests
import time
from entities.Product import Product
from entities.Brand import Brand


class ProductService:

    def execute_process(self):
        start = time.perf_counter()
        list_product_process = []
        limit = 900
        category = "MLA1763"
        offset = 0

        print("Se realizaran peticiones a la API de MercadoLibre...")
        while offset < limit:
            query = f"https://api.mercadolibre.com/sites/MLA/search?category={category}&offset={offset}"
            list_product_process += self.get_api_request(query)
            offset += 50

        self.list_brands(list_product_process)

        count_products = len(list_product_process)
        finish = time.perf_counter()

        print(f"\nCantidad de registros analizados: {count_products}")
        print(f"Tiempo de ejecucion de proceso: {round(finish - start, 2)} segundos")

    def get_api_request(self, query):
        results = None
        list_product = []
        try:
            resp = requests.get(query)
            data = resp.json()
            results = data['results']
            #print(f"Petición satisfactoria.")
        except Exception as e:
            print(f"Error en la Petición: {e}")

        if results is not None:
            for item in results:
                product = self.product_json(item)
                list_product.append(product)

        return list_product

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

        print("\n---LISTADO DE MARCAS---")
        for brand in list_by_brand:
            # print(f"Marca: {brand.brand_name} - Promedio: {brand.average} - Total: {brand.total_price} - Q:
            # {brand.quantity}")
            print(f"Marca: {brand.brand_name}  -  Precio Promedio: {round(brand.average)}")
