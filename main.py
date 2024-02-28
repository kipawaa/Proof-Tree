from identify_stubs import *
from update_links import *

import os
from tqdm import tqdm

wiki_directory = "../Proof-Tree.wiki/"

def main():
    # clear the roots page
    print("clearing roots article")
    with open(wiki_directory + "Roots.md") as roots_article:
        content = roots_article.read()
        content = content[:content.index("## Root Articles") + 16]

    with open(wiki_directory + "Roots.md", "w") as roots_article:
        roots_article.write(content)

    # clear the missing articles page
    print("clearing missing articles")
    with open(wiki_directory + "Missing-Articles.md") as missing_article:
        content = missing_article.read()
        content = content[:content.index('## List of Missing Articles') + 27]

    with open(wiki_directory + "Missing-Articles.md", 'w') as missing_article:
        missing_article.write(content)

    # loop over all files in directory
    print("updating links")
    for file in tqdm(os.listdir('../Proof-Tree.wiki/'), desc="Updating Links"):
        # get filename
        article_name = os.fsdecode(file)

        # only need to update links on markdown files that are article files
        if article_name.endswith('.md') and article_name not in IGNORE_LIST:
            with open(wiki_directory + article_name) as article:
                article_content = article.read()
            article_sections = get_sections(article_content)
            update_article_links(article_name, article_sections)

            if is_root(article_sections):
                with open(wiki_directory + "Roots.md", "a") as roots_article:
                    roots_article.write('\n- ' + name_to_link(article_name))


if __name__ == "__main__":
    main()
