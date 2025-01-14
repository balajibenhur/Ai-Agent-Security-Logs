```python
# anomaly_detection.py
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    model = IsolationForest(contamination=0.05, random_state=42)
    features = [
        [entry['severity'], entry['time']] for entry in data
    ]
    
    model.fit(features)
    predictions = model.predict(features)
    return [
        data[idx] for idx, pred in enumerate(predictions) if pred == -1
    ]
```
