
# Nursing Menu Automation System

A Python-based automation system designed to streamline the process of adding resident information to weekly menu templates and managing their distribution in healthcare facilities.

## Overview

This system automates three main tasks:
1. Processing resident information from a structured Word document
2. Adding resident names and room numbers to existing menu template PDFs
3. Automating the printing process for efficient distribution

## System Components

### Document Processing (`doc_processor.py`)
Extracts resident information (names, room numbers, and diet types) from a structured Word document and converts this data into a standardized JSON format for further processing.

### PDF Processing (`pdf_processor.py`)
Takes the existing menu template PDFs (House and Ground diet versions) and adds resident names and room numbers to them. The system selects the appropriate template based on each resident's diet type and organizes the output files by room numbers.

### Print Automation (`printing_processor.py`)
Handles the automated printing of the processed menu PDFs, implementing timed delays between print jobs to ensure reliable printer operation.

### Main Controller (`main.py`)
Coordinates all three processes in sequence, providing a single-command solution for the entire workflow.


## Important Note

Due to HIPAA compliance requirements, all example documents and patient information have been removed from this repository.
## Requirements

- Python 3.x
- Required libraries:
  - python-docx (for Word document processing)
  - PyPDF2 (for PDF manipulation)
  - reportlab (for adding text to PDFs)
  - pywin32 (for print automation)
    
---
*This system was developed to enhance operational efficiency while maintaining strict compliance with healthcare information management requirements.*
