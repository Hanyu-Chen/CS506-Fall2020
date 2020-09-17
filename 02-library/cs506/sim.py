def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i]-y[i]) ** 2
    return res ** 0.5

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += x[i]<y[i] and y[i]-x[i] or x[i]-y[i]
    return res

def jaccard_dist(x, y):
    # Check if the lengths of input are the same or equal 0
    if len(x) != len(y) or len(x) == 0:
        # -1 means the input is not right
        return -1;
    disjunction = 0;
    conjunction = 0;
    for i in range(len(x)):
        if x[i] == y[i]:
            conjunction += 1;
        disjunction += 1;
    return 1 - conjunction/disjunction;

def cosine_sim(x, y):
    # Check if the lengths of input are the same or equal 0
    if len(x) != len(y) or len(x) == 0:
        # -1 means the input is not right
        return -1;
    divisor = 0;
    dividend1 = 0;
    dividend2 = 0;
    for i in range(len(x)):
        divisor += x[i] * y[i];
        dividend1 += x[i] ** 2;
        dividend2 += y[i] ** 2;
    return divisor/(dividend1 ** 0.5 * dividend2 ** 0.5)

# Feel free to add more
