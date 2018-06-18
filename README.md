# Logs Analysis

## Overview
This is a program written in Python 3 for analyzing the popularity of contents in a news website using PostgreSQL for storing data (Article titles, author's infomation, log data).

## Features
It generates text file that have information of below.
* "The most popular three articles of all time"
* "The most popular article authors of all time"
* "Days did more than 1% of requests lead to errors"

[Generated text file(sample)](report.txt)

## Requirement
* Python 3
* PostgreSQL
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)  
(Recommended to install 5.1, Newer versions are not yet compatible with Vagrant.)
* [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)  
(newsdata.zip is required to put in `logs_analysis/` directory)

## How to Use
1. Start up Vagrant.
2. In the command line, switch to `logs_analysis/` directory.
3. Run: `python logsanalysis.py`, then it starts up.
4. Select from options with numbers, and input number.
< img src='input_screen.png'>

## License
This project is licensed under the MIT License.
