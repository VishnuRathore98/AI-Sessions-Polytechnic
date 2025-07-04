import cv2
import numpy as np

# Read the original image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found. Please check the filename.")
    exit()

# Save a copy of the original image
original = img.copy()

def apply_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_sepia(image):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepia = cv2.transform(image, kernel)  
    return np.clip(sepia, 0, 255).astype(np.uint8) 

def apply_blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)

def overlay_text(image, text="Sample Text"):
    result = image.copy()
    cv2.putText(result, text, (30, 60), cv2.FONT_HERSHEY_SIMPLEX,
                2, (0, 255, 0), 3)
    return result

while True:
    print("\n Photo Editor Menu:")
    print("1. Grayscale Filter")
    print("2. Sepia Filter")
    print("3. Blur Effect")
    print("4. Add Text Overlay")
    print("5. Save & Exit")
    print("6. Reset to Original")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        img = apply_grayscale(img)
        cv2.imshow("Grayscale", img)

    elif choice == "2":
        img = apply_sepia(img)
        cv2.imshow("Sepia", img)

    elif choice == "3":
        img = apply_blur(img)
        cv2.imshow("Blur", img)

    elif choice == "4":
        text = input("Enter text to overlay: ")
        img = overlay_text(img, text)
        cv2.imshow("Text Overlay", img)

    elif choice == "5":
        filename = input("Enter filename to save (e.g., edited.jpg): ")
        # Save the edited image, not the original
        cv2.imwrite(filename, img)
        print(f"Image saved as {filename}")
        break

    elif choice == "6":
        img = original.copy()
        print("Image reset to original.")
        cv2.imshow("Original", img)

    else:
        print("Invalid choice. Please select a valid option.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
