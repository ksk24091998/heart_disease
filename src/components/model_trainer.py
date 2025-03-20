import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from data_transformation import *

class modelling:
    def model_build_evals(self):
        train, test,path = transformation().trans()
        
        # Prepare the data
        X_train, y_train = train.drop("target", axis=1), train['target']
        X_test, y_test = test.drop("target", axis=1), test['target']
        
        # Standardize the features (important for models like Logistic Regression)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Initialize classifiers
        models = {
            'Logistic Regression': LogisticRegression(max_iter=1000),
            'Random Forest': RandomForestClassifier(),
            'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
        }
        
        # Initialize variables to track the best model and its performance
        best_model = None
        best_accuracy = 0
        
        # Evaluate each model
        for model_name, model in models.items():
            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test_scaled)
            accuracy = accuracy_score(y_test, y_pred)
            print(f"{model_name} Accuracy: {accuracy}")
            
            # Track the best model
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_model = model
        
        # Save the best model to a .pkl file
        if best_model:
            joblib.dump(best_model, os.path.join(path, 'best_model.pkl'))
            print("Best model saved as 'best_model.pkl'")

        
    

if __name__ == "__main__":
    modelling().model_build_evals()
    
