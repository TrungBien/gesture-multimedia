import mediapipe as mp
import cv2
from mediapipe.tasks import python
import time
import keyboard as kb
import threading


model_path = './custom_gesture5.task'


GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode
mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_draw_styles = mp.solutions.drawing_styles




def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):

    recognized_gestures = result.gestures

    if recognized_gestures:
        # print('Gesture recognition result: {}'.format(result.gestures))
        gesture = recognized_gestures[0]
        control = gesture[0].category_name
        multimedia_controls(control)




def multimedia_controls(control):


    if control == 'A':
        kb.send(164)

        print('Play/Pause')


    elif control == 'B':

        kb.send(165)

        print('Previous')
    elif control == 'C':

        kb.send(163)

        print('Next')

    elif control == 'D':

        kb.send(113)

        print('Mute')



def delay_function():
    global delay
    while cap.isOpened():
        time.sleep(0.5)  # Adjust the delay time here
        delay += 1


delay_thread = threading.Thread(target=delay_function)
delay_thread.start()


timestamp = 0

options = GestureRecognizerOptions(
        base_options = mp.tasks.BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.LIVE_STREAM,
        result_callback=print_result)
detected = False
hands = mp.solutions.hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5)
with GestureRecognizer.create_from_options(options) as recognizer:
    cap = cv2.VideoCapture(0)
    delay = 0
    start_time = time.time()

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        timestamp += 1
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(image,
                                       hand_landmarks,
                                       mp_hands.HAND_CONNECTIONS,
                                       mp_draw_styles.get_default_hand_landmarks_style(),
                                       mp_draw_styles.get_default_hand_connections_style())



        # print('Looking for gesture... ' + str(timestamp))
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        recognizer.recognize_async(mp_image, timestamp)

        delay+=1


        cv2.imshow('Hand Tracking', cv2.flip(image, 1))

        if cv2.waitKey(5) & 0xFF == 27:

            break

    cap.release()