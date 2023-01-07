import fileinput


class Blocker:
    def __init__(self, n, p, b, b_max, time):
        self.N = n
        self.P = p
        self.B = b
        self.B_max = b_max
        self.T = time
        self.tries = []

    def append(self, trie):
        if self.T - self.B_max <= trie <= self.T:
            self.tries.append(trie)

    def analyze(self):
        self.tries.sort()
        block_end = 0
        i_ = self.N
        while i_ <= len(self.tries):
            if self.tries[i_ - 1] - self.tries[i_ - self.N] < self.P:
                block_end = self.tries[i_ - 1] + self.B
                i_ += self.N - 1
                self.B = min(self.B * 2, b_max)
            i_ += 1
        if block_end < self.T:
            return None
        return block_end


if __name__ == '__main__':
    n, p, b, b_max, cur_unix = map(int, input().split())
    bl = Blocker(n, p, b, b_max, cur_unix)
    line = input()
    while line:
        bl.append(int(line))
        line = input()
    # for line in fileinput.input():
    time = bl.analyze()
    if time is None:
        print("ok")
    else:
        print(time)
