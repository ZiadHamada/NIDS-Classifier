from data_preprocessor import *
from src.config import Config
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
import pickle
scaler = StandardScaler()
scaler.fit(X_train)


dtc = DecisionTreeClassifier(max_depth=Config.MAX_DEPTH, criterion=Config.CRITERION, max_features=Config.MAX_FEATURES,
                             min_samples_leaf=Config.MIN_SAMPLES_LEAF, random_state=Config.RANDOM_STATE)
dtc.fit(scaler.transform(X_train), y_train)

t_pred = dtc.predict(scaler.transform(X_test))

print(confusion_matrix(y_test, t_pred))
print(classification_report(y_test, t_pred))


with open(os.path.join(Config.MODEL_SAVE_PATH, Config.MODEL), 'wb') as f:
    pickle.dump(dtc, f)  


with open(os.path.join(Config.MODEL_SAVE_PATH, Config.COLUMNS), 'wb') as f:
    pickle.dump(X_train.columns, f) 
    
with open(os.path.join(Config.MODEL_SAVE_PATH, Config.SCALER),'wb') as f:
    pickle.dump(scaler, f)
    