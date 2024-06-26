from shape_detect.utils import landmark, line, norm, ratio, vector
import pandas as pd
from torchvision.datasets import ImageFolder
from tqdm import tqdm
from shape_detect.classifier import classifier

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def get_vector(img_path):

    display_img, pos = landmark.get_landmark(img_path)#사진 랜드마크 처리

    if not pos: # 얼굴 검출 실패시 패스
        return False, False, False

    distances = line.get_line(display_img, pos)#랜드마크간 특징 거리 추출

    norm_distances = norm.get_norm(distances) #거리정보 정규화

    vectors = vector.get_vector(pos)#각도 산출을 위한 벡터 추출

    angles = vector.get_angles(vectors) #각도 추출

    rations = ratio.get_ratio(distances) #길이 간 비율 정보

    return norm_distances, angles, rations

def labeling(root, output):
    dataset = ImageFolder(root=root)

    vectors = []
    for path, label in tqdm(dataset.imgs, desc="Caculating face vector"):
        norm_distances, angles, rations = get_vector(path)

        if not norm_distances:
            continue

        vectors.append(norm_distances + rations + angles + [label])

    row = ["D1","D2","D3","D4","D5","D6","D7","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","A1","A2","A3","shape"]
    df = pd.DataFrame(vectors, columns=row)
    df.to_csv(output)
    
cls = classifier()

def get_shape(img_path):
    norm, angles, rations = get_vector(img_path)
    if not norm:
        return -1
    
    cls.set_vector(norm + angles + rations)
    return cls.get_shape()