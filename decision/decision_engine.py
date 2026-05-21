def decide_cloud(aws_status, azure_status):
    if aws_status:
        return "USE_AWS"
    elif azure_status:
        return "USE_AZURE"
    else:
        return "NO_SERVER_AVAILABLE"