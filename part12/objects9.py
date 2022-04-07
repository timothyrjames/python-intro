class Counter(object):
    count = 0

    def __init__(self):
        Counter.count += 1
    
    def get_count():
        return Counter.count


a = Counter()
b = Counter()
c = Counter()
d = Counter()

print(Counter.get_count())

# You can't do this - get_count() is a class method.
# a.get_count()

