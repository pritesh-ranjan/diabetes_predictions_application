import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
def train():
    dataset = pd.read_csv('pima.csv')
    X = dataset[['F','D','E','B','C']]
    Y = dataset[['I']]
    
    #train test split
    from sklearn.cross_validation import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 101)
    
    from sklearn.svm import SVC
    model = SVC(kernel='linear')
    svc=model.fit(X_train,Y_train)
    
    #Save Model As Pickle File
    with open('svc.pkl','wb') as m:
        pickle.dump(svc,m)
    test(X_test,Y_test)


def test(X_test,Y_test):
    with open('svc.pkl','rb') as mod:
        p=pickle.load(mod)
    
    pre=p.predict(X_test)
    from sklearn.metrics import accuracy_score
    print (accuracy_score(Y_test,pre))
    d={'B':197,'C':94,'D':18,'E':0,'F':22.7,}   
#   bv=pd.DataFrame(data=d,index=[0])
    check_input(d)
def check_input(data):
    df=pd.DataFrame(data=data,index=[0])
    with open('svc.pkl','rb') as model:
        p=pickle.load(model)
    op=p.predict(df)
    #print(op[0])
    return op[0]
if __name__=="__main__":
    train()

    