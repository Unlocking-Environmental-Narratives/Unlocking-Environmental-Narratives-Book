from genderize import Genderize
import csv
import random

with open("cd_gender_unique_articles.txt", 'r') as fin:
    lines = fin.readlines()
    for line in lines:
        line_a = line.strip().split("\t")
        print(line_a[0])
        if line_a[1] == "m":
            with open("male_author_balanced/%s.txt" % line_a[0], 'w') as fout:
                print(line_a[2], file=fout)
        elif line_a[1] == "f":
            with open("female_author_balanced/%s.txt" % line_a[0], 'w') as fout:
                print(line_a[2], file=fout)
