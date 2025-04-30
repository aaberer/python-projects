import random  # optional and you can delete this line if not useful

# subroutines if any, go here


# fill in placement
def placement(num_players, field):
    if not isinstance(num_players, int) or num_players <= 0:
        return (), ()
    if not field:
        return (), ()

    length = len(field)
    width = len(field[0])

    if length % 2 != 0:
        return (), ()
    if length < 2 or width < 2:
        return (), ()

    green_count = 0
    gold_count = 0
    green_spots = []
    gold_spots = []

    for i in range(length):
        for j in range(width):
            if field[i][j]:
                if i < length // 2:
                    green_count += field[i][j]
                    green_spots.append((i, j))
                else:
                    gold_count += field[i][j]
                    gold_spots.append((i, j))

    if len(green_spots) < num_players or len(gold_spots) < num_players:
        return (), ()

    green_count = len(green_spots)
    gold_count = len(gold_spots)
    minimum_count = min(num_players, green_count, gold_count)

    if minimum_count == 0:
        return (), ()

    greenReturn = random.sample(green_spots, num_players)
    goldReturn = random.sample(gold_spots, num_players)

    return tuple(greenReturn), tuple(goldReturn)
