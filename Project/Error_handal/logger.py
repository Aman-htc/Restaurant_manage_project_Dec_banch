

def write_logs(error):
    with open('error.txt','a') as file:
        file.write(error)