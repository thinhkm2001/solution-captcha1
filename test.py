from solution import PuzleSolver
import cv2

bg = cv2.imread('./test/bg.png', cv2.IMREAD_COLOR)
bock_bg = cv2.imread('./test/bock_bg.png', cv2.IMREAD_COLOR)

solver = PuzleSolver(background=bg, piece=bock_bg)
print(solver.get_position())