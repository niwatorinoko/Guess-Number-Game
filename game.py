import sys
import random


sys.stdout.buffer.write(b'Please enter minimum number: ')
sys.stdout.flush()
n = sys.stdin.buffer.readline()

sys.stdout.buffer.write(b'Please enter maximum number: ')
sys.stdout.flush()
m = sys.stdin.buffer.readline()

answer = random.randint(int(n), int(m))

while True:
    sys.stdout.buffer.write(b'Guess a number between ' + n.strip() + b' and ' + m.strip() + b': ')
    sys.stdout.flush()
    guess = sys.stdin.buffer.readline()
    if int(guess) < answer:
        sys.stdout.buffer.write(b'Too low!')
        sys.stdout.flush()
    elif int(guess) > answer:
        sys.stdout.buffer.write(b'Too high!')
        sys.stdout.flush()
    else:
        sys.stdout.buffer.write(b'You got it!')
        sys.stdout.flush()
        break

sys.stdout.buffer.write(b'The correct answer is ' + str(answer).encode() + b'. Thanks for playing!\n')
