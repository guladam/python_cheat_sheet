import os


PDF_DIR = "_pdf/"


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
    cwd = os.getcwd()
    pdf_dir = os.path.join(cwd, PDF_DIR)
    for name, path in md_files.items():
        os.chdir(os.path.join(cwd, os.path.dirname(path)))
        html = name.split(".")[0] + ".html"
        pdf = pdf_dir + name.split(".")[0] + ".pdf"
        os.system("grip {} --export {}".format(name, html))
        os.system("weasyprint {} {}".format(html, pdf))


if __name__ == "__main__":
    main()