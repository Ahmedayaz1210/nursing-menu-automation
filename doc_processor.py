import docx
import json


def clean_docx(doc, residents):
    for para in doc.paragraphs:
        
        if para.text.strip() and not para.text.__contains__('Residents on Selective Menu:'):
            parts = para.text.split('Rm.')
            if len(parts) == 2:  # Make sure we found "Rm."
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