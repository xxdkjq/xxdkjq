from cv2 import WINDOW_NORMAL
from em_model import EMR
import cv2
import time
from face_detect import find_faces
from image_commons import nparray_as_image, draw_with_alpha


def _load_emoticons(emotions):
    """
    carga los emojis desde la carpeta.
    :param emotions: Lisa con el nombre de la emociones.
    :return: lista de los emojis.
    """
    return [nparray_as_image(cv2.imread('graphics/%s.png' % emotion, -1), mode=None) for emotion in emotions]



def show_webcam_and_run(model, emoticons, window_size=None, window_name='webcam', update_time=10):
    """
    Muestra la webcam y detecta los rostros y las emociones en tiempo real para dibujar los emojis.
    :param model: Modelo para reconocer emociones.
    :param emoticons: emojis.
    :param window_size: tamao de la ventana donde estara el stream.
    :param window_name: Nombre de la ventana.
    :param update_time: tiempo para actualizar la imagen.
    """
    cv2.namedWindow(window_name, WINDOW_NORMAL)
    if window_size:
        width, height = window_size
        cv2.resizeWindow(window_name, width, height)

    vc = cv2.VideoCapture(0)  # http://192.168.0.2:4747/mjpegfeed para camara android remota por medio de Droidcam
    vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


    if vc.isOpened():
        read_value, webcam_image = vc.read()

    else:
        print("[ERROR] No se enontro camara.")
        return

    while read_value:
        for normalized_face, (x, y, w, h) in find_faces(webcam_image):

            prediction = network.predict(normalized_face)  # hace la prediccion
            prediction = prediction[0]  # guarda el numero de la emocion para diujar el emoji
            # carga el emoji para dibujarlo
            image_to_draw = emoticons[prediction.tolist().index(max(prediction))]
            # dibuja el emoji
            draw_with_alpha(webcam_image, image_to_draw, (x, y, w, h))#image_to_draw,  ,  webcam_image,

        cv2.imshow(window_name, webcam_image)
        read_value, webcam_image = vc.read()
        key = cv2.waitKey(update_time)

        if key == 27:  # salir con esc
            break

    cv2.destroyWindow(window_name)


if __name__ == '__main__':
    # lista de emociones
    emotions = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']
    # emojis
    emoticons = _load_emoticons(emotions)
    # crea la red 
    network = EMR()
    network.build_network()

    # ejecuta la app
    window_name = "faceDetect emojis"
    show_webcam_and_run(network,emoticons, window_size=(1920, 1080), window_name=window_name, update_time=30)


