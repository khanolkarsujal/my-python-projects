import hashlib
import pymupdf

def get_file_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename , "rb") as file :
        for chunk in iter(lambda:file.read(8192) , b""):
            sha256.update(chunk)

    return sha256.hexdigest()
        

def extract_text(filename):
    with pymupdf.open(filename) as document:
        return "\n".join(page.get_text() for page in document )


def compare_pdfs(pdf1, pdf2):
    if get_file_hash(pdf1) == get_file_hash(pdf2):
        return "PDFS are exactly identical"

    if extract_text(pdf1) == extract_text(pdf2):
        return "PDFS are different , but their extracted text is the same"

    return "PDFS contain different content."

print(compare_pdfs("sample.pdf" ,"sample1.pdf"))