import json
from pathlib import Path
from .product import Product, Electronics, Food


class Inventory:
    def __init__(self):
        self.products = []
    
    def __len__(self):
        return len(self.products)
    
    def __getitem__(self, index):
        return self.products[index]
    
    def add_product(self, product):
        """เพิ่มสินค้า"""
        self.products.append(product)
        print(f"Added: {product.name}")
    
    def find_by_id(self, id):
        """หาสินค้าจาก ID"""
        for p in self.products:
            if p.id == id:
                return p
        return None
    
    def search_by_name(self, keyword):
        """ค้นหาสินค้าจากชื่อ"""
        return [p for p in self.products if keyword.lower() in p.name.lower()]
    
    def remove_product(self, id):
        """ลบสินค้า"""
        product = self.find_by_id(id)
        if product:
            self.products.remove(product)
            print(f"Removed: {product.name}")
            return True
        print(f"Product ID '{id}' not found")
        return False
    
    def get_total_value(self):
        """มูลค่าสินค้าทั้งหมด"""
        return sum(p.get_total_value() for p in self.products)
    
    def show_all(self):
        """แสดงสินค้าทั้งหมด"""
        if not self.products:
            print("No products in inventory")
            return
        print(f"\n{'='*60}")
        print(f"{'INVENTORY':^60}")
        print(f"{'='*60}")
        for p in self.products:
            print(p)
        print(f"{'='*60}")
        print(f"Total items: {len(self)} | Total value: {self.get_total_value():,} THB")
    
    def save_to_file(self, filepath):
        """บันทึกลง JSON file"""
        data = [p.to_dict() for p in self.products]
        Path(filepath).parent.mkdir(exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(self)} products to {filepath}")
    
    def load_from_file(self, filepath):
        """โหลดจาก JSON file"""
        if not Path(filepath).exists():
            print(f"File not found: {filepath}")
            return
        
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.products = []
        for item in data:
            if item["type"] == "Electronics":
                self.products.append(Electronics.from_dict(item))
            elif item["type"] == "Food":
                self.products.append(Food.from_dict(item))
            else:
                self.products.append(Product.from_dict(item))
        
        print(f"Loaded {len(self)} products from {filepath}")
        print(f"products :{self.products}")