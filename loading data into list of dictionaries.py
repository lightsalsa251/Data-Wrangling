DATAFILE = "beatles-discography.csv"
def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        header = f.readline().split(',')
        counter = 0
        for line in f:
            if counter==10:
                break
            #because here we are taking the first 10 lines only
            fields = line.split(',')
            entry = {}
            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()
            #this loop runs for every field, putting the values in its respective indexes stored in the header
            data.append(entry)
            counter+=1
            #enumerate returns the index and the value
    return data


data = parse_file(DATAFILE)
print(data)
