def open_tags( path ):
    f = open(path, 'rb')
    rows = f.read().split('\r\n')
    arttags = {}
    for row in rows:
        article, tags = row.split(';', 1)
        arttags[article] = [x.strip('"') for x in tags.split('; ')]
    return arttags


print(open_tags('./keywords.csv'))

#open_tags('./keywords.csv')
