def test_password(pw, min, max, required):
    print(f'{pw} {min} {max} {required}')
    count = 0
    for x in pw:
        if x == required:
            count += 1

    return min <= count <= max

def test_password_2(pw, first, second, required):
    print(f'{pw} {first} {second} {required}')

    if len(pw) < first:
        return False
    elif len(pw) < second:
        return pw[first] == required
    elif pw[first] == required and pw[second] == required:
        return False
    elif pw[first] != required and pw[second] != required:
        return False

    return True

def compute():
    with open("passwords.txt") as fp:
        valid = 0
        for line in fp.readlines():
            data = line.strip().split(" ")
            min, max = data[0].split("-")
            
            #if test_password(data[2], int(min), int(max), data[1][0]):
            if test_password_2(data[2], int(min) - 1 , int(max) - 1, data[1][0]):
                valid += 1

    print(f"Valid count: {valid}")



if __name__ == '__main__':
    compute()