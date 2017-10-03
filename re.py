import re
import itertools

string = "Hallo mein name ist Art. 72 BGG, Art. 72 BGG, Art. 62 Abs. 3 BGG, Art. 42 Abs. 1 und 2 BGG, Art. 121-123 BGG, Art. 121 ff. BGG, ..."


# Art. 72 BGG
# Art. 62 Abs. 3 BGG
# Art. 42 Abs. 1 und 2 BGG
# Art. 121-123 BGG
# Art. 121 ff. BGG
# Art. 22 Abs. 1 des Bundesgesetzes vom 6. Oktober 1989 ueber die Arbeitsvermittlung und den Personalverleih (Arbeitsvermittlungsgesetz, AVG; SR 823.11)
# Art. 47 Abs. 1 lit. b ZPO
# Art. 6 Ziff. 1 EMRK

pattern1 = r"Art\.\ \d+\ [A-Z]{2,}"
pattern2 = r"Art\.\ \d+\ ff\.\ [A-Z]{2,}"
pattern3 = r"Art\.\ \d+\ Abs\.\ \d+\ [A-Z]{2,}"
pattern4 = r"Art\.\ \d+\ Abs\.\ \d+\ und\ \d+\ [A-Z]{2,}"
#pattern4 = r"Art\.\ \d+\ Abs\.\ \d+-\d+\ [A-Z]{2,}"

matches1 = re.findall(pattern1, string)
matches2 = re.findall(pattern2, string)
matches3 = re.findall(pattern3, string)
matches4 = re.findall(pattern4, string)

#allList = list(itertools.chain(matches1, matches2, matches3))
#allList = matches1 + matches3 + matches4
allList = matches1 + matches2 + matches3 + matches4
allList = list(set(allList))

print allList
# print matches1
# print matches2
# print matches3
#print matches4