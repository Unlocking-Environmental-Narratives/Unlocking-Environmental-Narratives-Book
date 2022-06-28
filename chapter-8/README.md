# Unlocking Environmental Narratives - Chapter 8

This repository includes a number of scripts that were developed to prepare the Guardian Country Diary data for analysis. All the country diary article data can be downloaded using the Guardian OpenPlatform API: https://open-platform.theguardian.com.

The scripts assume the data downloaded from the API has been saved in a filed called `country_diary_articles.csv`. To use the Genderize API to assign gender labels to the authors, use the script `genderize_country_diary.py`. This will output the data in `byline_genders.csv`.

`clean_Letters.py` is a helper script to remove all Letters to the editor that were included in the data set.

The Naive Bayes classification was done using the Mallet (Machine Learning for Language toolkit) available for download here: https://mimno.github.io/Mallet/

The create the input file for Mallet run `make_mallet_input.py`, which will output the `cd_gender.txt` file. This can then be prepared for use in Mallet with the following command.

`mallet-2.0.8/bin/mallet import-file --input cd_gender.txt --output cd_gender.mallet`
