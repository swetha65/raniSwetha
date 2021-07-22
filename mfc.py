import collections
def mfc(s):
    c = collections.Counter(s)
    return c.most_common(1)

print(mfc("hello world"))