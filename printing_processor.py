import win32print
import win32api
import os
import time

# So how do I want to automate this process:
# Loop over processed_menus folder/directory
# For each file in the folder, print the file
# wait for 5 seconds
# repeat the process


def test_pdf_print():
    # Get default printer
    printer_name = win32print.GetDefaultPrinter()
    print(f"Using printer: {printer_name}")

    win32print.SetDefaultPrinter(printer_name)

    for file in os.listdir("./processed_menus"):
        print(f"Printing file: {file}")
        try:
            win32api.ShellExecute(
                0,              # Handle (0 means no parent window)
                "print",        # Operation
                file,           # File to print
                None,           # Parameters (none needed)
                "./processed_menus",  # Working directory (current)
                0               # Show command (0 = hide)
            )
            print("Print command sent successfully")
        except Exception as e:
            print(f"Error while printing: {str(e)}")
        time.sleep(5)

if __name__ == "__main__":
    test_pdf_print()