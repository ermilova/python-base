class Student:

    def __init__(self, data):
        self.name = data[0]
        self.last_name = data[1]
        self.score = {"physics": float(data[2]),
                      "chemistry": float(data[3]),
                      "math": float(data[4]),
                      "comp_sci": float(data[5])}
        self.special_score = float(data[6])
        self.priorities = [data[7], data[8], data[9]]
        self.department = None

    def __str__(self):
        global exams
        return "{} {} {}".format(self.name, self.last_name, str(self.get_score(self.department)))

    def check(self, wave_, department_):
        return self.priorities[wave_] == department_

    def enroll(self, department_):
        self.department = department_

    def get_score(self, department_):
        global exams
        sum_score = 0
        for exam in exams[department_]:
            sum_score += self.score[exam]
        mean = sum_score / len(exams[department_])
        return max(mean, self.special_score)


departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
students = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
exams = {"Biotech": ["chemistry", "physics"],
         "Chemistry": ["chemistry"],
         "Engineering": ["comp_sci", "math"],
         "Mathematics": ["math"],
         "Physics": ["physics", "math"]}
n = int(input())
applicants = []

with open('applicants.txt', 'r') as file:
    for line in file:
        applicant_data = line.split()
        applicants.append(Student(applicant_data))


for wave in range(0, 3):
    for department in departments:
        depart_application = list(filter(lambda x: x.check(wave, department), applicants))
        depart_application.sort(key=lambda x: (-x.get_score(department), x.name, x.last_name))
        for applicant in depart_application:
            if len(students[department]) == n:
                break
            students[department].append(applicant)
            applicant.enroll(department)
            applicants.remove(applicant)


for department in departments:
    with open(department.lower() + ".txt", "w", encoding="utf-8") as d_file:
        students[department].sort(key=lambda x: (-x.get_score(department), x.name, x.last_name))
        for student in students[department]:
            d_file.write(str(student) + "\n")



