import re
def school_register(students):
    dct = {}

    for student in students:
        student = re.split(": |, " ,student)
    
        # Let's make grades and scores (int) and (float)
        score = float(student[5])
        grade = int(student[3])
        name = student[1]

        if score > 3.00:
            if grade not in dct:
                dct[grade] = {name:score}
            else:
                dct[grade].update({name:score})

    # Make the variables for storage
    name = "" 
    score = 0

    # Iterate through ther dict keys and values
    for grade, val in dct.items():
        for n, s in val.items():

	    # Add the name separated with comma if string is empty
            if name == "":
                name += n + ", "

	    # Otherwise just add the name with no comma.
            else:
                name += n
            score += s
        avg_score = score/len(val)
        print(f"{grade+1} Grade")
        print(f"List of students: {name}")
        print (f"Average annual grade from last year: {avg_score:.2f}\n")

	# Make variables empty for the next iteration
        name = ""
        score = 0
        
# Call the function
 
school_register(students = [
"Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
    "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
    "Student name: George, Grade: 8, Graduated with an average score: 2.83",
    "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
    "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
    "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
    "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
    "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
    "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
    "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
    "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
    "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00"
])




        
        
        
        
        