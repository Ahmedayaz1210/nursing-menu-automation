import docx
import json


def clean_docx(doc, residents):
    """
    This function takes a docx file and a list of residents as input and extracts the residents' information from the docx file.
    The function then appends the residents' information to the list of residents.
    """

    for para in doc.paragraphs:
        if para.text.strip() and not para.text.__contains__('Residents on Selective Menu:'):
            
            # Split the text into two parts: Patient Name and Room Number/Diet Type
            parts = para.text.split('Rm.')
            # If the text contains 'Rm.' then it has two parts
            if len(parts) == 2:  
                # Split the second part into Room Number and Diet Type
                room_diet = parts[1].strip() 
                room_diet_parts = room_diet.split()
                resident = {
                    "Patient Name": parts[0].replace(",","").strip(),
                    "Room Number": room_diet_parts[0].strip(),
                    "Diet Type": room_diet_parts[1].strip()
                }
                residents.append(resident)

    return residents
                
                    

doc = docx.Document('input_files/menus.docx')
residents = []
clean_docx(doc, residents)


with open('menus.json', 'w') as f:
    json.dump(residents, f, indent=4)