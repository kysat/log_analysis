# "Database code" for the logs_analysis.

import psycopg2
import sys


# create views for clear up necessary items in Database
# for using below get-functions.
def create_view():
    try:
        conn = psycopg2.connect("dbname=news")
        cursor = conn.cursor()
        # create view from log table
        # that showing article title with viewed count.
        cursor.execute(
            '''
            create or replace view view_articles as
            select replace(path, '/article/', '') as title, count(*) as views
            from log where status='200 OK' and path != '/'
            group by path order by views desc;
            '''
        )
        # create view joining author name and article title.
        cursor.execute(
            '''
            create or replace view view_authors as
            select authors.name, articles.slug
            from authors join articles
            on authors.id = articles.author;
            '''
        )
        conn.commit()
        conn.close()
    except psycopg2.Error as e:
        print("Unable to connect to database")
        sys.exit(1)


# Generate 'report.txt' that article titles with viewed counts is written.
def get_most_popular_article():
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(
        '''
        select * from view_articles
        limit 4;
        '''
    )
    results = cursor.fetchall()
    conn.close()
    with open('report.txt', 'w') as f:
        for row in results:
            title = row[0].replace('-', ' ').title()
            view = str(row[1])
            if title == '':
                continue
            else:
                f.write(title + " -- " + view + "views\n")


# Generate 'report.txt' that article author names
# with viewed counts is written.
def get_most_popular_article_author():
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(
        '''
        select view_authors.name as name, sum(view_articles.views) as views
        from view_authors
        join view_articles on view_authors.slug = view_articles.title
        group by name
        order by views desc;
        '''
    )
    results = cursor.fetchall()
    conn.close()
    with open('report.txt', 'w') as f:
        for row in results:
            name = row[0]
            view = str(row[1])
            f.write(name + " -- " + view + "views\n")


# Generate 'report.txt' that dates
# that error arose more than 1% in requests in one day is written.
def get_error_days():
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(
        '''
        select cast(time as date) as date, status, count(status)
        from log group by date, status;
        '''
    )
    results = cursor.fetchall()
    conn.close()
    results_on_each_dates = {}
    for row in results:
        date = row[0]
        results_on_each_dates[date] = []
    for row in results:
        date = row[0]
        count = row[2]
        # results_on_each_dates contains data like
        # {date: [times that successfully viewed, times that error arose]}
        results_on_each_dates[date].append(count)
    with open('report.txt', 'w') as f:
        for d in results_on_each_dates:
            count_sum = results_on_each_dates[d][0] \
                        + results_on_each_dates[d][1]
            error_rate = float(results_on_each_dates[d][1]) / count_sum
            if error_rate >= 0.01:
                f.write(d.strftime('%b,%Y') + ' -- ' + str(
                    round(error_rate * 100, 2)) + '% errors\n')
