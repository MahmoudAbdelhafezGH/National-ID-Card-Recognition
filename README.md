# National ID Card Recognition System

## Project Overview

In this Capstone project, the development of a National ID Card Recognition system using OCR (Optical Character Recognition) technology was explored. The project focused on the utilization of Tesseract OCR, a renowned open-source OCR engine, for accurately recognizing and extracting text from images of national ID cards. Additionally, OpenCV, a powerful open-source computer vision library, widely used for preprocessing the images, enhancing their quality for improved text recognition. The project aims to provide practical experience with OCR and computer vision techniques, which are pivotal in the realm of artificial intelligence.

## Key Components

- **Tesseract OCR**: Utilized for the OCR process to recognize text from ID card images.
- **OpenCV**: Played a crucial role in preprocessing images, thereby enhancing the OCR's accuracy. Techniques such as Find Contours were applied to isolate the ID card in the image, adjust its perspective, and enhance its readability.

## Project Goals

- Development of a generic codebase capable of handling various formats of national ID cards.
- Preprocessing images using OpenCV to optimize them for text recognition.
- Utilization of Tesseract OCR to extract text from preprocessed images.
- Structuring the extracted text into a readable and organized format using a pandas DataFrame.

## Steps

1. **Setup and Installation**: The project began with the setup of Tesseract OCR and OpenCV in the development environment. All necessary libraries and dependencies were installed.

2. **Image Preprocessing**:
   - OpenCV was utilized to load ID card images.
   - Preprocessing steps such as grayscale conversion, noise reduction, and edge detection were implemented.
   - The Find Contours method was applied to accurately isolate the ID card from the background and adjust its perspective.

3. **Text Recognition with Tesseract OCR**:
   - Preprocessed images were passed to Tesseract OCR for text extraction.
   - Tesseract's parameters were fine-tuned to improve accuracy for the specific layout and text style of national ID cards.

4. **Data Structuring**:
   - The extracted text was organized into a structured format.
   - pandas DataFrame was used to store the recognized information in a clear and accessible way, such as Name, Date of Birth, etc.

5. **Testing and Validation**:
   - The system was tested with a variety of national ID card images to ensure reliability and accuracy.
   - The extracted data was validated against known information to assess the OCR's performance.
