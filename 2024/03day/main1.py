import re

def process(path):
    inp = []

    with open(path) as f:
        for line in f.readlines():
            inp.append(line.strip())
        
    return "".join(inp)

def main(inp):
    i=0
    summ = 0
    while i<len(inp):
        start = inp.find("mul(",i)
        x = re.search("^\d{1,3},\d{1,3}\)",inp[start+4:start+4+8])
        if x is None:
            i = start+1
            continue
        end = inp.find(")",start)
        muls = inp[start+4:end].split(",")
        summ += int(muls[0]) * int(muls[1])
        i = end+1
    return summ



if __name__=="__main__":
    # #test1
    # print("test1")
    # inp = process("/Users/eddievilla/Repos/advent-of-code/2024/02day/test.txt")
    # val = main(inp)
    # print(f"return: {val}")

    #submission
    print("submission")
    inp = process("/Users/eddievilla/Repos/advent-of-code/2024/03day/input.txt")
    val = main(inp)
    print(f"return: {val}")
