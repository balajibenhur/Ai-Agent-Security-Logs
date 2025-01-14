#!/usr/bin/python
# generate_dashboard.py
import matplotlib.pyplot as plt

def plot_findings_summary(findings):
    severities = [finding['severity'] for finding in findings]
    plt.hist(severities, bins=10, color='blue', alpha=0.7)
    plt.title('GuardDuty Findings Severity Distribution')
    plt.xlabel('Severity')
    plt.ylabel('Frequency')
    plt.show()

