"""

Module 5 - Lab 3

Analysis of the Seattle Wage Data CSV file

https://catalog.data.gov/dataset/city-of-seattle-wage-data/resource/1b351da9-d1a9-48e4-850c-a1af51c43852 (Links to an external site.)Links to an external site.


"""

import csv

# Read in the CSV file using csv.reader
with open("./city_of_seattle_wage_data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)

# Store the header line in a variable using next 
    header = reader.__next__()
    print(header)

# Create a dictionary to store the list of 'Hourly Rate' by job title 
    job_title_list = []
    hourly_rate_list = []


    for row in reader:
        job = row[3]
        hourly_rate = row[4]
        job_title_list.append(job)
        hourly_rate_list.append(hourly_rate)

job_rate_list = zip(job_title_list, hourly_rate_list)
job_rate_dict = dict(job_rate_list)

# print(job_title_list)
# print(hourly_rate_list)

print()
print(job_rate_dict)


# Write the dictionary to a file
with open("./test_file_rates.txt", "w") as outfile:
    full_file_writer = csv.writer(outfile)
    full_file_writer.writerow([header[3], header[4]])
    for key, val in job_rate_dict.items():
        full_file_writer.writerow([key, val])

# Stretch Goals
# use a for loop to go over each job and calculate the average pay

for job, rate in job_rate_dict.items():
    total_jobs = len(rate)
    for x in rate:
        s = float(x)
        sum_rates += s

avg_rate = sum_rates/total_jobs
print(sum_rates)
#     rate = float(rate)

# print(sum(hourly_rate_list))



# Print a sentence for each job saying how many people work that job and what the average pay is. (hint: if there's one person, you just need to print the first value of the rates list)
 

# Calculate the highest paying job
# Print the seattle dictionary to a file
# Store the department as the first key and print out the average wage by job title in the department