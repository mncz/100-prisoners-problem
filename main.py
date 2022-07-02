import random
import time

PRISONERS = 100
TRIALS = 10000
WAIT = 0.0001

def no_strategy():
    prison = random.sample(range(1, PRISONERS + 1), PRISONERS)
    arrange = random.sample(range(1, PRISONERS + 1), PRISONERS)
    found = False

    for prisoner in prison:
        choices = random.sample(range(0, PRISONERS), PRISONERS // 2)

        for choice in choices:
            if prisoner == arrange[choice]:
                found = True
                break

        if not found:
            return 0
        else:
            found = False
    return 1

def solution():
    prison = random.sample(range(1, PRISONERS + 1), PRISONERS)
    arrange = random.sample(range(1, PRISONERS + 1), PRISONERS)
    boxes = {}
    found = False

    for i in range(0, PRISONERS):
        boxes[i + 1] = arrange[i]

    for prisoner in prison:
        id = prisoner

        for _ in range(PRISONERS // 2):
            if id == boxes[prisoner]:
                found = True
                break
            else:
                prisoner = boxes[prisoner]

        if not found:
            return 0
        else:
            found = False
    return 1

def main():
    successes = 0

    for i in range(1, TRIALS + 1):
        # if no_strategy():
        if solution():
            successes += 1
        print("Successes: %s/%s (%.4f%%)" % (successes, i, float((successes/i)*100)), end="\r", flush=True)
        time.sleep(WAIT)
    print("Successes: %s/%s (%.4f%%)" % (successes, TRIALS, float((successes/TRIALS)*100)))

if __name__ == "__main__":
    main()