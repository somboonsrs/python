#OOP in Python  Classes, inheritance, polymorphism

#OOP in Python  Classes, inheritance, polymorphism

# สร้าง class
class Person:
    # __init__ = constructor (เหมือน func NewPerson() ใน Go)
    def __init__(self, name, age,gender="Male"):
        self.name = name    # self = ตัวเอง (เหมือน this ใน Java)
        self.age = age
        self.gender=gender
    
    # method
    def greet(self):
        print(f"Hello, I'm {self.name}, {self.age} years old and gender is {self.gender}")
    
    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday! Now I'm {self.age}")
        
    def my_company(self,company):
        self.age += 1
        print(f"my name :{self.name} and company name is {company}")

# สร้าง object
person1 = Person("Sombo", 25,"Femail")
person2 = Person("Alice", 30)

# เรียก method
person1.greet()           # → Hello, I'm Sombo, 25 years old
person2.greet()           # → Hello, I'm Alice, 30 years old

# เข้าถึง attribute
print(person1.name)       # → Sombo
print(person1.age)        # → 25

# เรียก method ที่เปลี่ยนค่า
person1.have_birthday()   # → Happy birthday! Now I'm 26
person1.my_company("KKP")



# สร้าง class Employee ที่มี:

# Attributes:
# - name (บังคับ)
# - position (บังคับ)
# - salary (บังคับ)
# - department (default = "General")

# Methods:
# - get_info() → return string "Name (Position) - Department"
# - get_annual_salary() → return salary * 12
# - give_raise(percent) → เพิ่มเงินเดือนตาม % แล้ว print เงินเดือนใหม่

# ตัวอย่างการใช้งาน:
# emp1 = Employee("Sombo", "Developer", 45000, "IT")
# emp2 = Employee("Alice", "Manager", 65000)
#
# print(emp1.get_info())           # → Sombo (Developer) - IT
# print(emp2.get_info())           # → Alice (Manager) - General
# print(emp1.get_annual_salary())  # → 540000
# emp1.give_raise(10)              # → New salary: 49,500

class Employee:
    
    
    def __init__(self,name,position,salary,department="General"):
        self.name=name
        self.position=position
        self.salary=salary
        self.department=department

    
    def get_info(self):
        return (f"{self.name} ({self.position}) - {self.department}")
    
    def get_annual_salary(self):
        return self.salary*12
    
    def give_raise(self,percent):
        self.salary=(self.salary*(percent/100))+self.salary
        print(f"New salary: {self.salary:,.0f}")
    

emp1 = Employee("Sombo", "Developer", 45000, "IT")
emp2 = Employee("Alice", "Manager", 65000)
    
print(emp1.get_info())           # → Sombo (Developer) - IT
print(emp2.get_info())           # → Alice (Manager) - General
print(emp1.get_annual_salary())  # → 540000
emp1.give_raise(10)              # → New salary: 49,500
print(emp1.salary)
print(emp2.salary)


# Parent class (class แม่)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")
    
    def eat(self):
        print(f"{self.name} is eating")

# Child class (class ลูก) — สืบทอดจาก Animal
class Dog(Animal):    # ← ใส่ชื่อ parent ในวงเล็บ
    def speak(self):  # ← Override method ของ parent
        print(f"{self.name} says: Woof!")
    
    def fetch(self):  # ← เพิ่ม method ใหม่
        print(f"{self.name} is fetching the ball")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")
    
    def scratch(self):
        print(f"{self.name} is scratching")

# ใช้งาน
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()     # → Buddy says: Woof! (ใช้ method ของ Dog)
dog.eat()       # → Buddy is eating (ได้มาจาก Animal)
dog.fetch()     # → Buddy is fetching the ball

cat.speak()     # → Whiskers says: Meow!
cat.eat()       # → Whiskers is eating
cat.scratch()   # → Whiskers is scratching


# Parent class: Product
# - Attributes: name, price
# - Methods: 
#   - get_info() → "Name - Price THB"
#   - get_discounted_price(percent) → คำนวณราคาหลังลด

# Child class: Electronics (สืบทอดจาก Product)
# - เพิ่ม Attribute: warranty_years
# - Override get_info() → เพิ่มข้อมูล warranty

# Child class: Food (สืบทอดจาก Product)
# - เพิ่ม Attribute: expiry_date
# - Override get_info() → เพิ่มข้อมูล expiry
# - เพิ่ม Method: is_expired(today) → เช็คว่าหมดอายุหรือยัง

# ตัวอย่างการใช้งาน:
# phone = Electronics("iPhone", 32900, 2)
# milk = Food("Milk", 45, "2025-01-10")
#
# print(phone.get_info())                    # → iPhone - 32,900 THB (Warranty: 2 years)
# print(phone.get_discounted_price(10))      # → 29610.0
#
# print(milk.get_info())                     # → Milk - 45 THB (Expiry: 2025-01-10)
# print(milk.is_expired("2025-01-15"))       # → True

class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_info(self):
        return f"{self.name} - {self.price} THB"
    
    def get_discounted_price(self,percent):
        return self.price-(self.price*(percent/100))
    
class Electronics(Product):
    
    def __init__(self, name, price,warranty_years):
        super().__init__(name, price) 
        self.warranty_years = warranty_years
        
    def get_info(self):
        return f"{self.name} - {self.price:,.0f} THB - (Warranty: {self.warranty_years} years)"

class Food(Product):
    
    def __init__(self, name, price,expiry_date):
        super().__init__(name, price) 
        self.expiry_date = expiry_date
        
    def get_info(self):
        return f"{self.name} - {self.price:,.0f} THB - (Expiry date : {self.expiry_date})"

    def is_expired(self,today):
        return self.expiry_date < today

phone = Electronics("iPhone", 32900, 2)
milk = Food("Milk", 45, "2027-01-10")

print(phone.get_info())                          # → iPhone - 32,900 THB (Warranty: 2 years)
print(phone.get_discounted_price(10))       # → 29610.0

print(milk.get_info())                            # → Milk - 45 THB (Expiry: 2025-01-10)
print(milk.is_expired("2025-01-15"))        # → True


# ไม่มี __str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Sombo", 25)
print(person)    # → <__main__.Person object at 0x...> (อ่านไม่รู้เรื่อง!)

# มี __str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):    # ← สำหรับ print() แสดงผลให้ user
        return f"Person: {self.name}, {self.age} years old"
    
    def __repr__(self):   # ← สำหรับ debug แสดงผลให้ developer
        return f"Person('{self.name}', {self.age})"

person = Person("Sombo", 25)
print(person)        # → Person: Sombo, 25 years old (ใช้ __str__)
print(repr(person))  # → Person('Sombo', 25) (ใช้ __repr__)


# Requirements
# สร้างระบบจัดการสินค้าที่:
# Product class — base class
# Electronics, Food class — inherit จาก Product
# Inventory class — จัดการ products ทั้งหมด
# บันทึก/โหลดข้อมูลจาก JSON file
# CLI Menu — เพิ่ม, ดู, ค้นหา, ลบ สินค้า

# product_system/
# ├── main.py              # CLI menu
# ├── models/
# │   ├── __init__.py
# │   ├── product.py       # Product, Electronics, Food
# │   └── inventory.py     # Inventory class
# └── data/from models.inventory import Inventory

from models.inventory import Inventory
from models.product import Product, Electronics, Food

DATA_FILE = "data/products.json"

def show_menu():
    print("\n===== Product Management =====")
    print("1. Show all products")
    print("2. Add product")
    print("3. Search product")
    print("4. Remove product")
    print("5. Save & Exit")
    print("==============================")

def main():
    inventory = Inventory()
    inventory.load_from_file(DATA_FILE)
    
    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            # TODO: แสดงสินค้าทั้งหมด
            pass
        elif choice == "2":
            # TODO: เพิ่มสินค้า (ถามประเภท, ชื่อ, ราคา, จำนวน, etc.)
            pass
        elif choice == "3":
            # TODO: ค้นหาสินค้า
            pass
        elif choice == "4":
            # TODO: ลบสินค้า
            pass
        elif choice == "5":
            # TODO: บันทึกและออก
            pass
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
#     └── products.json    # เก็บข้อมูล


