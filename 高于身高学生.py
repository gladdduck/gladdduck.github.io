
student_data = {
    "Alice": 170,
    "Bob": 180,
    "Charlie": 165,
    "David": 175,
    "Eve": 160
}

height_threshold = int(input("请输入身高阈值: "))

above_height_students = {}
for name, height in student_data.items():
    if height > height_threshold:
        above_height_students[name] = height
        
if above_height_students:
    print(f"高于身高阈值 {height_threshold} 的学生信息如下：")
    for name, height in above_height_students.items():
        print(f"姓名: {name}, 身高: {height} cm")
else:
    print(f"没有找到高于身高阈值 {height_threshold} 的学生信息。")
