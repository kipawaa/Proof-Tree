from sections import *

def is_root(article_sections):
    return "### Dependencies\n### Dependents" in article_sections[LINKS]

def is_leaf(article_sections):
    return article_sections[LINKS].endswith("### Dependents\n")
