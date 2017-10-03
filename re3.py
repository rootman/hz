import re

link = "https://www.bger.ch/ext/eurospider/live/de/php/aza/http/index.php?highlight_docid=aza%3A%2F%2Faza://24-07-2017-4A_134-2017&lang=de&zoom=&type=show_document"

pattern = r"[0-9]{2}-[0-9]{2}-[0-9]{4}"

search = re.search( pattern, link )

print search.group(0)