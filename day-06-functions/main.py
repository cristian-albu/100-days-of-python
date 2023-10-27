def jump():
    print('You jumped 1 time')


def jump_with_args(times):
    if times == 1:
        jump()
    else:
        print(f"You jumped {times} times")


jump()

n = 2
while n < 5:
    jump_with_args(n)
    n += 1

jump_with_args(5)