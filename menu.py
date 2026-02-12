

marks = []

def enter_marks():
    """Enter marks for subjects with option to exit early"""
    marks.clear()
    n = int(input("Enter number of subjects: "))
    print("Type 'exit' anytime to stop entering marks early.")
    
    for i in range(n):
        while True:
            inp = input(f"Enter marks for subject {i+1}: ").strip()
            if inp.lower() == "exit":
                print("Stopped entering marks early.")
                return
            try:
                m = float(inp)
                if 0 <= m <= 100:
                    marks.append(m)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number or 'exit'.")
    print("Marks saved successfully!")

def calculate_percentage():
    if not marks:
        print("No marks entered yet!")
        return None
    percentage = sum(marks) / len(marks)
    print("Percentage:", round(percentage, 2))
    return percentage

def assign_grade():
    percentage = calculate_percentage()
    if percentage is None:
        return
    match percentage:
        case p if p >= 90:
            grade = "A+"
        case p if p >= 80:
            grade = "A"
        case p if p >= 70:
            grade = "B"
        case p if p >= 60:
            grade = "C"
        case p if p >= 50:
            grade = "D"
        case _:
            grade = "Fail"
    print("Grade:", grade)


while True:
    print("\n--- Student Result System ---")
    print("1. Enter Marks")
    print("2. Calculate Percentage")
    print("3. Assign Grade")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    match choice:
        case "1":
            enter_marks()
        case "2":
            calculate_percentage()
        case "3":
            assign_grade()
        case "4":
            print("Exiting...")
            break
        case _:
            print("Invalid choice! Try again.")
