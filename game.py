from random import randint


def roll():

    while True:
        frames = 0

        roll_1 = randint(0, 10)
        if roll_1 == 10:
            print('Strike')
            if roll_1 == 0:
                print('Gutter')
            if roll_1 <= 9:
                print(roll_1)

        roll_2 = randint(0, 10)
        if roll_2 <= 9:
            print(roll_2)
            if roll_2 == 0:
                print('Gutter')
            if roll_2 == 10:
                print('Strike')
        total = roll_1 + roll_2
        if total == 100:
            return total


def main():

    pins = 10
    roll = randint(0, 10)
    pins -= roll

    games = {'Player': []}
    for i in range(10):
        key, count = roll
        games[key].append(count)
        print(i)
    all_games = games['Player'][:]
    print('max game', max(all_games))
    print('min game', min(all_games))
    print('average', sum(all_games) / len(all_games))
    print('Player won', round(100 * len(games['Player']) / len(all_games)),
          '%', 'of the time')


if __name__ == '__main__':
    main()
