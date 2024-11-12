import cv2

def detect_logo(image_path, cascade_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    logo_cascade = cv2.CascadeClassifier(cascade_path)
    logos = logo_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in logos:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Logo Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
detect_logo('path_to_image.jpg', 'path_to_haar_cascade.xml')
