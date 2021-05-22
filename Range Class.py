# class Range:
#
#     def __init__(self, start: int = 0, end: int = None, step: int = 1):
#         self.start = start
#         self.step = step
#         self.end = end
#         if self.end == None:
#             self.end = self.start
#             self.start = 0
#
#     def __iter__(self):
#         self.start -= self.step
#         return self
#
#     def __next__(self):
#         self.start += self.step
#         if self.start < self.end:
#             return self.start
#         raise StopIteration('start is less than end')
#
#
# for i in Range(5):
#     print(i)


def Rrange(start: int = 0, end: int = None, step: int = 1):
    if end is None:
        end = start
        start = 0

    # if step < 0:
    #     start, end = end, start
    #     step = -step

    while start < end:
        yield start
        start += step


for i in Rrange(5, 0, -1):
    print(i)
