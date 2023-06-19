import tkinter as tk
import cv2
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Set up the webcam
cap = cv2.VideoCapture(0)

def predict_face(frame):
    # Resize and crop the image to 224x224
    resized_frame = cv2.resize(frame, (224, 224))
    image = Image.fromarray(resized_frame).convert("RGB")
    image = ImageOps.fit(image, (224, 224), Image.ANTIALIAS)

    # Turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Return the predicted class and confidence score
    return class_name[2:], confidence_score

def check_for_face():
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Predict the face in the frame
    predicted_class, confidence_score = predict_face(frame)
    print(predicted_class)
    # If a face is recognized, stop showing the face logo and show the recognized face instead
    if predicted_class.strip() == "Class 1":
        logo_label.pack_forget()
        face_label.configure(image=frame_to_image(frame))
        face_label.pack()
        print("hello")
        # Release the capture
        cap.release()

        return
        
    else:
    
        face_label.pack_forget()
        logo_label.pack()

    # Schedule the check_for_face function to be called again after 10 milliseconds
    root.after(10, check_for_face)

def frame_to_image(frame):
    # Convert the frame from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert the frame to an ImageTk-compatible format
    pil_image = Image.fromarray(rgb_frame)
    image = pil_image.resize((640, 480), Image.ANTIALIAS)
    return tk.PhotoImage(image=image)

# Create the tkinter window and labels for the face logo and recognized face
root = tk.Tk()
root.geometry("640x480")
logo_image = tk.PhotoImage(file="face_logo B.gif")
logo_label = tk.Label(root, image=logo_image)
face_image=tk.PhotoImage(file="face_logo A.gif")
face_label = tk.Label(root,image=face_image)

# Start checking for faces
check_for_face()

# Start the tkinter event loop
root.mainloop()


