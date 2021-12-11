# DORK SCANNER #

A typical search engine scanner that scans search engines with queries you provide to find vulnerable URLs.


## Introduction ##

Dorking is a technique used by news organizations, investigative agencies, security auditors, and savvy criminals to query various search engines to find hidden information on public websites and vulnerabilities exposed by public servers. Dorking is a way to use search engines to their fullest capacity to penetrate web-based services to depths that may not be visible at first glance.

## Requirements ##

```
pip3 install -r requirements.txt
```

## Usage ##

```
$ python3 dorkScanner.py --help
usage: dorkScanner.py [-h] [-q QUERY] [-e ENGINE] [-p PAGES] [-P PROCESSES] [-o OUTPUT]

optional arguments:
  -h, --help display this help message and exit
  -q QUERY, --query QUERY
                        Specifies the search query without ''.
  -e ENGINE, --engine ENGINE
                        Specifies the search engine (Ask | Bing | WoW)
  -p PAGES, --pages PAGES
                        Specifies the number of pages (default: 1)
  -P PROCESSES, --processes PROCESSES
                        Specify the number of processes (default: 2)
  -o OUTPUT, --output OUTPUT 
			Specify the name of the output file (absolute or relative path)
```

### You can also specify arguments inside the program:

```
Enter the search query: 
Choose the search engine (Ask | Bing | WoW):
```


Translated with www.DeepL.com/Translator (free version)
