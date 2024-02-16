import re

# constants for indices of sections in articles
STATEMENT = 0
EXPLANATION = 1
PROOFS = 2
HISTORY = 3
APPLICATIONS = 4
LINKS = 5
SOURCES = 6


def get_sections(article_content):
    return re.split(r'\s##\s', article_content)
