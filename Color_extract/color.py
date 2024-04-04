import sys
import os
import cv2
import numpy as np
import pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Skin_detect.skin_detect_v2 import *

def extract_rgb(mask, path):
    img = cv2.imread(path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    points = np.argwhere(mask)
    return rgb_img[points[:, 0], points[:, 1], :]

def extract_hsv(mask, path):
    img = cv2.imread(path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    points = np.argwhere(mask)
    return hsv_img[points[:, 0], points[:, 1], :]

def extract_ycrcb(mask, path):
    img = cv2.imread(path)
    ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    points = np.argwhere(mask)
    return ycrcb_img[points[:, 0], points[:, 1], :]

def extract_lab(mask, path):
    img = cv2.imread(path)
    lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    points = np.argwhere(mask)
    return lab_img[points[:, 0], points[:, 1], :]

def save_data_csv(df, csv_path):
    df.to_csv(path_or_buf = csv_path, mode='w', index = False)

def make_ycrcb_data(csv_path, folder_name):
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

    df = pd.read_csv(csv_path)

    # columns 명의 공백 제거
    df.columns = [x.replace(' ', '') for x in df.columns]

    # label이 포함된 경우 추출
    label = []
    if df.columns[-1] == "label":
        label = df['label']
        df.drop(columns='label', inplace=True)

    Y = [0] * len(df)
    Cr = [0] * len(df)
    Cb = [0] * len(df)

    for idx, file in enumerate(df['filename']):
        # 색상정보 검출할 파일 경로
        path = os.path.join(os.getcwd(), folder_name, "train", file)
        total_feat_mask = get_mask(path)

        face_mask = get_feature_mask(total_feat_mask, FaceFeature.FACE)
        nose_mask = get_feature_mask(total_feat_mask, FaceFeature.NOSE)

        face_nose_mask = combine_feature(face_mask, nose_mask)

        binary_mask = (face_nose_mask >= 0.5).astype(int) 

        face_img = extract_feature(path, binary_mask)

        ycrcb = extract_ycrcb(face_img, path)

        ycrcb_mean = ycrcb.mean(axis=0).round()

        Y[idx] = ycrcb_mean[0]
        Cr[idx] = ycrcb_mean[1]
        Cb[idx] = ycrcb_mean[2]

        print("진행률 : {} / {}\n".format(idx, len(df)))

    ycrcb_data = {'Y' : Y, 'Cr' : Cr, 'Cb': Cb}
    ycrcb_df = pd.DataFrame(ycrcb_data)

    total_df = pd.concat([df, ycrcb_df], axis=1, ignore_index=False)

    if len(label) != 0:
        total_df['label'] = label
    return total_df

def make_hsv_data(csv_path, folder_name):
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

    df = pd.read_csv(csv_path)

    # columns 명의 공백 제거
    df.columns = [x.replace(' ', '') for x in df.columns]

    # label이 포함된 경우 추출
    label = []
    if df.columns[-1] == "label":
        label = df['label']
        df.drop(columns='label', inplace=True)

    H = [0] * len(df)
    S = [0] * len(df)
    V = [0] * len(df)

    for idx, file in enumerate(df['filename']):
        # 색상정보 검출할 파일 경로
        path = os.path.join(os.getcwd(), folder_name, "train", file)
        total_feat_mask = get_mask(path)

        face_mask = get_feature_mask(total_feat_mask, FaceFeature.FACE)
        nose_mask = get_feature_mask(total_feat_mask, FaceFeature.NOSE)

        face_nose_mask = combine_feature(face_mask, nose_mask)

        binary_mask = (face_nose_mask >= 0.5).astype(int)

        face_img = extract_feature(path, binary_mask)

        hsv = extract_hsv(face_img, path)

        hsv_mean = hsv.mean(axis=0).round()

        H[idx] = hsv_mean[0]
        S[idx] = hsv_mean[1]
        V[idx] = hsv_mean[2]

        print("진행률 : {} / {}\n".format(idx, len(df)))

    hsv_data = {'H' : H, 'S' : S, 'V': V}
    hsv_df = pd.DataFrame(hsv_data)

    total_df = pd.concat([df, hsv_df], axis=1, ignore_index=False)

    if len(label) != 0:
        total_df['label'] = label
    return total_df

def make_rgb_data(csv_path, folder_name):
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

    df = pd.read_csv(csv_path)

    # columns 명의 공백 제거
    df.columns = [x.replace(' ', '') for x in df.columns]

    # label 포함 data일 시 label 추출
    label = []
    if df.columns[-1] == "label":
        label = df['label']
        df.drop(columns='label', inplace=True)

    # rgb 색상 저장할 list 생성
    red = [0] * len(df)
    green = [0] * len(df)
    blue = [0] * len(df)

    for idx, file in enumerate(df['filename']):
        # 색상정보 검출할 파일 경로
        path = os.path.join(os.getcwd(), folder_name, "train", file)
        total_feat_mask = get_mask(path)

        face_mask = get_feature_mask(total_feat_mask, FaceFeature.LEFT_EYE)
        nose_mask = get_feature_mask(total_feat_mask, FaceFeature.RIGHT_EYE)

        face_nose_mask = combine_feature(face_mask, nose_mask)

        binary_mask = (face_nose_mask >= 0.5).astype(int)

        face_img = extract_feature(path, binary_mask)

        rgb = extract_rgb(face_img, path)

        rgb_mean = rgb.mean(axis=0).round()

        red[idx] = rgb_mean[0]
        green[idx] = rgb_mean[1]
        blue[idx] = rgb_mean[2]

        print("진행률 : {} / {}\n".format(idx, len(df)))

    rgb_data = {'Eye_Red' : red, 'Eye_Green' : green, 'Eye_Blue': blue}
    rgb_df = pd.DataFrame(rgb_data)

    total_df = pd.concat([df, rgb_df], axis=1, ignore_index=False)
    if len(label) != 0:
        total_df = pd.concat([total_df, label], axis=1, ignore_index=False)

    return total_df

def make_lab_data(csv_path, folder_name):
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

    df = pd.read_csv(csv_path)

    # columns 명의 공백 제거
    df.columns = [x.replace(' ', '') for x in df.columns]

    # label이 포함된 경우 추출
    label = []
    if df.columns[-1] == "label":
        label = df['label']
        df.drop(columns='label', inplace=True)

    L = [0] * len(df)
    A = [0] * len(df)
    B = [0] * len(df)

    for idx, file in enumerate(df['filename']):
        # 색상정보 검출할 파일 경로
        path = os.path.join(os.getcwd(), folder_name, "train", file)
        total_feat_mask = get_mask(path)

        face_mask = get_feature_mask(total_feat_mask, FaceFeature.FACE)
        nose_mask = get_feature_mask(total_feat_mask, FaceFeature.NOSE)

        face_nose_mask = combine_feature(face_mask, nose_mask)

        binary_mask = (face_nose_mask >= 0.5).astype(int)

        lab = extract_lab(binary_mask, path)

        lab_mean = lab.mean(axis=0).round()

        L[idx] = lab_mean[0]
        A[idx] = lab_mean[1]
        B[idx] = lab_mean[2]

        print("진행률 : {} / {}\n".format(idx, len(df)))

    lab_data = {'L' : L, 'A' : A, 'B' : B}
    lab_df = pd.DataFrame(lab_data)

    total_df = pd.concat([df, lab_df], axis=1, ignore_index=False)

    if len(label) != 0:
        total_df['label'] = label

    return total_df