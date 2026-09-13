import pypdf
quet=''#to temporarily store a question
quep=''#to premanently store a question
reader=pypdf.PdfReader('as2.pdf')
for page in reader.pages:
    words=page.extract_text(extraction_mode='layout')
    lines=words.split('\n')
    for line in lines:
        match line[0:2]:
            case x if x.endswith('.'):
                quep=quet
                quet=''
                quet+=line
                print(quep+'!!!!!')
            case _:
                quet+=line+'\n'
print(quet,'!!!!') #to print out any value that is left in quet at the end 
            




#programme can separate out each question
#work on user input answer writing 
                

    

        
    