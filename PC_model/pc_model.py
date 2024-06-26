#%%
import pandas as pd
import numpy as np
import sys
import os
import joblib

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from image_processing.gamma_correction import gamma_correction
from Skin_detect.skin_detect_v2 import *
from Color_extract.color import extract_high_rank, save_data_csv


from sklearn.model_selection import train_test_split
from PC_model.utils import *
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

from xgboost import XGBClassifier, plot_importance
from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.model_selection import StratifiedKFold

class PersonalColorModel:
    def __init__(self) -> None:
        self.xgb = XGBClassifier(objective="multi:softmax")
        self.ovr = OneVsRestClassifier(LinearRegression())
        self.ovo = OneVsOneClassifier(SVC())
        self.knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1,)
        self.lr = LogisticRegression(max_iter=5000)
        self.voting = VotingClassifier(estimators=[("xgb", self.xgb), ("knn", self.knn),
                                                   ("lr", self.lr)], voting='soft')
        self.rfc = RandomForestClassifier()


    def train(self, train_x, train_y):
        self.xgb.fit(train_x, train_y)
        self.ovr.fit(train_x, train_y)
        self.ovo.fit(train_x, train_y)
        self.knn.fit(train_x, train_y,)
        self.lr.fit(train_x, train_y)
        self.voting.fit(train_x, train_y)
        self.rfc.fit(train_x, train_y)

    def select_train(self, model, train_x, train_y):
        if model == "xgb":
            self.xgb.fit(train_x, train_y)
        elif model == "ovr":
            self.ovr.fit(train_x, train_y)
        elif model == "ovo":
            self.ovo.fit(train_x, train_y)
        elif model == "knn":
            self.knn.fit(train_x, train_y)
        elif model == "lr":
            self.lr.fit(train_x, train_y)
        elif model == "voting":
            self.voting.fit(train_x, train_y)
        elif model == "rfc":
            self.rfc.fit(train_x, train_y)
        else:
            print("선언되지 않은 모델입니다.")

    def select_test(self, model, test_x):
        if model == "xgb":
            return self.xgb.predict(test_x)
        elif model == "ovr":
            return self.ovr.predict(test_x)
        elif model == "ovo":
            return self.ovo.predict(test_x)
        elif model == "knn":
            return self.knn.predict(test_x)
        elif model == "lr":
            return self.lr.predict(test_x)
        elif model == "voting":
            return self.voting.predict(test_x)
        elif model == "rfc":
            return self.rfc.predict(test_x)
        return False
    
    def select_predict_probability(self, model, test_x):
        if model == "xgb":
            return self.xgb.predict_proba(test_x)
        elif model == "knn":
            return self.knn.predict_proba(test_x)
        elif model == "lr":
            return self.lr.predict_proba(test_x)
        elif model == "voting":
            return self.voting.predict_proba(test_x)
        elif model == "rfc":
            return self.rfc.predict_proba(test_x)
        return False

    def predict_probability(self, test_x):
        return self.xgb.predict_proba(test_x),\
            self.knn.predict_proba(test_x),\
                  self.lr.predict_proba(test_x),\
                      self.voting.predict_proba(test_x),\
                          self.rfc.predict_proba(test_x)

    def test(self, test_x):
        return self.xgb.predict(test_x),\
              self.ovr.predict(test_x),\
                  self.ovo.predict(test_x),\
                      self.knn.predict(test_x), \
                        self.lr.predict(test_x),\
                              self.voting.predict(test_x),\
                                  self.rfc.predict(test_x)
    
    def save(self):
        joblib.dump(value=self, \
                    filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "test_model.pkl"))
    
def save_model(model, path):
    try:
        joblib.dump(model, path)
        return True
    except :
        print("model 저장에 실패하였습니다.")
        return False
#%%
def model_train_save():
    train_df = pd.read_csv("/Users/ohs/Desktop/capstone/personal_color_dataset/train/data.csv")
    features = ['Hair_Red', 'Hue', 'Saturation', 'Cr', 'Cb', 'L',
            'A', 'B', 'New Blue', 'Eye_Red', 'Eye_Blue', 'New Green', 'New Red']

    train_x = train_df[features]
    train_y = train_df['label']


    m = PersonalColorModel()
    scaler = StandardScaler()

    S_kfold = StratifiedKFold(n_splits= 5, shuffle=True)
    for train_index, test_index in S_kfold.split(train_x, train_y):  
        x_train, x_test = train_x.iloc[train_index], train_x.iloc[test_index]
        y_train, y_test = train_y.iloc[train_index], train_y.iloc[test_index]

        processing_train_x = scaler.fit_transform(x_train)
        
        m.train(processing_train_x, y_train)

        processing_test_x = scaler.transform(x_test)
        cv_accuracy = []
        for res in m.test(processing_test_x):
            cv_accuracy.append(np.round(get_accuracy(y_test, res), 4))
        print(cv_accuracy)

    save_model(scaler, os.path.join(os.path.dirname(os.path.dirname(__file__)), "scaler_v2.pkl"))
    save_model(m, os.path.join(os.path.dirname(os.path.dirname(__file__)), "model_v2.pkl"))
        

# %%


# m = PersonalColorModel()
# scaler = StandardScaler()

# for train_index, test_index in S_kfold.split(train_x, train_y):  
#     x_train, x_test = train_x.iloc[train_index], train_x.iloc[test_index]
#     y_train, y_test = train_y.iloc[train_index], train_y.iloc[test_index]


#     processing_train_x = scaler.fit_transform(x_train)
#     m.train(processing_train_x, y_train)

#     # m.train(x_train, y_train)


#     processing_test_x = scaler.transform(x_test)

#     for i, res in zip(range(7), m.test(processing_test_x)):
#     # for i, res in zip(range(7), m.test(x_test)):
#         cv_accuracy[i].append(np.round(get_accuracy(y_test, res), 4))
#     print(cv_accuracy)


#%%
# colors = plt.cm.get_cmap('tab10', 7)
# matplotlib.use('module://matplotlib_inline.backend_inline')
# model_names = ["xgb", "ovr", "ovo", "knn", "lr", "voting", "rfc"]
# plt.figure()
# for idx, accuracy_list in enumerate(cv_accuracy):
#     plt.plot(range(1, len(accuracy_list) + 1), accuracy_list, marker='o', linestyle='-', label=model_names[idx])

# plt.title('Accuracy for Each Fold by Model')
# plt.xlabel('Fold')
# plt.ylabel('Accuracy')
# plt.xticks(range(1, 6))
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# plt.grid(True)
# plt.show()

#%%

# # m.train(processing_train_x, train_y)

# test_x = test_df[features]
# test_y = test_df['label']

# processing_test_x = scaler.transform(test_x)

# res_xgb, res_ovr, res_ovo, res_knn, res_lr, res_voting, res_rfc = m.test(processing_test_x)
# #     # res_xgb, res_knn, res_lr, res_voting, res_rfc = m.predict_probability(processing_test_x)

# print("xgb 평가지표")
# # print(res_xgb)
# get_evaluation(test_y, res_xgb)
# print()

# print("ovr 평가지표")
# # print(res_ovr)
# get_evaluation(test_y, res_ovr)
# print()

# print("ovo 평가지표")
# # print(res_ovo)
# get_evaluation(test_y, res_ovo)
# print()

# print("knn 평가지표")
# # print(res_knn)
# get_evaluation(test_y, res_knn)
# print()

# print("lr 평가지표")
# # print(res_lr)
# get_evaluation(test_y, res_lr)
# print()

# print("voting 평가지표")
# # print(res_voting)
# get_evaluation(test_y, res_voting)
# print()

# print("rfc 평가지표")
# # print(res_rfc)
# get_evaluation(test_y, res_rfc)
# print()
# # #%%
# # feature_plot(train_df, "label")

# # #%%
# # feature_corr = train_x.corr()   
# # heatmap_plot(feature_corr)
# # # %%
# # plot_importance(m.xgb)

# # %%
# model_train_save()
# %%