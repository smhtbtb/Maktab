class Indenter:

    # @staticmethod
    def print(self, n: str = None):

        print(n)

    def __enter__(self):
        # self.print(n)
        print(f'\t', end='')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('    ')
        return True


# Indenter.print('hi')
with Indenter() as indent:
    indent.print('talk is cheap')
    with indent:
        indent.print('show me the code')


#
#
#
#
#
#
#
# from contextlib import contextmanager
#
#
# @contextmanager
# class Indenter:
#
#     @staticmethod
#     def print(n: str = None):
#         return print(n)
#
#     def indent(self):
#         try:
#             yield '    '
#
#         finally:
#             yield '    '
#
#
# Indenter.print('hi')
