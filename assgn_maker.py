#program automates the making of your submitttion assigment to a degree that you only have to enter your name,
#roll no, answer to each question question as it is displayed one by one 
#program arranges questions and answers just as nirnay sir told to do
#program recognizes quesion by the format by whuch the begin
#in this program, it read the file and separates the question based on the 'x.' with which they begin 
#if the file were to have questions that began with, say 'x)', it wouldnt recognize that and the program
#will fail to function
#will improve if need be in future
import pypdf
from docx import Document
def q1by1(file):
    doc=Document()
    nam=input('Your Name: ')
    rno=input('your roll no. (like 20XXYYYXXX):')
    doc.add_paragraph(nam+'\n'+rno)
    lines_t='' #to temporarily store some lines
    lines_p='' #to premanently store some lines
    reader=pypdf.PdfReader(file)
    for page in reader.pages:
        words=page.extract_text(extraction_mode='layout')
        lines=words.split('\n')
        for line in lines:
            que_no=line[0:2]
            match que_no:
                case x if x.endswith('.'):
                    lines_p=lines_t
                    lines_t=''
                    lines_t+=line
                    print(lines_p)
                    doc.add_paragraph(lines_p)
                    match lines_p[0:2]:
                        case x if x.endswith('.'):
                            ans=input(f'answer to ques {lines_p[0:2]}: ')
                            doc.add_paragraph('==> '+ans+'\n\n')
                case _:
                    lines_t+=line+'\n'
    print(lines_t) #to print out any value that is left in quet at the end 
    doc.add_paragraph(lines_t)
    match lines_t[0:2]:
        case x if x.endswith('.'):
            ans=input(f'answer to ques {lines_t[0:2]}: ')
            doc.add_paragraph('==> '+ans)
    doc.save('tosubmit.docx')


f=input('file name: ')
q1by1(f)