from pypdf import PdfReader
from pypdf import PdfWriter
from pypdf.generic import AnnotationBuilder

URL = "devoirs-prepa.blogspot.com"
# Set the location of the resource folder
RESOURCE_ROOT = 'D:/'
file = 'DS-2_2022-23_v1.1.pdf'
pdf_path = os.path.join(RESOURCE_ROOT, file)
reader = PdfReader(pdf_path)
number_pages = len(reader.pages)

writer = PdfWriter()

for i in range(number_pages):
    page = reader.pages[i]
    writer.add_page(page)
    writer.add_blank_page()
    print(f"writer len pages : {len(writer.pages)}")

print(f"pages : {number_pages}")
meta=reader.metadata
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

# Get the page dimensions
page_width = page.mediabox[3]
page_height = page.mediabox[3]

# Create a new rectangle annotation at the bottom of the page
rect = (60, 20, page_width/3+20, 40)

# Create a new link annotation with a border
annotation = AnnotationBuilder.link(
    #[xLL, yLL, xUR, yUR]
    rect=rect,
    url="https://"+URL,
    
)
writer.add_annotation(page_number=0, annotation=annotation)

# Create the annotation and add it
annotation = AnnotationBuilder.free_text(
    URL,
    rect=rect,
    font="consolas",
    bold=True,
    italic=True,
    font_size="16pt",
    font_color="E34234", #Vermillion (from https://htmlcolorcodes.com/colors/vermillion/)
    border_color="DAF7A6",
    background_color="DAF7A6",
)
writer.add_annotation(page_number=0, annotation=annotation)

# Save the new PDF to a file
with open("meta-pdf.pdf", "wb") as f:
    writer.write(f)
