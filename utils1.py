import re
from sklearn.preprocessing import LabelEncoder
class PrepProcesor(LabelEncoder): 
    def fit(self, X, y=None): 
        self.lableen = LabelEncoder()
        self.lableen.fit(X[['Address']])
        return
    def transform(self, X, y=None):
        X['Address'] = self.lableen.transform(X[['Address']])
        return X

columns = ['Area','Room','Parking','Warehouse','Elevator','Address']