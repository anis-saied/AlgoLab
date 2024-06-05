import fitz #pip install PyMuPDF
from fitz.utils import getColor # "getColor" is the only method you really need
from pypdf import PdfReader
from pypdf import PdfWriter
from pypdf.generic import AnnotationBuilder
import os

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


red  = (1,0,0)  # some colors
gold = (1,1,0)
blue = (0,0,1)

text = "https://devoirs-prepa.blogspot.com"  # Texte à ajouter
for file in L:
    doc = fitz.open(file)  # new or existing PDF
    for page in doc:
        # Get the page object
        #page = doc[i]
        
        # Obtenir les dimensions de la page
        page_width = page.rect.width
        page_height = page.rect.height
        
        shape = page.new_shape()
        shape.insert_text((page_width/3,page_height-10), text,color=(0, 0, 1), border_width=1, rotate=0)
        shape.commit()  # write all stuff to page /Contents



    # Save the modified PDF file
    file=file[:file.index(".pdf")]
    doc.save(file+"out.pdf")

    # Close the PDF file and image file
    doc.close()



