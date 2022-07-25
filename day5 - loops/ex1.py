# You are going to write a program that calculates the average student height from a List of heights.
#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
student_heights = input("Input a list of student heights with a space").split()
total_height = 0
total_students = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_height = total_height+student_heights[n]
    total_students = total_students+1

avg_height = round(total_height/total_students)
print(avg_height)
