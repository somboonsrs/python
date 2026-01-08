#Functions & Modules เขียน reusable code

# สร้าง function register_member ที่:
# 1. รับ username (บังคับ)
# 2. รับ email (บังคับ)
# 3. รับ role (default = "member")
# 4. รับ is_active (default = True)
# 5. รับ *args สำหรับ skills หลายๆ ตัว
# 6. รับ **kwargs สำหรับข้อมูลเพิ่มเติม เช่น phone, address
#
# Return dict:
# {
#     "username": ...,
#     "email": ...,
#     "role": ...,
#     "is_active": ...,
#     "skills": list ของ skills,
#     "extra_info": kwargs
# }

# ตัวอย่างการใช้งาน:

# register_member("sombo", "sombo@mail.com")
# → {'username': 'sombo', 'email': 'sombo@mail.com', 'role': 'member', 
#    'is_active': True, 'skills': [], 'extra_info': {}}

# register_member("sombo", "sombo@mail.com", "admin", True, 
#                 "Python", "Go", "Java", phone="081-xxx-xxxx")
# → {'username': 'sombo', 'email': 'sombo@mail.com', 'role': 'admin',
#    'is_active': True, 'skills': ['Python', 'Go', 'Java'], 
#    'extra_info': {'phone': '081-xxx-xxxx'}}


def register_member(username,email,role="member",is_active=True,*args,**kwargs):
    return{
            "username": username,
            "email": email,
            "role": role,
            "is_active": is_active,
            "skills": args,
            "extra_info": kwargs
        }

print(register_member("somboon","somboon@email.com","admin",False,phone="11111",gender="Male"))
print(register_member("somboon","somboon@email.com","xx",False,phone="11111",gender="Male"))
print(register_member("sombo", "sombo@email.com", "admin", True, "Python", "Go", phone="11111"))
print(register_member("sombo", "sombo@email.com", "admin", True, "Python", "Go", phone="11111"))

############################################################################

from services.product_service import get_all_products, get_product_by_id, get_expensive_products

print(get_all_products())
print(get_product_by_id(20))
print(get_expensive_products(10000))

############################################################################
from collections import Counter
orders = [
    {"id": "ORD001", "customer": "Alice", "amount": 1500, "status": "completed"},
    {"id": "ORD002", "customer": "Bob", "amount": 2300, "status": "pending"},
    {"id": "ORD003", "customer": "Alice", "amount": 800, "status": "completed"},
    {"id": "ORD004", "customer": "Charlie", "amount": 3200, "status": "completed"},
    {"id": "ORD005", "customer": "Bob", "amount": 1100, "status": "cancelled"},
    {"id": "ORD006", "customer": "Alice", "amount": 2700, "status": "pending"},
]
# ใช้ built-in functions ตอบคำถาม:
# 1. ยอดรวมทั้งหมด (sum)
# → Total: 11,600
print(f"Total: {sum([o["amount"] for o in orders]):,}")
# 2. order ที่มียอดสูงสุด (max + key)
# → Max order: ORD004 - 3,200
max_order=max(orders,key=lambda o: o["amount"])
print(f"Max order: {max_order["id"]} - {max_order["amount"]:,}")
# 3. order ที่มียอดต่ำสุด (min + key)
# → Min order: ORD003 - 800
min_order=min(orders,key=lambda o: o["amount"])
print(f"Min order: {min_order["id"]} - {min_order["amount"]:,}")
# 4. มี order ที่ cancelled ไหม (any)
# → Has cancelled: True
print(f"Has cancelled: {any(o["status"]=="cancelled" for o in orders)}")
# 5. ทุก order completed หมดไหม (all)
# → All completed: False
print(f"All completed: {all(o["status"]=="completed" for o in orders)}")
# 6. นับจำนวน order แยกตาม status (Counter)
# → Status count: {'completed': 3, 'pending': 2, 'cancelled': 1}
print(Counter([o["status"] for o in orders])) 
# 7. นับจำนวน order แยกตาม customer (Counter)
# → Customer count: {'Alice': 3, 'Bob': 2, 'Charlie': 1}
print(Counter([o["customer"] for o in orders]))


from pathlib import Path
import organizer 
import os

# สร้างโฟลเดอร์ test_files
test_dir = Path("test_files")
test_dir.mkdir(exist_ok=True)

# สร้างไฟล์จำลอง
test_files = [
    "photo1.jpg",
    "photo2.png", 
    "vacation.gif",
    "document.pdf",
    "report.docx",
    "data.xlsx",
    "script.py",
    "notes.txt",
    "music.mp3",
    "video.mp4",
]

for filename in test_files:
    (test_dir / filename).write_text(f"{filename}")

print(f"Created {len(test_files)} test files in {test_dir}/")

file = Path("organizer.py")
file.touch()

print(organizer.get_category(Path("photo.jpg").suffix))
dir_path = Path("./test_files")
print(organizer.scan_files(dir_path))
print(organizer.show_summary(dir_path))
organizer.organize_files(dir_path, dry_run=False)

