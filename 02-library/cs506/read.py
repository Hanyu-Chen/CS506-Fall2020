# import pandas as pd
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    stopWords = ["\n", "\""]
    f = open(csv_file_path, "r")
    res = [line for line in f.readlines()]

    # Delete stopWords (like punctuations except ",")
    for sw in stopWords:
        res = [line.replace(sw, "") for line in res]

    # Split each element
    # If there is a integer, convert it from str to int
    for i in range(len(res)):
        tmp = res[i].split(",")
        for j in range(len(tmp)):
            try:
                tmp[j] = int(tmp[j])
            except:
                pass
        res[i] = tmp
    return res

# read_csv("../tests/test_files/dataset_2.csv")

