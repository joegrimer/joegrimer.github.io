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
import math

INPUTS = 3
OUTPUTS = INPUTS
COLUMNS = 3  # layers
HEIGHT = INPUTS # not neccessarily correct
nn = []
NODE_RESOLUTION = 1000
HALF_RESOLUTION = NODE_RESOLUTION / 2 # n.b. intentionally not flooring

def starting_node_weight():
    return random.randint(1, NODE_RESOLUTION)

def mash_numbers(a, b):
    # dodgy float multiplication
    new_res = math.floor((a/HALF_RESOLUTION)*(b/HALF_RESOLUTION) * NODE_RESOLUTION)
    if new_res > NODE_RESOLUTION-1:
        return NODE_RESOLUTION-1
    elif new_res < 1:
        return 1
    return new_res


def print_nn(nn: dict):

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
            middle = ("V:" + str(node["value"])) if node["value"] else nid
            rotated_screen[r_id][c_id] = f"{node['in_weights']}->{node['body_weight']}->[{middle}]"
            r_id += 1
        c_id += 1
    for row in rotated_screen:
        print("\t|\t".join(row))

def main():
    print("making nn")
    nid = 0
    for column_no in range(0, COLUMNS):
        nn.append({})
        for row in range(0, HEIGHT):
            nn[column_no][nid] = {
                "in_weights": {},
                "body_weight": starting_node_weight(),
                "value": None,
            }
            if column_no != 0:
                nn[column_no][nid]["in_weights"] = {nid: starting_node_weight() for nid in nn[column_no - 1].keys()}
            nid += 1

    print("print nn")
    print_nn(nn)

    print("run nn")
    inputs = [starting_node_weight() for _ in range(0, INPUTS)]
    print("inputs", inputs)
    input_index = 0  # happens to correlatete with nid
    for input in inputs:
        nn[0][input_index]["value"] = mash_numbers(input, nn[0][input_index]["body_weight"])
        input_index += 1

    last_column = 0
    last_outputs = []
    for column in nn[1:]:
        last_outputs = []
        for _, node in column.items():
            node["value"] = node["body_weight"]
            for back_nid, link_weight in node["in_weights"].items():
                node["value"] = mash_numbers(node["value"], link_weight)
                node["value"] = mash_numbers(node["value"], nn[last_column][back_nid]["value"])
            last_outputs.append(node["value"])
        last_column += 1
    print("outputs", last_outputs)

    print("Print nn")
    print_nn(nn)

    print("end")


if __name__ == '__main__':
    main()
