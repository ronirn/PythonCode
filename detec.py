import cv2
import mediapipe as mp

# Inisialisasi detektor tangan
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Buka kamera laptop
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Ganti BGR (Blue-Green-Red) menjadi RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Deteksi tangan
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Hitung jumlah jari yang terangkat
            finger_count = 0
            if landmarks.landmark[4].y < landmarks.landmark[3].y:
                finger_count += 1
            if landmarks.landmark[8].y < landmarks.landmark[7].y:
                finger_count += 1
            if landmarks.landmark[12].y < landmarks.landmark[11].y:
                finger_count += 1
            if landmarks.landmark[16].y < landmarks.landmark[15].y:
                finger_count += 1
            if landmarks.landmark[20].y < landmarks.landmark[19].y:
                finger_count += 1

            # Tampilkan hasil
            cv2.putText(frame, f'Jari Terangkat: {finger_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Gambar landmark tangan
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

    # Tampilkan frame
    cv2.imshow('Deteksi Jari', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
