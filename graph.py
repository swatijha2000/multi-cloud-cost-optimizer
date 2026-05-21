import matplotlib.pyplot as plt

aws_count = 0
azure_count = 0

with open("logs.txt", "r") as f:
    for line in f:
        if "USE_AWS" in line:
            aws_count += 1
        elif "USE_AZURE" in line:
            azure_count += 1

labels = ['AWS', 'Azure']
values = [aws_count, azure_count]

plt.bar(labels, values, color=['blue', 'green'])
plt.title("Cloud Usage Comparison")
plt.xlabel("Cloud Provider")
plt.ylabel("Number of Times Selected")

plt.show()