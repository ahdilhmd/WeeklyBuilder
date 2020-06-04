# Project designing software that simply calculates the overall grade for a certain class. 





categories = []
weight = []
scores = []
final_grades = []

subject = input("Welcome to Grade Calculator, Please enter the class you want to Calculate your grade for: ")
print("")


def assignments():
	temp1 = "hi"
	while temp1 != "none": 
		temp1 = input("Please enter the assignments that are part of your grade. Enter none if you have no more assignments:  ")
		categories.append(temp1)
	categories.pop()
	print(categories)

def weight_of_assignment():
	temp2 = "bye"
	for i in range(len(categories)):
		temp2 = input("Please enter the value that " + categories[i] + " is weighted on your grade. Enter the percentage it holds in decimal form:   ")
		print("")
		try:
			float(temp2)
			weight.append(temp2)
		except ValueError:
			print("Please enter weight in decimal form")

def add_to_dict():
	for i in range(len(categories)):
		grade_map[categories[i]] = weight[i]
		i+= 1
	print(grade_map)


def calculate_scores():
	for i in range(len(categories)):
		temp_score = input("What was your score on " + categories[i] + ":"  )
		scores.append(temp_score)

def calculate_grade(): 
	for i in range(len(scores)):
		final_grades.append(float(weight[i]) * float(scores[i]))
	total = 0
	for i in range(len(final_grades)):
		total += final_grades[i]
	print("")
	print("Hey there, your final grade for " + subject +  " is " + str(total) + 
		" Thank you for using our grade calculator, hope you come back and use it again!")
	print("")


@main 
assignments()
weight_of_assignment()
calculate_scores()
calculate_grade()

