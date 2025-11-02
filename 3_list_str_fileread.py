file=open("q4/employee.txt")

fileText=file.read()

records=fileText.split("\n")

file.close()

employeeList=[]

class Employee:
	def __init__(self,name,gender,location,salary):
		self.name = name
		self.gender = gender
		self.location = location  # Use lowercase
		self.salary = salary
		
for i in range(1,len(records)):
	recordDetails=records[i].split(",")
	if len(recordDetails) == 4:
		empName=recordDetails[0]
		empGender=recordDetails[1]
		empLocation=recordDetails[2]
		empSalary=recordDetails[3]
		
		empObject=Employee(empName,empGender,empLocation,empSalary)
		empObject.name=empName
		empObject.gender=empGender
		empObject.location=empLocation
		empObject.salary=empSalary
		
		employeeList.append(empObject)
	
def totalSalaryToBePaid(empList):
	totalSalary=0
	for emp in empList:
		totalSalary=totalSalary+int(emp.salary)
	return totalSalary
def genderBaseSalary(empList):
	maleSalary=0
	femaleSalary=0
	maleCount=0
	femaleCount=0
	for emp in empList:
		if emp.gender=="male":
			maleSalary+=int(emp.salary)
			maleCount+=1
		elif emp.gender=="female":
			femaleSalary+=int(emp.salary)
			femaleCount+=1
	return{"male salary":maleSalary,"female salary":femaleSalary, "male average": maleSalary/maleCount if maleCount > 0 else 0, "female average": femaleSalary/femaleCount if femaleCount > 0 else 0}

def locationBaseSalary(empList):
	locations = {}
	for emp in empList:
		loc = emp.location
		if loc not in locations:
			locations[loc] = {"total": 0, "count": 0}
		locations[loc]["total"] += int(emp.salary)
		locations[loc]["count"] += 1
	for loc in locations:
		locations[loc]["average"] = locations[loc]["total"] / locations[loc]["count"]
	return locations

print(f"Total salary of the employees: {totalSalaryToBePaid(employeeList)}")
print(f"Total number of employees: {len(employeeList)}")
gender_data = genderBaseSalary(employeeList)
print(f"Total male salary: {gender_data['male salary']}")
print(f"Total female salary: {gender_data['female salary']}")
print(f"Average salary per gender:")
print(f"  Male: {gender_data['male average']}")
print(f"  Female: {gender_data['female average']}")
location_data = locationBaseSalary(employeeList)
print("Average salary per location:")
for loc, data in location_data.items():
    print(f"  {loc}: {data['average']}")
