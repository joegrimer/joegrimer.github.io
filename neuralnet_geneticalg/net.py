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
DATA_B = [
    ((0, 0, 0), (0,)),
    ((0, 0, 1), (1,)),
    ((0, 1, 0), (0,)),
    ((0, 1, 1), (1,)),
    ((1, 0, 0), (0,)),
    ((1, 0, 1), (1,)),
    ((1, 1, 0), (0,)),
    ((1, 1, 1), (1,)),
]
DATA_C = [
    ((0, 0, 0), (0,)),
    ((0, 0, 1), (0,)),
    ((0, 1, 0), (0,)),
    ((0, 1, 1), (0,)),
    ((1, 0, 0), (0,)),
    ((1, 0, 1), (0,)),
    ((1, 1, 0), (1,)),
    ((1, 1, 1), (1,)),
]
DATA_D = [
    ((0, 0, 0), (1,)),
    ((0, 0, 1), (0,)),
    ((0, 1, 0), (0,)),
    ((0, 1, 1), (0,)),
    ((1, 0, 0), (0,)),
    ((1, 0, 1), (0,)),
    ((1, 1, 0), (0,)),
    ((1, 1, 1), (0,)),
]
DATA = DATA_D
MAX_ITERATIONS = 99999
# DATA = DATA_OLD
INPUTS = len(DATA[0][0])
OUTPUTS = len(DATA[0][1])
HEIGHT = INPUTS+4 # not neccessarily correct
COLUMNS = 5  # layers
NODE_RESOLUTION = 99
TRIGGER_AMOUNT = NODE_RESOLUTION*0.6 # n.b. intentionally not flooring

MANUAL_NET = [
    {0: {'in_weights': {}, 'value': None, 'flip_val': True,},
     1: {'in_weights': {}, 'value': None, 'flip_val': True,},
     2: {'in_weights': {}, 'value': None, 'flip_val': True,}},
    {3: {'in_weights': {
        0: int(NODE_RESOLUTION*0.25),
        1: int(NODE_RESOLUTION*0.25),
        2: int(NODE_RESOLUTION*0.25)},
        'value': None, 'flip_val': False}}]


def main():
    print("start")
    print("Brute force")
    run_brute_force()
    print("mutater")
    run_mutater()
    # run_manual()
    print("end")


def run_brute_force():
    most_hits = 0
    successes = 0
    for i in range(0, MAX_ITERATIONS):
        local_net = generate_net()

        hits = 0
        for datum in DATA:
            inputs = [i*NODE_RESOLUTION for i in datum[0]]
            wanted_output = datum[1][0]
            nn_output = int(run_net(local_net, inputs)[0] >= TRIGGER_AMOUNT)
            print_net(local_net)
            if wanted_output == nn_output:
                hits += 1
        if hits > most_hits:
            most_hits = hits
        if hits == len(DATA):
            successes += 1
    print(f"was successfull with {successes} out of {MAX_ITERATIONS} iterations")
    print("best was", most_hits)


def run_mutater():
    best_so_far = 0
    net_barn = []
    successes = 0
    for i in range(0, MAX_ITERATIONS):
        if net_barn and (i % 2 == 0):
            local_net = mutate_net(net_barn[0])
        else:
            local_net = generate_net()

        hits = 0
        example = ""
        for datum in DATA:
            inputs = [i*NODE_RESOLUTION for i in datum[0]]
            wanted_output = datum[1][0]
            nn_output = int(run_net(local_net, inputs)[0] >= TRIGGER_AMOUNT)
            if wanted_output == nn_output:
                hits += 1
        if hits == best_so_far:
            net_barn.append(local_net)
        if hits > best_so_far:
            net_barn = [local_net]
            best_so_far = hits
        if hits == len(DATA):
            successes += 1
    print(f"was successfull with {successes} out of {MAX_ITERATIONS} iterations")


def mutate_once():
    return randof(MUTATION_RATE) == 0

MUTATION_RATE = 10  # i.e. 1 in 10 per number
def mutate_net(old_net):
    new_net = []
    column_no = 0
    for column in old_net:
        new_net.append({})
        for row_nid, row_val in column.items():
            new_net[column_no][row_nid] = {
                "in_weights": {},
                "value": None,
                "flip_val": row_val["flip_val"] if mutate_once() else randof(1)
            }
            if column_no != 0:
                in_weights = {}
                in_keys = row_val['in_weights'].keys()

                for mnid in in_keys:
                    if mutate_once():
                        in_weights[mnid] = randof(NODE_RESOLUTION)
                    else:
                        in_weights[mnid] = row_val['in_weights'][mnid]
                while sum(in_weights.values()) > NODE_RESOLUTION:
                    # in case it's gone over
                    for weight in in_weights:
                        in_weights[weight] = in_weights[weight] -1 or 0
                new_net[column_no][row_nid]["in_weights"] = in_weights
        column_no += 1
    return new_net


def run_manual():
    print("MANUAL")

    local_net = MANUAL_NET
    hits = 0
    print_net(local_net)
    for datum in DATA:
        print(f"datum: {datum}")
        inputs = [i*(NODE_RESOLUTION) for i in datum[0]]
        wanted_output = datum[1][0]
        nn_output = int(run_net(local_net, inputs)[0] >= TRIGGER_AMOUNT)
        print_net(local_net)
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


def print_net(net_to_print: dict):
    print(net_to_str(net_to_print))

def net_to_str(net_to_render: dict):
    rotated_screen = []
    column_index = 0
    print_null_val = '        '
    for column in net_to_render:
        row_index = 0
        for nid, node in column.items():
            if row_index > len(rotated_screen)-1:
                rotated_screen.append([])
            if column_index > len(rotated_screen[row_index])-1:
                rotated_screen[row_index].append(print_null_val)

            flipper = "F" if node['flip_val'] else "V"
            proto_val = node['value'] or 0
            middle = f"{flipper}:{proto_val:02}"

            while len(rotated_screen[row_index]) < column_index+1 :
                rotated_screen[row_index].append(print_null_val)
            in_weights_conv = ', '.join(f'{key}:{val:02}' for key, val in node['in_weights'].items())
            rotated_screen[row_index][column_index] = f"{in_weights_conv}->[{middle}]"

            row_index += 1
        column_index += 1
    res = ''
    for row in rotated_screen:
        res += "  ".join(row) + "\n"
    return res


def generate_net():
    new_net = []
    nid = 0
    # print(f"INPUTS {INPUTS} OUTPUTS {OUTPUTS} HEIGHT {HEIGHT}")
    for column_no in range(0, COLUMNS):
        new_net.append({})
        if column_no == 0:
            height_of_layer = INPUTS
        elif column_no + 1 >= COLUMNS:
            height_of_layer = OUTPUTS
        else:
            height_of_layer = HEIGHT
        # print(f"column_no is {column_no} and height of layer {height_of_layer}")
        for _ in range(0, height_of_layer):
            new_net[column_no][nid] = {
                "in_weights": {},
                "value": None,
                "flip_val": randof(1)
            }
            if column_no != 0:
                in_weights = {}
                in_keys = new_net[column_no - 1].keys()

                no_cuts = len(in_keys) - 1
                this_node_max = randof(NODE_RESOLUTION)
                # doing it with cuts to equally distribute the weight randomness
                cuts = [0] + sorted([randof(this_node_max) for _ in range(0, no_cuts)]) + [this_node_max]
                for mnid in in_keys:
                    in_weights[mnid] = cuts.pop() - cuts[-1]
                new_net[column_no][nid]["in_weights"] = in_weights
            nid += 1
    return new_net


def run_net(net_in_question, inputs):
    input_index = 0  # happens to correlatete with nid
    for input in inputs:
        net_in_question[0][input_index]["value"] = input
        input_index += 1

    last_column = 0
    last_outputs = []

    # check inputs for flipped vals
    for _, node in net_in_question[0].items():
        if node["flip_val"]:
            node["value"] = NODE_RESOLUTION - node["value"]

    for column in net_in_question[1:]:
        last_outputs = []
        for _, node in column.items():
            new_val = 0
            for back_nid, link_weight in node["in_weights"].items():
                new_val += funnel(net_in_question[last_column][back_nid]["value"], link_weight)
            if node["flip_val"]:
                new_val = NODE_RESOLUTION - new_val
            node["value"] = new_val
            last_outputs.append(node["value"])
        last_column += 1
    return last_outputs


if __name__ == '__main__':
    main()
