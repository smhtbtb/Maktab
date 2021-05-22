class BackUpOpen:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.back_up = open('back_up_file.txt', 'w')

        # with open(self.file_name, 'r') as original:
        #     helper = original.read()
        #     self.back_up.write(helper)
        original = open(self.file_name, 'r')
        helper = original.read()
        original.close()
        self.back_up.write(helper)

        self.x = open(self.file_name, self.mode)

        return self.x

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.x.close()
        # self.back_up.close()

        if exc_tb or exc_type or exc_val:
            self.back_up.close()
            self.x.close()
            self.x = open(self.file_name, 'w')
            self.x.write('')
            self.back_up = open('back_up_file.txt', 'r')
            helper = self.back_up.read()
            self.x.write(helper)

        self.x.close()
        self.back_up.close()

        return True


with BackUpOpen('test.txt', 'w') as f:
    f.write('hi hi')
    f.sdc('sd')

with open('test.txt') as f:
    print(f.read())
