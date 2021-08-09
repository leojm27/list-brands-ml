from services.ProductService import ProductService
from services.BrandService import BrandService

productService = ProductService()
brandService = BrandService()


class BrandController:
    def get_list_brands(self):
        list_products = productService.get_list_products()
        list_brands = brandService.list_brands(list_products)
        return list_brands

    def show_brand_average(self, list_brands):
        brandService.show_brand_average(list_brands)

    def show_brands(self, list_brands):
        brandService.show_brands(list_brands)
