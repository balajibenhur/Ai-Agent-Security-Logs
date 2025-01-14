# Ai-Agent-Security-Logs
AI Agent for Processing Security Lake and GuardDuty Logs
## Description
This project provides an AI agent that fetches, preprocesses, and analyzes logs from AWS Security Lake and GuardDuty. It uses machine learning to detect anomalies and generates dashboards for security insights.

## Features
- Fetch logs from Security Lake (S3) and GuardDuty.
- Preprocess and normalize logs for analysis.
- Use Isolation Forest to detect anomalies.
- Generate dashboards for GuardDuty findings.

## Prerequisites
- AWS account with access to Security Lake and GuardDuty.
- Python 3.8 or above.
- IAM role with permissions for `s3` and `guardduty` actions.

## Usage
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the AI agent:
    ```bash
    python main.py
    ```

## Future Work
- Add support for additional AWS services (e.g., AWS Macie).
- Implement real-time anomaly detection pipelines.
```
