count=int(input("Enter number of students: "))

# Initialize an empty list to store student data
students={}

for i in range(count):
    
    print(f"\nEnter details for student {i+1}:")
    
    name=input("Enter student name: ")
    tamil=int(input("Enter tamil marks: "))
    english=int(input("Enter english marks: "))
    maths=int(input("Enter maths marks: "))
    science=int(input("Enter science marks: "))
    social=int(input("Enter social marks: "))
    total=tamil+english+maths+science+social
    average=total/5 
    
    if average>=90:
        grade='A+'
    elif average>=80:
        grade='A'
    elif average>=70:
        grade='B+'
    elif average>=60:
        grade='B'
    elif average>=50:
        grade='C'
    elif average>=40:
        grade='D'
    else:
        grade='F'
    
    
    students[name]={
        'Tamil':tamil,
        'English':english,
        'Maths':maths,
        'Science':science,
        'Social':social,
        'Total':total,
        'Average':average,
        'Grade':grade
    }
    
print("\n "+ '='*45)
print(" | {:^43} |".format("Student Report Card"))
print(" + '='*45")

for name, details in students.items():
   for name, details in students.items():
    print(f"\nStudent Name : {name}")
    print("-"*45)
    print(f"{'Subject':<20}{'Marks':>10}")
    print("-"*45)
    print(f"{'Tamil':<20}{details['Tamil']:>10}")
    print(f"{'English':<20}{details['English']:>10}")
    print(f"{'Maths':<20}{details['Maths']:>10}")
    print("-"*45)
    print(f"{'Total':<20}{details['Total']:>10}")
    print(f"{'Average':<20}{details['Average']:>10}")
    print(f"{'Grade':<20}{details['Grade']:>10}")
    print("="*45)