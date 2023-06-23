import os
import subprocess

# set directory
directory = "./articles"

# for each filename in directory
for filename in os.listdir(directory):
    # get file from filename and directory
    file = os.path.join(directory, filename)

    # if file is legit
    if os.path.isfile(file):
        print(file)
        # get articles it links to
        try:
            output = subprocess.check_output(f"sed '/id=\"linked-proofs\"/q' {file} | pup 'a[href] attr{{href}}'", shell=True)
        except subprocess.CalledProcessError as e:
            print(e.returncode)
            print(e.output)
            exit()

        # clean output and remove duplicates
        links = set(output.decode('utf-8').strip().split('\n'))
        print(f"linked articles: {links}")

        contents = []

        # copy contents
        with open(file, "r") as openFile:
            contents = openFile.readlines()

        # insert links
        with open(file, "w") as openFile:
            for line in contents:
                openFile.write(line)
                if "id=\"dependencies\"" in line:
                    openFile.write("<ol>\n")
                    for link in links:
                        if link != "":
                            name = link.removeprefix("./articles/").removesuffix(".html")
                            openFile.write(f"<li><a href=\"{name}.html\">{name}</a></li>\n")
                    openFile.write("</ol>\n")
        
        # add file link to dependencies' pages
        for link in links:
            if link != "":
                linkedFile = os.path.join(directory, link)

                # read contents
                with open(linkedFile) as openFile:
                    contents = openFile.readlines()
                
                # update and write contents
                with open(linkedFile, "w") as openFile:
                    for line in contents:
                        openFile.write(line)
                        if "id=\"dependents\"" in line:
                            name = file.removeprefix("./articles/").removesuffix(".html")
                            openFile.write(f"</li><a href=\"{name}.html\">{name}</a></li>")
