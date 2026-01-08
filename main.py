# "r" = read (default) — อ่านอย่างเดียว
# "w" = write — เขียนทับ (ลบของเดิม!)
# "a" = append — เขียนต่อท้าย
# "x" = create — สร้างใหม่ (error ถ้ามีอยู่แล้ว)

# # เขียนทับ
# with open("test.txt", "w") as f:
#     f.write("Line 1\n")
#     f.write("Line 2\n")

# # เขียนต่อท้าย
# with open("test.txt", "a") as f:
#     f.write("Line 3\n")
    

with  open('pyfile.txt', 'w') as f:
   f.write("Line1")

with  open('pyfile.txt', 'r') as f:
     for s in f :
         print(f"read : {s}")
         
# สร้าง 3 functions:
# 1. save_note(filename, content) — บันทึกโน้ตลงไฟล์
# 2. append_note(filename, content) — เพิ่มโน้ตต่อท้ายไฟล์
# 3. read_note(filename) — อ่านโน้ตจากไฟล์ return content
#    ถ้าไฟล์ไม่มี return "File not found"
# ตัวอย่างการใช้งาน:
# save_note("notes.txt", "Meeting at 10am")
# append_note("notes.txt", "Call John")
# print(read_note("notes.txt"))
# → Meeting at 10am
# → Call John

def save_note(filename, content):
    with open(filename, 'w') as f:
       f.write(content)

def append_note(filename, content):
    with open(filename, 'a') as f:
        f.write(content)

def read_note(filename):
    with open(filename, 'a') as f:
        return f

save_note("notes.txt", "Meeting at 10am\n")
append_note("notes.txt", "Call John")
print(read_note("notes.txt"))
  