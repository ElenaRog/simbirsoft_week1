import random


def rand_num() -> str:
    return str(random.randint(0, 9999999999)).zfill(10)


def rand_name(num: str) -> str:
    rname = ''
    for i in range(0, 10, 2):
        rname += chr((int(num[i:i + 2]) % 26) + 97)
    return rname


class RandomData:
    post_code: str
    first_name: str

    def __init__(self):
        self.post_code = rand_num()
        self.first_name = rand_name(self.post_code).title()



