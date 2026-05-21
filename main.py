from monitoring.monitor import check_aws, check_azure
from decision.decision_engine import decide_cloud
from automation.actions import switch_to_aws, switch_to_azure
import time

while True:
    aws = check_aws()
    azure = check_azure()

    print(f"AWS: {aws}, Azure: {azure}")

    decision = decide_cloud(aws, azure)

    if decision == "USE_AWS":
        switch_to_aws()
    elif decision == "USE_AZURE":
        switch_to_azure()
    else:
        print("No server available")

    time.sleep(10)