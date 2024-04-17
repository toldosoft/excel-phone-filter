# Excel Phone Filter

## Overview
This Python script filters out specific phone numbers from an Excel spreadsheet and saves the result in a new file. It is designed to manage and clean contact lists or any other data where phone numbers need to be filtered out.

## Features
- **Read Excel File**: Uses Pandas to read an Excel file.
- **Filter Phone Numbers**: Filters out specified phone numbers.
- **Write Excel File**: Saves the filtered data back to an Excel file without the filtered phone numbers.

## Requirements
- Python 3.x
- Pandas library
- Openpyxl library

## Setup
1. **Install Required Libraries**:
   ```bash
   pip install pandas openpyxl
   ```

2. **Prepare Your Data**:
   - Ensure your Excel file (`excel.xlsx`) is in the `xlsx_files` directory and formatted correctly.
   - The spreadsheet must contain a column named `phone` with the phone numbers.

## Usage
- Execute the script to filter the phone numbers and generate a new Excel file:
  ```bash
  python app.py
  ```

## Output
- The result will be saved in a file named `resul.xlsx` in the same directory, with the specified phone numbers removed from the `phone` column.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
