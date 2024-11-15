with open("data/data_validation/status.txt",'r') as f:
    content=f.read().split(" ")[-1]

print(content)