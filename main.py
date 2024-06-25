#!/usr/bin/python3
print("tgrab - main.py has executed")
'''
this main.py script will attempt to read a desired .pdf file and pull all available text from it.
'''
import os
cwd = os.getcwd()
print("Current working directory: " + os.getcwd() )
if os.path.isdir(cwd + "/source_pdf"):
    print("source_pdf folder found.")
else:
    print("source_pdf folder not found.. creating")
    os.makedirs('source_pdf')


if os.path.isdir(cwd + "/output"):
    print("output folder found.")
else:
    print("output folder not found.. creating")
    os.makedirs('output')
output_path = ( cwd + "/output/")

print("Attempting to find source pdf file..")
files_in_source_pdf_directory = os.listdir(cwd + "/source_pdf")
found_pdf = [ i for i in files_in_source_pdf_directory if i.endswith('.pdf')]
print("There are " + str(len(found_pdf)) + " file(s) in source_pdf directory" )
total_files_in_found_pdf = int(0)
for i in range(len(found_pdf)):
    total_files_in_found_pdf = total_files_in_found_pdf + 1
    print('Index ' + str(i) + ' in found_pdf is: ' + found_pdf[i])
print("Found total of: " + str(total_files_in_found_pdf) + " files in source_pdf directory")
target_pdf = found_pdf[0]
print(target_pdf)

from pypdf import PdfReader

target_pdf_path = PdfReader(cwd + "/source_pdf/" + target_pdf)
#reader = PdfReader(cwd + "/source_pdf/" + target_pdf)
#number_of_pages = len(reader.pages)
#page = reader.pages[22]
#text = page.extract_text()
#print(text)

def export_from_page_range(page_min, page_max):
    min = int( page_min - 1)
    max = int( page_max )

    from pypdf import PdfReader
    pdf = PdfReader(cwd + "/source_pdf/" + target_pdf)
    export_text = ""
    for page in range(min, max):
        #print("Attempting to print page: " + str(page))
        page_string = pdf.pages[page]
        text = page_string.extract_text()
        export_text += str(text) 
        #print(text)
    return export_text 


chapt_1_questions = export_from_page_range(23, 104)
print(chapt_1_questions, file=open(output_path + 'chapter_1_questions.txt', 'w'))
chapt_1_answers = export_from_page_range(439, 495)
print(chapt_1_answers, file=open(output_path + 'chapter_1_answers.txt', 'w'))

chapt_2_questions = export_from_page_range(109, 162)
print(chapt_2_questions, file=open(output_path + 'chapter_2_questions.txt', 'w'))
chapt_2_answers = export_from_page_range(496, 536)
print(chapt_2_answers, file=open(output_path + 'chapter_2_answers.txt', 'w'))


chapt_3_questions = export_from_page_range(167, 211)
print(chapt_3_questions, file=open(output_path + 'chapter_3_questions.txt', 'w'))
chapt_3_answers = export_from_page_range(537, 569)
print(chapt_3_answers, file=open(output_path + 'chapter_3_answers.txt', 'w'))


chapt_4_questions = export_from_page_range(217, 270)
print(chapt_4_questions, file=open(output_path + 'chapter_4_questions.txt', 'w'))
chapt_4_answers = export_from_page_range(570, 614)
print(chapt_4_answers, file=open(output_path + 'chapter_4_answers.txt', 'w'))


chapt_5_questions = export_from_page_range(276, 362)
print(chapt_5_questions, file=open(output_path + 'chapter_5_questions.txt', 'w'))
chapt_5_answers = export_from_page_range(615, 663)
print(chapt_5_answers, file=open(output_path + 'chapter_5_answers.txt', 'w'))




