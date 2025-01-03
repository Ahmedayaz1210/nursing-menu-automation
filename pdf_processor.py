import io  
from reportlab.pdfgen import canvas 
from PyPDF2 import PdfReader, PdfWriter  
import json
import os


def fill_pdf(input_pdf, output_pdf, data):
    """
    Takes a PDF form and fills it with patient data (name and room number).
    Handles multi-page PDFs and adds text to both left and right sides of each page.
    
    Args:
        input_pdf (str): Path to the original PDF menu template
        output_pdf (str): Path where the filled PDF should be saved
        data (dict): Contains 'name' and 'room' info to be added to the PDF
    """
    # Create a virtual PDF file in memory (like a temporary scratch pad)
    packet = io.BytesIO()
    # Create a canvas object - this is what we'll use to write text on our virtual PDF
    can = canvas.Canvas(packet)
    
    # Define where text should be placed on each page
    # Each page has left and right sides that need the same info
    page_coordinates = [
        {
            'left': {'name': (150, -462), 'room': (350, -462)},  # Left side coordinates
            'right': {'name': (500, -462), 'room': (690, -462)}  # Right side coordinates
        },
    ] * 7  # Create same coordinates for all 7 pages

    # Process each page of the PDF
    for page_num in range(len(page_coordinates)):
        # Set up text appearance for this page
        can.setFont("Helvetica", 18)  
        can.setFillColorRGB(0, 0, 0)  # Set text color to black
        can.saveState()  # Save these settings so we can restore them later
        
        # Rotate canvas 90 degrees clockwise
        # This is needed because PDFs use a different coordinate system
        can.rotate(90)
        
        # Get coordinates for left side of current page
        left_coords = page_coordinates[page_num]['left']
        # Add name and room number to left side
        can.drawString(left_coords['name'][0], left_coords['name'][1], data["name"])
        can.drawString(left_coords['room'][0], left_coords['room'][1], data["room"])
        
        # Get coordinates for right side of current page
        right_coords = page_coordinates[page_num]['right']
        # Add same name and room number to right side
        can.drawString(right_coords['name'][0], right_coords['name'][1], data["name"])
        can.drawString(right_coords['room'][0], right_coords['room'][1], data["room"])
        
        # Reset canvas rotation and move to next page
        can.restoreState()  # Undo the rotation
        can.showPage()  # Finish current page and start a new one

    # Finalize our virtual PDF with all the text
    can.save()

    # Now we need to combine our text with the original menu PDF
    packet.seek(0)  # Go back to start of our virtual PDF
    new_pdf = PdfReader(packet)  # Read our text-only PDF
    existing_pdf = PdfReader(open(input_pdf, "rb"))  # Read original menu PDF
    output = PdfWriter()  # Create a new PDF to store the combined result

    # Combine text with menu for each page
    for page in range(len(existing_pdf.pages)):
        page_obj = existing_pdf.pages[page]  # Get current page from menu
        if page < len(new_pdf.pages):
            # Overlay our text on top of the menu page
            page_obj.merge_page(new_pdf.pages[page])
        # Add the combined page to our final PDF
        output.add_page(page_obj)

    # Save the final PDF with both menu and text
    with open(output_pdf, "wb") as output_file:
        output.write(output_file)

def process_all_menus():
    """
    Process menus for all residents from JSON, organized by room number.
    This naturally groups by floor since room numbers start with floor number.
    """
    # Create output directory if it doesn't exist
    output_dir = "processed_menus"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read resident data from JSON
    with open('menus.json', 'r') as f:
        residents = json.load(f)
    
    
    for resident in residents:
        # Select template based on diet type
        template = "input_files/House.pdf" if resident["Diet Type"].lower() == "hse" else "input_files/Ground.pdf"
        
        # Create output filename with room number
        output_file = f"{output_dir}/{resident['Room Number']}_{resident['Patient Name']}_{resident['Diet Type']}_menu.pdf"
        
        fill_pdf(template, output_file, {
            "name": resident["Patient Name"],
            "room": resident["Room Number"]
        })

if __name__ == "__main__":
    process_all_menus()