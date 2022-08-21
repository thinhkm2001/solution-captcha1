import numpy as np
import cv2
import base64

from flask import *
from solution import PuzleSolver

def base64_to_cv2(im_b64: str):
    im_bytes = base64.b64decode(im_b64)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return img

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def solutionCaptcha_process():
    if request.method == 'POST': 
        bg_base64 = request.form.get('bg_base64')
        block_bg_base64 = request.form.get('block_bg_base64')

        piece = base64_to_cv2(block_bg_base64)
        background = base64_to_cv2(bg_base64)

        result = PuzleSolver(background, piece)

        return result.get_position()
        
    else:
        return "Server OK"

# Start Backend

if __name__ == '__main__':
    app.run()
