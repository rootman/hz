import urllib
from bs4 import BeautifulSoup
import re
import itertools
import json

import sys
sys.path.append('/Users/anthony/anaconda/lib/python2.7/site-packages/')

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')


URLS = './urls.txt'
WORDS = './tagwords.txt'
TAGS = './keywords.csv'
OUT = './documents.json'


def open_list( path ):
    f = open(path, 'rb')
    file = f.read().split('\n')
    return file


def open_tags( path ):
    f = open(path, 'rb')
    rows = f.read().split('\r\n')
    arttags = {}
    for row in rows:
        article, tags = row.split(';', 1)
        arttags[article.lower()] = [x.strip('"') for x in tags.split('; ')]
    #print arttags
    return arttags


def get_html( url ):
    site = urllib.urlopen(url)
    string = site.read()
    return string


def get_and_parse_site( link ):
    # Get html from one url
    #document['html'] = get_html(link)
    string = get_html(link)

    # Load to beautifulsoup
    #parsed_html = BeautifulSoup(document['html'], 'html.parser')
    parsed_html = BeautifulSoup(string, 'html.parser')

    return parsed_html


def get_main( parsed_html ):
    # Get main class
    maindiv = parsed_html.findAll("div", { "class": "main"})

    # Make string
    mainstring = str(maindiv) #.lower()

    return mainstring


def find_articles( string ):
    pattern1 = r"Art\.\ \d+\ [A-Z]{2,}"
    pattern2 = r"Art\.\ \d+\ ff\.\ [A-Z]{2,}"
    pattern3 = r"Art\.\ \d+\ Abs\.\ \d+\ [A-Z]{2,}"
    pattern4 = r"Art\.\ \d+\ Abs\.\ \d+\ und\ \d+\ [A-Z]{2,}"
    pattern5 = r"art\.\ \d+\ [A-Z]{2,}"
    pattern6 = r"art\.\ \d+\ abs\.\ \d+\ [A-Z]{2,}"
    pattern7 = r"art\.\ \d+\ abs\.\ \d+\ und\ \d+\ [A-Z]{2,}"
    #pattern4 = r"Art\.\ \d+\ Abs\.\ \d+-\d+\ [A-Z]{2,}"
    # Art. 334a

    match1 = re.findall(pattern1, string)
    match2 = re.findall(pattern2, string)
    match3 = re.findall(pattern3, string)
    match4 = re.findall(pattern4, string)
    match5 = re.findall(pattern5, string)
    match6 = re.findall(pattern6, string)
    match7 = re.findall(pattern7, string)
    #match4 = re.findall(pattern4, string)

    # Concenate to 1 list
    articleList = match1 + match2 + match3 + match4 + match5 + match6 + match7

    # Remove duplicates
    articleList = list(set(articleList))

    return articleList


def get_tags_for_articles( articleList, tagDict ):
    tags = []
    sub_articles = []

    for article in articleList:

        sub_article = article

        pattern1 = r"\ Abs\.\ \d+\ "
        pattern2 = r"\ Abs\.\ \d+\ und\ \d+\ "
        pattern3 = r"\ ff\.\ "
        pattern4 = r"-\d+\ "

        sub_article = re.sub(pattern2, " ", sub_article)
        sub_article = re.sub(pattern1, " ", sub_article)
        sub_article = re.sub(pattern3, " ", sub_article)
        sub_article = re.sub(pattern4, " ", sub_article)

        # Add to sub_articles list (before decapitalizing)
        sub_articles += [sub_article]

        sub_article = sub_article.lower()
        #print sub_article

        try:
            this_tags = tagDict[sub_article]
            tags += this_tags

        except:
            pass

    #tags = list(set(tags))
    tags += sub_articles

    return tags


def find_words_in_main( string, wordList ):
    tag_words = []
    lower_string = string.lower()
    for word in wordList:
        if word.lower() in lower_string:
            tag_words.append(word)

    #print('found', tag_words)

    return tag_words


def get_date(link):
    pattern = r"[0-9]{2}-[0-9]{2}-[0-9]{4}"
    search = re.search( pattern, link )
    return search.group(0)


def get_id( parsed_html ):
    # Find candidates
    candidates = []
    for element in parsed_html.findAll("div", { "class": "para"}):
        try:
            for bold in element.find("b"):
                candidates.append(bold)
        except:
            pass

    # ID pattern
    pattern = re.compile("[A-Z0-9]{2}_[0-9]{3}/[0-9]{4}")

    ids = []
    for candidate in candidates:
        match =  pattern.match(candidate)
        if match is not None:
            ids.append(candidate)

    #print ids[0]
    result = "N/A"
    try:
        result = ids[0].strip()
    except:
        pass

    return result


def get_gegenstand( parsed_html ):
    gegenstand = False

    # Find identifier
    identifier = parsed_html.find('div', text=re.compile(r'Gegenstand\s*'))

    # If no German was found
    if identifier is None:
        identifier = parsed_html.find('div', text=re.compile(r'Objet\s*'))

    # If either German or French was found
    if identifier is not None:
        next_div = identifier.find_next_sibling('div')
        gegenstand = next_div.contents[0].strip().strip(',')

    return gegenstand or 'N/A'


def save_to_json( document, outfile ):
    with open(outfile, 'wb') as f:
        json.dump(document, f)


def main():
    # Get linklist
    link_list = open_list(URLS)

    # Get article-tags mapping
    art_tags = open_tags(TAGS)

    # Open tagwords list
    wordList = open_list(WORDS)

    # Define documents
    documents = []

    for link in link_list:

        print link

        # Document object
        document = {}

        # Store url
        document['url'] = link

        # Store date
        document['date'] = get_date(link)

        # Parse site
        parsed_html = get_and_parse_site(link)
        #print parsed_html

        # Get main string from url
        main_string = get_main(parsed_html)

        # Get mentioned articles articles
        document['articles'] = find_articles(main_string)

        # Get tags for articles
        document['tags'] = get_tags_for_articles( document['articles'], art_tags )

        # Add tags for words
        document['tags'] += find_words_in_main( main_string, wordList )

        # Deduplicate tags
        document['tags'] = list(set(document['tags']))
        print document['tags']

        # Get id
        document['id'] = get_id(parsed_html)

        # Get Gegenstand
        document['gegenstand'] = get_gegenstand(parsed_html)

        documents.append(document)

        print('.')

    # Write to json
    save_to_json( documents, OUT )


main()
