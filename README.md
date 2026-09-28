# DecodeLabs AI Project 4

## Image and Text Recognition using OCR

This project implements a basic Optical Character Recognition (OCR)
system using Python, OpenCV, Pytesseract, and Tesseract OCR.

## Technologies Used

- Python
- OpenCV
- Pytesseract
- Tesseract OCR

## Processing Pipeline

1. Load input image
2. Convert image to grayscale
3. Apply Gaussian blur
4. Apply adaptive thresholding
5. Perform OCR
6. Calculate recognition confidence
7. Display the recognized text

## Project Objective

The objective of this project is to extract machine-readable text
from an input image using OCR techniques.

## Confidence Threshold

The project uses an 80% minimum confidence threshold
for validated OCR results.

## Files

- `ocr.py` - Main OCR program
- `sample_text.png` - Sample input image
- `processed_image.png` - Preprocessed image
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation
