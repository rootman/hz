import re

candidates = [
    '4A_134/2017',
    '4A_134/2017',
    'Urteil vom 24. Juli 2017',
    'I. zivilrechtliche Abteilung',
    'Sachverhalt:'
]

pattern = re.compile("[A-Z0-9]{2}_[0-9]{3}/[0-9]{4}")



ids = []

for candidate in candidates:

    match =  pattern.match(candidate)

    if match is not None:

        ids.append(candidate)

#return ids[0]
print ids[0]