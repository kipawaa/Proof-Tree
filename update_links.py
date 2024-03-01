from sections import *
from names import *

import re

# List of files that don't need link updates
IGNORE_LIST = [
    "About.md",
    "Contact.md",
    "Contributing.md",
    "Home.md",
    "Template.md",
    "Upcoming-Features.md",
    "Missing-Articles.md",
    "Roots.md",
    "_Footer.md",
    "_Sidebar.md"
]

wiki_directory = "../Proof-Tree.wiki/"


def update_article_links(article_name, article_sections):
        print(f"updating {article_name}")
        
        # get links from the main sections
        links = []
        for section in [STATEMENT, EXPLANATION, PROOFS, HISTORY, APPLICATIONS]:
            links += re.findall(r'\[\[[\w+\s]+[\|[\w+\s]+]?\]\]',
                                article_sections[section])


        # format links
        for i in range(len(links)):
            if '|' in links[i]:
                links[i] = '[[' + links[i][links[i].index('|') + 1:]

        # only keep unique links
        links = set(links)

        # with all links found, now add to dependencies and add to dependency
        # files
        links_section = article_sections[LINKS].split('\n')
        while '#' not in links_section[2]:
            links_section.pop(2)

        for link in links:
            links_section.insert(2, '- ' + link)

        article_sections[LINKS] = '\n'.join(links_section)

        # write back to file
        with open(wiki_directory + article_name, 'w') as article:
            article.write('\n## '.join(article_sections))

        # now update dependencies to list this article as a dependent
        for link in links:
            # get the filename for the linked file
            linked_article_name = link_to_name(link)
            
            try:
                # get the sections from the linked file
                with open(wiki_directory + linked_article_name) as linked_article:
                    linked_article_content = linked_article.read()
                linked_article_sections = get_sections(linked_article_content)

                # update the dependents links
                if name_to_link(article_name) not in linked_article_sections[LINKS]:
                    linked_article_sections[LINKS] += '- ' + name_to_link(article_name) + '\n'
                
                # write to the file
                with open(wiki_directory + linked_article_name, 'w') as linked_article:
                   linked_article.write('\n## '.join(linked_article_sections))
            except:
                print(f"{linked_article_name} is missing")
                with open(wiki_directory + "Missing-Articles.md", "a") as missing_article:
                    missing_article.write('\n- ' name_to_link(article_name) + ' links ' + name_to_link(linked_article_name))
