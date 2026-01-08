# 1. ตัวแปร products เก็บ list ของสินค้า
# products = [
#     {"id": 1, "name": "iPhone", "price": 32900},
#     {"id": 2, "name": "AirPods", "price": 6900},
#     {"id": 3, "name": "iPad", "price": 19900},
# ]

# 2. function get_all_products() — return products ทั้งหมด

# 3. function get_product_by_id(id) — return product ที่ตรงกับ id หรือ None

# 4. function get_expensive_products(min_price) — return products ที่ราคา >= min_price

products  = [
    {"id": 1, "name": "iPhone", "price": 32900},
    {"id": 2, "name": "AirPods", "price": 6900},
    {"id": 3, "name": "iPad", "price": 19900},
]

def get_all_products():
    return products
    
    
def get_product_by_id(id):
    return next((p for p in products if p["id"]==id),None)
    
def get_expensive_products(min_price):
    return [p for p in products if p["price"]>=min_price]
    
    
