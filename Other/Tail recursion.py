def make_student_classifier(lower_bound, upper_bound):
    def classify_student(exam_dict):    # exam_dict takes the students dict as an argument
      
        # returns a dictionary with the specified condition
        return {k:v for (k,v) in exam_dict.items() if lower_bound <= v < upper_bound} 

    # function has to be returned in order to be accessibe to the outer function
    return classify_student   
    
students = {
    'Alice': 98,
    'Bob': 67,
    'Chris': 85,
    'David': 75,
    'Ella': 54,
    'Fiona': 35,
    'Grace': 69
}
grade_A = make_student_classifier(80, 100)
grade_B = make_student_classifier(70, 80)
grade_C = make_student_classifier(50, 70)
grade_D = make_student_classifier(0, 50)

print(grade_A(students))
print(grade_B(students))
print(grade_C(students))
print(grade_D(students))


#################  SAMPLE ###################
# def foo(lst):
#     def bar(dct):
#         a = 5
#         return dct
#     return bar
        

# a = foo(2)
# b = a(1)
