def process(path):
    inp = []

    with open(path) as f:
        for line in f.readlines():
            inp.append([int(n) for n in line.strip().split(" ")])
    return inp

def main(inp):
    safe = 0
    for report in inp:
        diff = report[0] - report[1]
        if not (1 <= abs(diff) <= 3):
            continue
        signedo = int(diff / abs(diff))
        issafe = True
        for li in range(1,len(report)-1):
            diff = report[li] - report[li+1]
            if not (1 <= abs(diff) <= 3):
                issafe = False
                break
            if (diff / abs(diff)) != signedo:
                issafe = False
                break
        if issafe:
            safe += 1
    return safe


if __name__=="__main__":
    # #test1
    # print("test1")
    # inp = process("/Users/eddievilla/Repos/advent-of-code/2024/02day/test.txt")
    # safe = main(inp)
    # print(f"safe: {safe}")

    #submission
    print("submission")
    inp = process("/Users/eddievilla/Repos/advent-of-code/2024/02day/input.txt")
    safe = main(inp)
    print(f"safe: {safe}")
