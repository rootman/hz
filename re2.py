import re
import itertools

string = "Hallo mein name ist Art. 72 BGG, Art. 72 BGG, Art. 62 Abs. 3 BGG, Art. 42 Abs. 1 und 2 BGG, Art. 121-123 BGG, Art. 121 ff. BGG, ..."

pattern1 = r"\ Abs\.\ \d+\ "
pattern2 = r"\ Abs\.\ \d+\ und\ \d+\ "
pattern3 = r"\ ff\.\ "
pattern4 = r"-\d+\ "

string = re.sub(pattern2, " ", string)
string = re.sub(pattern1, " ", string)
string = re.sub(pattern3, " ", string)
string = re.sub(pattern4, " ", string)

print string
