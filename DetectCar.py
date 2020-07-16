import cv2
import numpy as np

net = cv2.dnn.readNet("../myauto_project_data/model_data/yolov3-tiny.weights", "../myauto_project_data/model_data/yolov3-tiny.cfg")
classes = []
with open("../myauto_project_data/model_data/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
outputlayers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def detect_car(img_path : str):
    img = cv2.imread(img_path)
    if(img is None):
        return None
    img = cv2.resize(img, (416,416))
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0,0,0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(outputlayers)
    returnList = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                returnList.append((str(classes[class_id]), confidence))
                # print("found", str(classes[class_id]), "with", confidence, "percent")
    return returnList