'''
Created on Nov 23, 2016

@author: ThomasC
'''

from collections import defaultdict

salaries_and_tenures = [
    (83000, 8.7),(88000, 8.1),(48000, 0.7),(76000, 6),(69000, 6.5),(76000, 7.5),(60000, 2.5),(83000, 10),(48000, 1.9),(63000, 4.2)
    ]

# keys are years, values are list of salaries for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary);
    
# keys are years, each value are average salary for that tenure
average_salary_by_tenure = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
    }

print("Average Salary by Tenure")
print(average_salary_by_tenure)

def tenure_bucket(tenure):
    if tenure < 2:
        return "Less than 2"
    elif tenure < 5:
        return "Between 2 and 5"
    else:
        return "More than 5"
    
    
# keys are tenure_bucket, values are list of salaries for each bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    tenure_group = tenure_bucket(tenure)
    salary_by_tenure_bucket[tenure_group].append(salary);
    

# keys are tenure bucket, each value are average salary for that tenure bucket
average_salary_by_tenure_bucket = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure_bucket.items()
    }

print("Average Salary by Tenure Group")
print(average_salary_by_tenure_bucket)
    
    