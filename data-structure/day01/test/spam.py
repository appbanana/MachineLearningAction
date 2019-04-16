print('from the spam.py')

money = 1000


def read1():
    print('spam->read1->money', money)


def read2():
    print('spam->read2 calling read')
    read1()


def change():
    global money
    money = 0
