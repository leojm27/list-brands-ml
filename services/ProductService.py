import concurrent.futures
import requests
import time

from models.Product import Product


class ProductService:
    def get_list_products(self):
        start = time.perf_counter()
        list_product = []
        url = "https://api.mercadolibre.com/sites/MLA/search"
        limit = 900
        category = "MLA1763"
        offset = 0
        list_query = self.get_list_query(url, offset, limit, category)

        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(self.get_api_request, list_query)
            for result in results:
                list_product += result

        count_products = len(list_product)
        finish = time.perf_counter()
        print("\nSe generó listado de productos.")
        print(f"\nCantidad de registros de motos: {count_products}")
        print(f"Tiempo de ejecucion de peticiones: {round(finish - start, 2)} segundos")
        return list_product

    def get_list_query(self, url, offset, limit, category):
        list_query = []
        while offset < limit:
            query = f"{url}?category={category}&offset={offset}"
            list_query.append(query)
            offset += 50
        return list_query

    def get_api_request(self, query):
        results = None
        list_product = []
        try:
            resp = requests.get(query)
            data = resp.json()
            results = data['results']
            # print(f"Petición satisfactoria.")
        except Exception as e:
            print(f"Error en la Petición: {e}")

        if results is not None:
            for item in results:
                product = self.get_product_instance(item)
                list_product.append(product)

        return list_product

    def get_product_instance(self, item):
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

    def show_products(self, list_products):
        print("\n---LISTADO DE MOTOS---")
        for product in list_products:
            print(product.get_info())

