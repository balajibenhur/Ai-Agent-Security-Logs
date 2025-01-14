```python
# preprocess_logs.py
import json

def preprocess_guardduty(findings):
    processed = []
    for finding in findings:
        processed.append({
            'id': finding['Id'],
            'type': finding['Type'],
            'severity': finding['Severity'],
            'account': finding['AccountId'],
            'region': finding['Region'],
            'time': finding['UpdatedAt']
        })
    return processed

def preprocess_security_lake(logs):
    processed = []
    for log in logs:
        processed.extend(json.loads(log))  # Assuming logs are in JSON format
    return processed
```
