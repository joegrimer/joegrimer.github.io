"""
Task:
    - Make a very simple neural network
    - Print it
    - Make it play the same different coin flip game
    - genetic algorithm
    - competition
    - generation
    - cross breed
    - mutation
    - Play against it
"""
from pprint import pprint
import random

INPUTS = 2
OUTPUTS = 2
COLUMNS = 2  # middle layers
HEIGHT = INPUTS
nn = []

def starting_node_weight():
    return random.randint(1, 9)

def main():
    print("making nn")
    nid = 0
    for column_no in range(0, COLUMNS):
        nn.append({})
        for row in range(0, HEIGHT):
            nn[column_no][nid] = {
                "in_weights": {},
                "out_weight": starting_node_weight(),
            }
            if column_no != 0:
                nn[column_no][nid]["in_weights"] = {nid: starting_node_weight() for nid in nn[column_no - 1].keys()}
            nid += 1

    print("print nn")
    rotated_screen = []
    c_id = 0
    for column in nn:
        r_id = 0
        for nid, node in column.items():
            if r_id > len(rotated_screen)-1:
                rotated_screen.append([])
            if c_id > len(rotated_screen[r_id])-1:
                rotated_screen[r_id].append("null")
            # print("rotated_sceen", rotated_screen)
            # print("r_id", r_id)
            # print("c_id", c_id)
            rotated_screen[r_id][c_id] = f"{node['in_weights']}->[{nid}]->{node['out_weight']}"
            r_id += 1
        c_id += 1
    for row in rotated_screen:
        print("\t|\t".join(row))


if __name__ == '__main__':
    main()
