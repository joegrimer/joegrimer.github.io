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
import random

DATA_A = [
    ((0,0), (0,)),
    ((0,1), (0,)),
    ((1,0), (1,)),
    ((1,1), (1,)),
]
DATA = [
    ((0, 0, 0), (0,)),
    ((0, 0, 1), (1,)),
    ((0, 1, 0), (0,)),
    ((0, 1, 1), (1,)),
    ((1, 0, 0), (0,)),
    ((1, 0, 1), (1,)),
    ((1, 1, 0), (0,)),
    ((1, 1, 1), (1,)),
]
ITERATIONS = 9999999
# DATA = DATA_OLD
INPUTS = len(DATA[0][0])
OUTPUTS = len(DATA[0][1])
HEIGHT = INPUTS # not neccessarily correct
COLUMNS = 2  # layers
nn = []
NODE_RESOLUTION = 100
HALF_RESOLUTION = NODE_RESOLUTION / 2 # n.b. intentionally not flooring

MANUAL_NN = [
    {0: {'in_weights': {}, 'value': None},
     1: {'in_weights': {}, 'value': None},
     2: {'in_weights': {}, 'value': None}},
    {3: {'in_weights': {0: 0, 1: 0, 2: NODE_RESOLUTION}, 'value': None}}]


def main():
    print("start")
    run_iterations()
    # run_manual()
    print("end")


def run_iterations():
    global nn
    most_hits = 0
    for i in range(0, ITERATIONS):
        generate_nn()
        hits = 0
        # inputs = [starting_node_weight() for _ in range(0, INPUTS)]
        example = ""
        for datum in DATA:
            example += f"datum: {datum}\n"
            inputs = [i*NODE_RESOLUTION for i in datum[0]]
            wanted_output = datum[1][0]
            nn_output = int(run_nn(inputs)[0] >= 500)
            # example += "Print nn\n"
            # print_nn(nn)
            example += f"wanted {wanted_output} and outputs {nn_output}\n"
            if wanted_output == nn_output:
                hits += 1
        if hits > most_hits:
            most_hits = hits
            print("---------")
            print("Best went up: ", most_hits)
            print(example)
            print_nn(nn)
        if hits == len(DATA):
            print("--------------------------------")
            print("IT WORKED", i, "for len", len(DATA))
            print("print nn")
            print_nn(nn)

            break
    print("end i is", i)
    print("best was", most_hits)


def run_manual():
    print("MANUAL")

    global nn
    nn = MANUAL_NN
    hits = 0
    print_nn(nn)
    for datum in DATA:
        print(f"datum: {datum}")
        inputs = [i*(NODE_RESOLUTION) for i in datum[0]]
        wanted_output = datum[1][0]
        nn_output = int(run_nn(inputs)[0] >= HALF_RESOLUTION)
        print_nn(nn)
        print(f"wanted {wanted_output} and outputs {nn_output}")
        if wanted_output == nn_output:
            hits += 1

    print("Hits: {}".format(hits))


def starting_node_weight():
    return random.randint(1, NODE_RESOLUTION)


def randof(ceiling):
    return random.randint(0, ceiling)


def mash_numbers(a, b):
    return (a + b) // 2  # i.e. average, and throw remainder


def funnel(charge, pipe):
    return int(pipe * (charge/NODE_RESOLUTION))


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
            middle = f"V:{node['value']:03}" if node["value"] is not None else f"{nid:03}"
            rotated_screen[r_id][c_id] = f"{node['in_weights']}->[{middle}]"
            r_id += 1
        c_id += 1
    for row in rotated_screen:
        print("  ".join(row))


def generate_nn():
    global nn
    nn = []
    nid = 0
    for column_no in range(0, COLUMNS):
        nn.append({})
        height_of_layer = HEIGHT if column_no+1 < COLUMNS else OUTPUTS
        for _ in range(0, height_of_layer):
            nn[column_no][nid] = {
                "in_weights": {},
                "value": None,
            }
            if column_no != 0:
                in_weights = {}
                in_weights_total = 0
                for mnid in nn[column_no - 1].keys():
                    if mnid == (HEIGHT -1):
                        new_weight = NODE_RESOLUTION - in_weights_total
                    else:
                        new_weight = randof(NODE_RESOLUTION - in_weights_total)
                    in_weights_total += new_weight
                    in_weights[mnid] = new_weight
                nn[column_no][nid]["in_weights"] = in_weights
            nid += 1


def run_nn(inputs):
    input_index = 0  # happens to correlatete with nid
    for input in inputs:
        nn[0][input_index]["value"] = input
        input_index += 1

    last_column = 0
    last_outputs = []
    for column in nn[1:]:
        last_outputs = []
        for _, node in column.items():
            new_val = 0
            for back_nid, link_weight in node["in_weights"].items():
                new_val += funnel(nn[last_column][back_nid]["value"], link_weight)
            node["value"] = new_val
            last_outputs.append(node["value"])
        last_column += 1
    return last_outputs


if __name__ == '__main__':
    main()
