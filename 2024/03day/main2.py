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
    cond = 1
    while i<len(inp):
        print(i)
        condst = inp.find("do()",i)
        condst = condst if condst != -1 else float("inf")
        condsf = inp.find("don't()",i)
        condsf = condsf if condsf != -1 else float("inf")

        start = inp.find("mul(",i)
        start = start if start != -1 else float("inf")

        mini = min(condst, condsf, start)
        if condst == mini:
            print("cond1")
            cond = 1
            i = condst+1
            continue
        elif condsf == mini:
            print("cond2")
            cond = 0
            i = condsf+1
            continue
        elif start == mini:
            print("cond3")
            i = start+1
            pass
        else:
            if start == float("inf"):
                i += 1
                continue
            else:
                ValueError("unexpected condition")
       
        x = re.search("^\d{1,3},\d{1,3}\)",inp[start+4:start+4+8])
        if x is None:
            continue
        end = inp.find(")",start)
        muls = inp[start+4:end].split(",")
        summ += int(muls[0]) * int(muls[1]) * cond
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
