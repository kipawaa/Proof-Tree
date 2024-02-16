import re

def name_to_link(article_name):
    return '[[' + article_name[:-3].replace('-', ' ') + ']]'

def link_to_name(article_link):
    if '|' in article_link:
        return article_link[article_link.index('|') + 1:-2].replace(' ', '-') + '.md'
    return article_link[2:-2].replace(' ', '-') + '.md'

if __name__ == "__main__":
    print(link_to_name("[[link]]"))
    print(link_to_name("[[link with spaces]]"))
    print(link_to_name("[[text|link with text and spaces]]"))

    print(name_to_link("Domain-of-a-Relation-is-a-Set.md"))
