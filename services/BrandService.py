from entities.Brand import Brand


class BrandService:
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

        print("\nSe generó listado de marcas.")
        return list_by_brand

    def find_product(self, list_by_brand, item):
        res = None
        for element in list_by_brand:
            if element.brand_name == item:
                res = element
        return res

    def show_brands(self, list_brands):
        print("\n---LISTADO DE MARCAS---")
        for brand in list_brands:
            print(brand.get_info())

    def show_brand_average(self, list_brands):
        print("\n---LISTADO DE MARCAS Y PROMEDIOS---")
        for brand in list_brands:
            print(f"Marca: {brand.brand_name}  -  Precio Promedio: {round(brand.average)}")
