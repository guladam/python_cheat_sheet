import os

PDF_DIR = ".\\_pdf\\"

def main():
    walk_directories()


def walk_directories():
    markdown_files = {}
    
    # Walk through all available files
    for root, dirs, files in os.walk(".", topdown = False):
        for name in files:
            # We grab the markdown filepaths
            if name != "README.md" and name.endswith(".md"):
                markdown_files[name] = os.path.join(root, name)
    
    # We update the markdowns with the appropriate metadata
    convert_md_to_pdf(markdown_files)


def convert_md_to_pdf(md_files):
    for name, path in md_files.items():
        pdf = PDF_DIR + name.split(".")[0] + ".pdf"
        print(pdf)
        os.system("pandoc {} -f markdown -t pdf -s -o {}".format(path, pdf))


if __name__ == "__main__":
    main()