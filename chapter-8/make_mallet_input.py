from genderize import Genderize
import csv

mallet_articles = {}

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

with open("cd_gender.txt", 'w') as fout:
    for article_id in mallet_articles:
        article = mallet_articles[article_id]
        if article['gender'] == 'male' or article['gender'] == 'female':
            if article['prob'] > 0.8:
                print("%s\t%s\t%s" % (article_id, article['gender'], article['body_text']), file=fout)

