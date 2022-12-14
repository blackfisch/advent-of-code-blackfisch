"""
AoC 2022 Day 3: Rucksack Reorganization
https://adventofcode.com/2022/day/3
"""

from aocd import data as input_data


class ItemPriotity:  # pylint: disable=too-few-public-methods
    """Item Priorities"""
    items = dict(
        zip(
            list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            range(1, 53)
        )
    )

    @staticmethod
    def get_priority(char: str):
        """Return the priority for a character"""
        return ItemPriotity.items.get(char)


### Solutions ###

def part_a(data: str):
    """Solution for part A"""

    def prepare_data(data: str) -> list:
        """Prepare the data"""
        return [
            (line[:len(line)//2], line[len(line)//2:])
            for line in data.splitlines()
        ]

    all_rucksacks = prepare_data(data)

    shared_items = []
    for comp_1, comp_2 in all_rucksacks:
        for item in comp_1:
            if item in comp_2:
                shared_items.append(ItemPriotity.get_priority(item))
                break

    return sum(shared_items)


def part_b(data: str):
    """Solution for part B"""

    def prepare_data(data: str) -> list:
        """Pepare the data"""

        rucksacks = data.splitlines()
        groups = []
        for counter in range(0, len(rucksacks)//3):
            groups.append(data.splitlines()[counter * 3:(counter + 1) * 3])

        return groups

    groups = prepare_data(data)

    shared_items = []
    for bp_1, bp_2, bp_3 in groups:
        for item in bp_1:
            if item in bp_2 and item in bp_3:
                shared_items.append(ItemPriotity.get_priority(item))
                break

    return sum(shared_items)


if __name__ == '__main__':
    print(f'Part A: {part_a(input_data)}')
    print(f'Part B: {part_b(input_data)}')
