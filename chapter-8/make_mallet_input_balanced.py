from genderize import Genderize
import csv
import random

mallet_articles = {}

max_per_category = 0

with open("country_diary_articles.csv", 'r') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        article_id = row['id']
        body_text = row['body_text']
        mallet_articles[article_id] = {}
        mallet_articles[article_id]['body_text'] = body_text

with open("byline_genders.csv", 'r') as fin:
    reader = csv.reader(fin)
    for row in reader:
        article_id = row[0]
        gender = row[1]
        prob = 0.0
        if row[2] != "":
            prob = float(row[2])
        mallet_articles[article_id]['gender'] = gender
        mallet_articles[article_id]['prob'] = prob
        if gender == "female":
            max_per_category = max_per_category + 1

male_articles = 0
female_articles = 0
with open("cd_gender_balanced.txt", 'w') as fout:
    keys = list(mallet_articles.keys()) # List of keys
    random.shuffle(keys)
    for article_id in keys:
        article = mallet_articles[article_id]
        if article['gender'] == 'male' or article['gender'] == 'female':
            if article['prob'] > 0.8:
                if article['gender'] == 'male':
                    if male_articles > max_per_category:
                        continue
                    else:
                        male_articles = male_articles + 1
                if article['gender'] == 'female':
                    if female_articles > max_per_category:
                        continue
                    else:
                        female_articles = female_articles + 1
                print("%s\t%s\t%s" % (article_id, article['gender'], article['body_text']), file=fout)

