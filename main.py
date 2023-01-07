import fileinput


class Blocker:
    def __init__(self, n, p, b, b_max, time):
        self.N = n
        self.P = p
        self.B = b
        self.B_max = b_max
        self.T = time
        self.tries = []
        # для хранения n элементов, исрользуется O(n) памяти

    def append(self, trie):
        # сложность (по времени) вставки O(n)
        if self.T - 2 * self.B_max <= trie <= self.T:
            self.tries.append(trie)

    def analyze(self):
        # сложность (по времени) сортировки O(n*log(n))
        # для сортировки встроенными средствами Python необъодимо O(n) памяти
        self.tries.sort()
        block_end = 0
        i_ = self.N
        # сложностьпо (по времени) обхода n элементного списка O(n)
        while i_ <= len(self.tries):
            if self.tries[i_ - 1] - self.tries[i_ - self.N] < self.P:
                block_end = self.tries[i_ - 1] + self.B
                i_ += self.N - 1
                self.B = min(self.B * 2, b_max)
            i_ += 1
        if block_end < self.T:
            return None
        return block_end

# по итогу сложность по времени всего алгоритма O(n*log(n))
# по итогу сложность по памяти всего алгоритма O(n)

if __name__ == '__main__':
    n, p, b, b_max, cur_unix = map(int, input().split())
    bl = Blocker(n, p, b, b_max, cur_unix)
    for line in fileinput.input():
        bl.append(int(line))
    end_time = bl.analyze()
    if end_time is None:
        print("ok")
    else:
        print(end_time)
