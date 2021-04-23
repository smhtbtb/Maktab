from abc import ABC, abstractmethod


class Morse(ABC):
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', '\n': '|', ' ': '/'
                       # ', ': '--..--', '.': '.-.-.-',
                       # '?': '..--..', '/': '-..-.', '-': '-....-',
                       # '(': '-.--.', ')': '-.--.-'
                       }

    def __init__(self, data: str):
        self._data = data
        assert self._check()

    @abstractmethod
    def process(self) -> str:
        pass

    @abstractmethod
    def _check(self) -> bool:
        pass

    def save_file(self, file_name):
        with open(file_name, 'w') as f:
            f.write(self.process())
        return file_name

    @classmethod
    def from_file(cls, file_path):
        with open(file_path) as f:
            data = f.read()
            return cls(data)


class MorseEncoder(Morse):
    def process(self) -> str:
        res = ''
        for c in self._data.replace('  ', ' '):
            res += self.MORSE_CODE_DICT[c.upper()] + ' '

        return res

    def play(self, speed=1.0, freq=1800):
        import winsound
        from time import sleep
        p_data = self.process()
        frequency = freq
        speed = 1 / speed
        for c in p_data:
            if c == '.':
                winsound.Beep(frequency, int(200 * speed))
            elif c == '-':
                winsound.Beep(frequency, int(400 * speed))
            else:
                sleep(0.5 * speed)

    def _check(self) -> bool:
        return all(
            map(
                lambda s: s.isalnum() and s.isascii(),
                self._data.split()
            )
        )


class MorseDecoder(Morse):

    def process(self) -> str:
        MORSE_CODE_DICT2 = {}
        for k in self.MORSE_CODE_DICT:
            MORSE_CODE_DICT2[self.MORSE_CODE_DICT[k]] = k

        res = ''
        for c in self._data.split():
            res += MORSE_CODE_DICT2[c]

        return res.title()

    def _check(self) -> bool:
        for i in self._data.split():
            if i in self.MORSE_CODE_DICT.values():
                # print(i)
                return True


m = MorseEncoder('Salam Chetori Akbar')
print(m.process())

n = MorseDecoder('... .- .-.. .- -- / -.-. .... . - --- .-. .. / .- -.- -... .- .-. ')
n = n.process()
print(n)
