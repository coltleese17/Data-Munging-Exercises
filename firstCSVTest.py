import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

DATAFILE = os.path.join(__location__, 'beatles-discography.csv')


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if (counter==10) :
            	break

            field = line.split(",")
            entry = {}

            for i, value in enumerate(field):
            	entry[header[i].strip()] = value.strip()

            data.append(entry) 
            print entry
            counter += 1

    return data

parse_file(DATAFILE)