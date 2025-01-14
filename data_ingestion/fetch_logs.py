```python
# fetch_logs.py
import boto3

def fetch_guardduty_findings():
    client = boto3.client('guardduty')
    detectors = client.list_detectors()['DetectorIds']
    findings = []

    for detector_id in detectors:
        response = client.list_findings(DetectorId=detector_id, MaxResults=50)
        if response['FindingIds']:
            findings.extend(client.get_findings(
                DetectorId=detector_id,
                FindingIds=response['FindingIds']
            )['Findings'])

    return findings

def fetch_security_lake_logs():
    client = boto3.client('s3')
    bucket_name = '<security-lake-bucket>'  # Replace with your Security Lake S3 bucket
    logs = []

    for obj in client.list_objects_v2(Bucket=bucket_name)['Contents']:
        response = client.get_object(Bucket=bucket_name, Key=obj['Key'])
        logs.append(response['Body'].read().decode('utf-8'))

    return logs

if __name__ == "__main__":
    guardduty_data = fetch_guardduty_findings()
    security_lake_data = fetch_security_lake_logs()
    print(f"GuardDuty Findings: {len(guardduty_data)}")
    print(f"Security Lake Logs: {len(security_lake_data)}")
```
