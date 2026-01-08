#Python Fundamentals เข้าใจ syntax, data types, control flow

todos = ["Learn Python", "Build API"]
todos.append("Deploy to Cloud")
todos.insert(1,"Setup Database")
print(todos)
todos.remove("Build API")
print(todos)
print(f"Total tasks: {len(todos)}")
if 'Setup Database' in todos:
    print("Found : Setup Database")
if 'Go API' not in todos:
    print("Not found : Go API")
    
print("\n"*2)
##########################################
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])     # → 2,3,4
print(numbers[:3])      # → 0,1,2
print(numbers[7:])      # → 7,8,9
print(numbers[::3])     # → 0,3,6,9
print(numbers[::-1])    # → 9,8,7,6,5,4,3,2,1,0

##########################################
# สร้าง dictionary
person = {
    "name": "Somboon",
    "age": 25,
    "is_developer": True,
    "skills": ["Python", "Go", "Java"]
}

# เข้าถึงค่า
print(person["name"])         # → Somboon
print(person["skills"])       # → ["Python", "Go", "Java"]
print(person["skills"][0])    # → Python

# แก้ไขค่า
person["age"] = 26
print(person["age"])          # → 26

# เพิ่ม key ใหม่
person["city"] = "Bangkok"
person["gender"] = "Male"
print(person.get("salary","XXX"))
print(person)

person = {"name": "Sombo", "age": 25}

# เข้าถึงแบบปลอดภัย (ไม่ error ถ้าไม่มี key)
print(person.get("name"))           # → Sombo
print(person.get("salary"))         # → None
print(person.get("salary", 0))      # → 0 (default value)

# ดู keys, values, items
print(person.keys())                # → dict_keys(['name', 'age'])
print(person.values())              # → dict_values(['Sombo', 25])
print(person.items())               # → dict_items([('name', 'Sombo'), ('age', 25)])

# ลบ key
del person["age"]
print(person)                       # → {'name': 'Sombo'}

# เช็คว่ามี key ไหม
print("name" in person)             # → True
print("age" in person)              # → False

###################################################
#สร้างโปรแกรมเก็บข้อมูล Product:
#สร้าง dict product เก็บข้อมูล:
product = {
    "name" : "iPhone 15",
    "price": 32900,
    "in_stock" : True
}
#เพิ่ม key category เป็น "Electronics"
product["category"]="Electronics"
#เปลี่ยน price เป็น 29900 (ลดราคา!)
product["price"]= 29000
#print ข้อความ: iPhone 15 - Price: 29,900 THB (Electronics)
print(f"{product['name']} - Price: {product['price']:,} THB ({product['category']})")

###################################################
order = {
    "id": "ORD001",
    "customer": {
        "name": "Sombo",
        "email": "sombo@mail.com"
    },
    "items": [
        {"name": "iPhone 15", "price": 29900},
        {"name": "AirPods", "price": 6900},
        {"name": "xxx", "price": 999}
    ],
    "total": 36800
}

# เข้าถึง nested data
print(order["customer"]["name"])     # → Sombo
print(order["items"][0]["name"])     # → iPhone 15
print(order["items"][1]["price"])    # → 6900
print(order["items"][2]["name"])    # → xxx


# ลบ duplicate จาก list
names = ["A", "B", "A", "C", "B"]
unique_names = list(set(names))
print(unique_names)       # → ["A", "B", "C"]

###################################################
dev1_skills = {"Python", "Go", "Java", "SQL"}
dev2_skills = {"Python", "JavaScript", "SQL", "React"}
# 1. หา skill ที่ทั้งคู่มี (intersection)
# Hint: dev1_skills & dev2_skills
# 2. หา skill ทั้งหมดรวมกัน (union)
# Hint: dev1_skills | dev2_skills
# 3. หา skill ที่ dev1 มี แต่ dev2 ไม่มี (difference)
# Hint: dev1_skills - dev2_skills

#print(list(set(list(dev1_skills)+list(dev2_skills))))
#print(list(dev1_skills)+list(dev2_skills))
#print(list(dev1_skills-dev2_skills))
print(dev1_skills&dev2_skills)
print(dev1_skills|dev2_skills)
print(dev1_skills-dev2_skills)
print(dev2_skills-dev1_skills)

###################################################
squares = [i * i for i in range(1, 6)]
print(squares)
products = [
    {"name": "iPhone", "price": 32900, "in_stock": True},
    {"name": "AirPods", "price": 6900, "in_stock": False},
    {"name": "iPad", "price": 19900, "in_stock": True},
    {"name": "MacBook", "price": 45900, "in_stock": False}
]

# 1. ดึงเฉพาะชื่อสินค้า → ["iPhone", "AirPods", "iPad", "MacBook"]
#print([products[i]["name"] for i in range(0,len(products))])
print([ p["name"] for p in products])
# 2. กรองเฉพาะสินค้าที่มีในสต็อก → [{"name": "iPhone", ...}, {"name": "iPad", ...}]
#print([products[i] for i in range(0,len(products)) if products[i]["name"].startswith("iP")])
print([ p for p in products if p["in_stock"]])
# 3. ดึงชื่อสินค้าที่ราคาเกิน 20000 → ["iPhone", "MacBook"]
#print([products[i]["name"] for i in range(0,len(products)) if products[i]["price"]>20000])
print([ p["name"] for p in products if p["price"]>20000])

###################################################
# เขียน if ตรวจสอบ
# ถ้าผ่าน → print "Approved"
# ถ้าไม่ผ่าน → print "Rejected" พร้อมบอกเหตุผล
#   - "Age must be at least 20"
#   - "Salary must be at least 15000"
#   - ถ้าไม่ผ่านทั้งคู่ → บอกทั้ง 2 เหตุผล
age = 10
salary = 8000
err=[]
if age>=20 and salary>=15000:
    print("Approved")
else :
    print("Rejected")
    if age<20 :
        err.append("Age must be at least 20")
    if salary<15000:
        err.append("Salary must be at least 15000")
for e in err :print(f"{e}")
###################################################
orders = [
    {"id": "ORD001", "product": "iPhone", "amount": 32900},
    {"id": "ORD002", "product": "AirPods", "amount": 6900},
    {"id": "ORD003", "product": "iPad", "amount": 19900},
    {"id": "ORD004", "product": "MacBook", "amount": 45900},
]

# 1. print รายละเอียดแต่ละ order:
#    "ORD001: iPhone - 32,900 THB"
totals=0
expensive_amount=0
order_id=""
product=""
for o in orders :
    if o["id"]=="ORD001" :
        print(f"{o['id']} : {o['product']} - {o['amount']:,} THB")
# 2. คำนวณยอดรวมทั้งหมด แล้ว print:
#    "Total: 105,600 THB"
for o in orders :
    totals=totals+o['amount']
    if o['amount']>=expensive_amount:
        expensive_amount=o['amount']
        order_id=o["id"]
        product=o["product"]
print(f"Total: {totals:,} THB")
# 3. หา order ที่แพงที่สุด แล้ว print:
#    "Most expensive: ORD004 - MacBook (45,900 THB)"
print(f"Most expensive: {order_id} - {product} ({expensive_amount:,}) THB")
most_expensive = max(orders, key=lambda o: o["amount"])
print(f"Most expensive: {most_expensive['id']} - {most_expensive['product']}")
most_cheap = min(orders, key=lambda o: o["amount"])
print(f"Most cheap: {most_cheap['id']} - {most_cheap['product']}")


###################################################
# กติกา:
# 1. กำหนดเลขลับ secret = 7
# 2. ให้ user ทายไปเรื่อยๆ จนกว่าจะถูก
# 3. ถ้าทายผิด บอก "Too high!" หรือ "Too low!"
# 4. ถ้าทายถูก บอก "Correct! You won in X attempts"
# 5. นับจำนวนครั้งที่ทาย
# Hint: ใช้ input() รับค่า และ int() แปลงเป็นตัวเลข
# guess = int(input("Enter your guess: "))


# import random
# secret = random.randint(1, 100)
# times=0
# while True :
#     try:
#         input_guess=int(input("Enter your guess:"))
#         times=times+1
#         if secret==input_guess:
#             print(f"Correct! You won in {times} attempts")
#             break
#         elif input_guess>secret: print("Too high!")
#         else : print("Too low!")
#     except:
#         print("Invalid input! Please enter a whole number (no decimals)")
#         continue

# Lab 12: Mini Project — CLI Calculator
# รวมทุกอย่างที่เรียนมา!
# Project นี้จะใช้:

# Variables & Data Types
# String operations
# Collections (dict)
# if/elif/else
# while loop
# try/except
# Functions (แอบสอนเพิ่ม!)


# Requirements
# สร้างเครื่องคิดเลขที่:

# แสดง menu ให้เลือก: +, -, *, /
# รับตัวเลข 2 ตัว
# คำนวณและแสดงผล
# ถามว่าจะคำนวณต่อไหม (y/n)
# จัดการ error:

# input ไม่ใช่ตัวเลข
# หารด้วย 0
# operator ไม่ถูกต้อง

def main_menu_calculator():
    print("===== Calculator =====")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

def cal(input_choice):
    input1=float(input("Enter first number:"))
    input2=float(input("Enter second number:"))
    if  input_choice==1:
        add(input1,input2)
    elif input_choice==2:
        subtract(input1,input2)
    elif input_choice==3:
        multiply(input1,input2)
    elif input_choice==4:
        divide(input1,input2)   
     
def add (input1,input2) :
    print(f"Result: {input1} + {input2} = {(input1+input2):,.2f}")
    
def subtract (input1,input2) :
    print(f"Result: {input1} - {input2} = {(input1-input2):,.2f}")
    
def multiply (input1,input2) :
    print(f"Result: {input1} * {input2} = {(input1*input2):,.2f}")
    
def divide (input1,input2) :
    if input2==0:  
        print("Error: Cannot divide by zero!")
        return
    print(f"Result: {input1} / {input2} = {(input1/input2):,.2f}")
    
def get_yes_no(prompt):
    while True:
        user_input = input(prompt).lower().strip()
        
        if user_input in ['y', 'n']:
            return user_input[0]    # return 'y' หรือ 'n'
        else:
            print("Invalid input! Please enter 'y' or 'n'")  
                    
while True:
    main_menu_calculator()
    try:
        input_choice=int(input("Enter choice (1-5):"))
        if input_choice not in [1,2,3,4,5] : 
            print("Invalid choice! Please select 1-5")
            continue
        try:
            if input_choice==5: 
                print("Thank you! Goodbye") 
                break
            cal(input_choice)
            input_con = get_yes_no("Continue? (y/n): ")
            if input_con=='n':
                print("Thank you! Goodbye") 
                break 
        except:
            print("Invalid input! Please enter a whole number (no decimals)")
            continue
    except:
            print("Invalid input! Please enter a whole number (no decimals)")
            continue
    
