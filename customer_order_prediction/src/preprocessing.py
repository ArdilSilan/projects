from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def preprocess_data(df, test_size = 0.2,class_imbalance = 0):
    X = df[['total_orders', 'total_spent', 'avg_order_value']]
    y = df['will_order_again']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled,y, test_size=test_size, random_state=42)

    if class_imbalance == 0:
        return X_train, y_train, X_test, y_test
       
    
    if class_imbalance == 1:
        sm = SMOTE(random_state=42)
        X_resampled, y_resampled = sm.fit_resample(X_train, y_train)
        return X_resampled, y_resampled, X_test, y_test
    
    if class_imbalance == 2:
        return 

