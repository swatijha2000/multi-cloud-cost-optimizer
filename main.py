from monitoring.monitor import check_aws, check_azure
from decision.decision_engine import decide_cloud
from automation.actions import switch_to_aws, switch_to_azure
from datetime import datetime
import time
import os

print(" Multi-Cloud Failover System Started...\n")

while True:
    aws_status = check_aws()
    azure_status = check_azure()

    print(f"AWS Status: {aws_status}, Azure Status: {azure_status}")

    decision = decide_cloud(aws_status, azure_status)

    # Decision handling
    if decision == "USE_AWS":
        switch_to_aws()
    elif decision == "USE_AZURE":
        switch_to_azure()
    else:
        print(" No server available")

    log_file = os.path.join(os.path.dirname(__file__), "logs.txt")

    #  Logging
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} | AWS: {aws_status}, Azure: {azure_status}, Decision: {decision}\n")

    print("-" * 40)

    time.sleep(10)