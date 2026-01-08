class Product:
    def __init__(self, id, name, price, quantity=0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"[{self.id}] {self.name} - {self.price:,} THB (Stock: {self.quantity})"
    
    def __repr__(self):
        return f"Product('{self.id}', '{self.name}', {self.price}, {self.quantity})"
    
    def get_total_value(self):
        return self.price * self.quantity
    
    def to_dict(self):
        """แปลงเป็น dict สำหรับบันทึก JSON"""
        return {
            "type": "Product",
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
    
    @classmethod
    def from_dict(cls, data):
        """สร้าง object จาก dict"""
        return cls(data["id"], data["name"], data["price"], data["quantity"])


class Electronics(Product):
    def __init__(self, id, name, price, quantity=0, warranty_years=1):
        super().__init__(id, name, price, quantity)
        self.warranty_years = warranty_years
    
    def __str__(self):
        return f"{super().__str__()} [Warranty: {self.warranty_years}y]"
    
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Electronics"
        data["warranty_years"] = self.warranty_years
        return data
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["price"], 
                   data["quantity"], data["warranty_years"])


class Food(Product):
    def __init__(self, id, name, price, quantity=0, expiry_date=""):
        super().__init__(id, name, price, quantity)
        self.expiry_date = expiry_date
    
    def __str__(self):
        return f"{super().__str__()} [Expiry: {self.expiry_date}]"
    
    def is_expired(self, today):
        return self.expiry_date < today
    
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Food"
        data["expiry_date"] = self.expiry_date
        return data
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["price"], 
                   data["quantity"], data["expiry_date"])