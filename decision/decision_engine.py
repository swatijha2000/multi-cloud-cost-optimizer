def decide_cloud(aws_status, azure_status):
    aws_cost = 5      # assumed cost
    azure_cost = 3    # assumed cheaper

    if aws_status and azure_status:
        if azure_cost < aws_cost:
            return "USE_AZURE"
        else:
            return "USE_AWS"
    elif aws_status:
        return "USE_AWS"
    elif azure_status:
        return "USE_AZURE"
    else:
        return "NO_SERVER"