import os
from doc_processor import process_document
from pdf_processor import process_all_menus
from printing_processor import test_pdf_print
import time

def main():
    """
    Main orchestration function that runs the entire menu automation process.
    This function coordinates document processing, PDF generation, and printing
    in a sequential manner, with error handling at each step.
    """
    try:
        print("\n=== Starting Menu Automation Process ===\n")

        # Step 1: Process Word document into JSON
        print("Step 1: Processing Word document...")
        process_document('input_files/menus.docx')
        print("✓ Word document processed successfully\n")

        # Step 2: Generate PDFs for each resident
        print("Step 2: Generating PDF menus...")
        process_all_menus()
        print("✓ PDF menus generated successfully\n")

        # Step 3: Print all generated PDFs
        print("Step 3: Printing menus...")
        print("Note: There will be a 5-second delay between each print job")
        test_pdf_print()
        print("✓ Print jobs completed\n")

        print("=== Menu Automation Process Completed Successfully ===")

    except Exception as e:
        print(f"\nError: The automation process encountered an error:")
        print(f"  {str(e)}")
        print("\nPlease check the input files and try again.")

if __name__ == "__main__":
    main()