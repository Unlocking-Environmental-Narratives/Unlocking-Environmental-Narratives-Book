from genderize import Genderize
import csv


articles_tested = []
with open("byline_genders.csv", 'r') as fileDone:
    lines = fileDone.readlines() 
    for line in lines:
        if "Letter" not in line:
            print(line.strip())
        else:
            line_a = line.strip().split(",")
            line_a[1] = "none"
            print(",".join(line_a))
