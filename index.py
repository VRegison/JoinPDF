import PyPDF2
import os

merge = PyPDF2.PdfMerger()

list_files = os.listdir('files')
list_files.sort()


for file in list_files:
   if ".pdf" in file:
      merge.append(f"files/{file}")
merge.write("result/final.pdf ")