#!/usr/bin/python3

from logsdb import create_view, get_most_popular_article, \
    get_most_popular_article_author, \
    get_error_days

print("What do you want to know?")
line = '-' * 30
print(line)
print("1: The most popular three articles of all time")
print("2: The most popular article authors of all time")
print("3: Days did more than 1% of requests lead to errors")
print(line)
user_select = str(input("select: "))

while True:
    if user_select == '1':
        get_most_popular_article()
        break
    elif user_select == '2':
        get_most_popular_article_author()
        break
    elif user_select == '3':
        get_error_days()
        break
    else:
        print("Wrong input. Please try other number")
        user_select = str(input("select: "))

print("Report file was successfully generated!")