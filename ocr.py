import cv2
import pytesseract


# Tesseract OCR ka location
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# Input image
image_path = "sample_text.png"

# Image load karo
image = cv2.imread(image_path)

if image is None:
    print("ERROR: sample_text.png nahi mili.")
    print("Make sure image project folder ke andar hai.")
    exit()


# 1. Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 3. Adaptive Thresholding
threshold = cv2.adaptiveThreshold(
    blur,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)


# OCR data with confidence
data = pytesseract.image_to_data(
    threshold,
    output_type=pytesseract.Output.DICT
)


print("\n========== OCR RESULT ==========\n")

confidences = []
recognized_words = []

for i in range(len(data["text"])):
    text = data["text"][i].strip()

    try:
        confidence = float(data["conf"][i])
    except ValueError:
        confidence = -1

    if text and confidence >= 0:
        recognized_words.append(text)
        confidences.append(confidence)
        print(f"{text}  | Confidence: {confidence:.2f}%")


# Average confidence
if confidences:
    average_confidence = sum(confidences) / len(confidences)

    print("\n--------------------------------")
    print(f"Average Confidence: {average_confidence:.2f}%")

    if average_confidence >= 80:
        print("Recognition Status: PASSED")
        print("Confidence is above the 80% threshold.")
    else:
        print("Recognition Status: BELOW THRESHOLD")
        print("Confidence is below the 80% threshold.")
else:
    print("No text was recognized.")


# Complete recognized text
print("\n========== RECOGNIZED TEXT ==========\n")
print(" ".join(recognized_words))

# Save processed image
cv2.imwrite("processed_image.png", threshold)

print("\nProcessed image saved as: processed_image.png")