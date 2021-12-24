# DORK SCANNER V2.5.0 #

An atypical search engine scanner that scans search engines with queries you provide to find vulnerable URLs.


## Introduction ##

### What is dorking?
Dorking is a technique used by news organizations, investigative agencies, security auditors, and savvy criminals to query various search engines to find hidden information on public websites and vulnerabilities exposed by public servers. Dorking is a way to use search engines to their fullest capacity to penetrate web-based services to depths that may not be visible at first glance.

## Requirements ##

```
pip3 install -r requirements.txt
```

## Usage ##

### Command Line Interface
```
# python3 cli.py -h
usage: python3 cli.py [-h] [-q QUERY] [-e ENGINE] [-p PAGES] [-o OUTPUT] [-d DORK]

Example : python3 cli.py -e Bing -p 2 -o test.txt -d dorks.txt

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Specifies the query
  -e ENGINE, --engine ENGINE
                        Specifies the search engine (Ask | Bing | WoW)
  -p PAGES, --pages PAGES
                        Specifies the pages numbers (Default: 1)
  -o OUTPUT, --output OUTPUT
                        Specifies the output file name (Default: /home/balgogan/dorkscanner/pages/pages.txt)
  -d DORK, --dork DORK  Specifies the file containing the dorks (Default: /home/balgogan/dorkscanner/dorks/dorks.txt)

  
```

#### You can also specify arguments inside the program:

```
Enter the search query:
Choose the search engine (Ask | Bing | WoW):
```

### Python Module