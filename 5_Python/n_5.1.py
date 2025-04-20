import random as rand
from pathlib import Path

def generate_name(length=8):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(rand.choices(chars, k=length))

names = [generate_name() for _ in range(10)]

while True:
    directory = input("Введите директорию для сохранения файлов (Enter - текущая директория): ").strip()
    if not directory:
        directory = '.'
        break

    dir_path = Path(directory)
    if dir_path.exists() and dir_path.is_dir(): 
        break
    else:
        print("Ошибка: директория не существует или не является папкой!")  

created_files = []
for name in names:
    path = Path(directory) / f"{name}.txt"
    try:
        path.touch()
        created_files.append(path)
    except:  
        print(f"Ошибка при создании файла {name}")
        continue  

print("\nСозданные файлы:")
for file in created_files:
    print(file.absolute())     