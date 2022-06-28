from genderize import Genderize
import csv

articles_tested = []
with open("byline_genders.csv", 'r') as fileDone:
    lines = fileDone.readlines() 
    for line in lines:
        article_id = line.split(",")[0]
        articles_tested.append(article_id)

ten_names = []
ten_ids = []
outF = open("byline_genders.csv", "a")
with open('country_diary_articles.csv', 'r' ) as theFile:
    reader = csv.DictReader(theFile)
    for line in reader:
        article_id = line['id']
        if article_id in articles_tested:
            print("skipped")
            continue
        print(article_id)
        if line['byline'] == "":
            print("%s,%s,%s,%s" % (article_id, "none", "", "empty"), file=outF)
            continue
        names = line['byline'].split()
        if names[0].lower() == "corrections":
            print("%s,%s,%s,%s" % (article_id, "none", "", "corrections"), file=outF)
            continue
        if names[0].lower() == "by":
            names = names[1:]
        if len(names[0]) < 2:
            names = names[1:]
        first_name = names[0]
        ten_ids.append(article_id)
        ten_names.append(first_name)
        if len(ten_names) == 10:
            ## do genderize call
            genders = Genderize().get(ten_names)
            for i in range(len(genders)):
                gender_str = ""
                if genders[i]['gender'] is None:
                    gender_str = "none"
                else:
                	gender_str = genders[i]['gender']
                print("%s,%s,%f,%s" % (ten_ids[i], gender_str, genders[i]['probability'], genders[i]['name']), file=outF)
            ten_ids = []
            ten_names = []
if len(ten_names) > 0:
    ## do last genderize call
    genders = Genderize().get(ten_names)
    for i in range(len(genders)):
        gender_str = genders[i]['gender']
        if genders[i]['gender'] is None:
            gender_str = "none"
        print("%s,%s,%f,%s" % (ten_ids[i], gender_str, genders[i]['probability'], genders[i]['name']), file=outF)
outF.close()
