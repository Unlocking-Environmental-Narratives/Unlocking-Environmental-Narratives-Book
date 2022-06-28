from genderize import Genderize
import csv
import random

with open("cd_gender_balanced.txt", 'r') as fin:
    lines = fin.readlines()
    for line in lines:
        line_a = line.strip().split("\t")
        print(line_a[0])
        if line_a[1] == "male":
            with open("male/%s.txt" % line_a[0], 'w') as fout:
                print(line_a[2], file=fout)
        elif line_a[1] == "female":
            with open("female/%s.txt" % line_a[0], 'w') as fout:
                print(line_a[2], file=fout)

