import cv2
import requests

api_key = 'ooAvEPrs8sINdHewmyih5ZmHs_snvaxd'
api_secret = 'j-GEgmL6JgTLXzS0LU3gA9a7Xwk0P7_q'

url = 'https://api-us.faceplusplus.com/facepp/v3/detect'

emocao_cores = {
    'happy': (0, 255, 255),    # Amarelo
    'sad': (255, 0, 0),        # Azul
    'angry': (0, 0, 255),      # Vermelho
    'surprised': (255, 182, 193),  # Rosa
    'disgusted': (169, 169, 169),  # Cinza
    'fear': (128, 0, 128),     # Roxo
    'neutral': (255, 255, 255) # Branco
}

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

cap.set(3, 640)  
cap.set(4, 480)  

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        image_path = 'captura.jpg'
        cv2.imwrite(image_path, frame)

        with open(image_path, 'rb') as image_file:
            files = {'image_file': image_file}
            data = {'api_key': api_key, 'api_secret': api_secret, 'return_attributes': 'emotion'}
            response = requests.post(url, data=data, files=files)

        result = response.json()
        if 'faces' in result:
            emotions = result['faces'][0]['attributes']['emotion']
            emotion = max(emotions, key=emotions.get)
            emotion_score = emotions[emotion]
            
            print(f"Emoção detectada: {emotion} ({emotion_score*100:.2f}%)")

            color = emocao_cores.get(emotion, (255, 255, 255))  

            cv2.putText(frame, f"{emotion.capitalize()}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
            cv2.rectangle(frame, (0, 0), (640, 480), color, 10)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
