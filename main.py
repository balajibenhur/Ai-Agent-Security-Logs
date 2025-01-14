# main.py
from data_ingestion.fetch_logs import fetch_guardduty_findings, fetch_security_lake_logs
from preprocessing.preprocess_logs import preprocess_guardduty, preprocess_security_lake
from models.anomaly_detection import detect_anomalies
from dashboards.generate_dashboard import plot_findings_summary

def main():
    print("Fetching logs...")
    guardduty_data = fetch_guardduty_findings()
    security_lake_data = fetch_security_lake_logs()

    print("Preprocessing logs...")
    processed_guardduty = preprocess_guardduty(guardduty_data)
    processed_security_lake = preprocess_security_lake(security_lake_data)

    print("Detecting anomalies...")
    anomalies = detect_anomalies(processed_guardduty)
    print(f"Anomalies detected: {len(anomalies)}")

    print("Generating dashboard...")
    plot_findings_summary(processed_guardduty)

if __name__ == "__main__":
    main()
```
