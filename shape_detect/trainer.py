from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import argparse
from controller import labeling

class trainer:

    def __init__(self):
        self.df = pd.read_csv("./train.csv")
        self.x_data = self.df.loc[:, "D1":"A3"]
        self.y_data = self.df.loc[:, "shape"]
    
    def train_knn(self):
        knn = KNeighborsClassifier(n_neighbors=4, weights="distance", metric="euclidean")
        knn.fit(self.x_data, self.y_data)

        joblib.dump(knn, './shape_detect/models/knn_model.pkl') 

    def train_dt(self):
        dt = DecisionTreeClassifier()
        dt.fit(self.x_data, self.y_data)

        joblib.dump(dt, './shape_detect/models/dt_model.pkl') 
    
    def train_svm(self):
        clf = svm.SVC(kernel='linear', probability=True)
        clf.fit(self.x_data, self.y_data)

        joblib.dump(clf, './shape_detect/models/svm_model.pkl')

    def train_all(self):
        self.train_knn()
        self.train_dt()
        self.train_svm()
        print("train complete")

def main(args):
    if args.label:
        labeling(args.dataset)
    cls = trainer()
    cls.train_all()
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train Command')

    # dataset, train option
    parser.add_argument('--dataset', type=str, default="./shape_detect/dataset/train")
    parser.add_argument('--label', type=int, default=1)
    parser.add_argument('--output', type=str, default="train.csv")
    args = parser.parse_args()
    main(args)
    