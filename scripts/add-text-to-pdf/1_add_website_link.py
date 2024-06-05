from pypdf import PdfReader
from pypdf import PdfWriter
from pypdf.generic import AnnotationBuilder
import os

URL = "    devoirs-prepa.blogspot.com"

# Set the location of the resource folder
root = "C:/Users/DELL/OneDrive - Ministere de l'Enseignement Superieur et de la Recherche Scientifique/projects/devoirs-prepa/pdf devoirs-prepa in drive/"
# "C:\\Users\\DELL\\Downloads\\books"
#path = root+"info/2ème année/DS1/ipein/2016-17"
path="."
os.chdir(path)

# recupérer liste des noms des fichiers
L = os.listdir()

# filter files : take only pdf files
L = list(filter(lambda file_name: '.pdf' in file_name, L))

for file in L:
    print(file)
    reader = PdfReader(file)
    number_pages = len(reader.pages)
    print(f"file : {file} ...")

    writer = PdfWriter()
    meta = reader.metadata
    # Add the metadata
    writer.add_metadata(
        {
            "/Author": URL,
            "/Producer": URL,
            "/creator": URL,
            "/subject": "Epréuve prépa tunisie",
            "/title": "Epréuve prépa tunisie",
        }
    )    
    for i in range(number_pages):
        page = reader.pages[i]
        writer.add_page(page)



        # Get the page dimensions
        page_width = page.mediabox[3]
        page_height = page.mediabox[3]

        # Create a new rectangle annotation at the bottom of the page
        # [xLL, yLL, xUR, yUR]
        rect = (180, 10, page_width/2+20, 27)

        # Create a new link annotation with a border
        annotation = AnnotationBuilder.link(
            rect=rect,
            url="https://devoirs-prepa.blogspot.com"
            #"https://"+URL.strip(),
        )
        
        writer.add_annotation(page_number=i, annotation=annotation)

        # Create the annotation and add it
        annotation = AnnotationBuilder.free_text(
            URL,
            rect=rect,
            font="consolas",
            bold=True,
            italic=True,
            font_size="14pt",
            # Vermillion (from https://htmlcolorcodes.com/colors/vermillion/)
            font_color="E34234",
            border_color="DAF7A6",
            background_color="DAF7A6",
        )
        #writer.add_annotation(page_number=i, annotation=annotation)

    # Save the new PDF to a file
    file=file[:file.index(".pdf")]
    with open(file+".pdf", "wb") as f:
        writer.write(f)
