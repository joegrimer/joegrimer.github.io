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
MAX_ITERATIONS = 504
# DATA = DATA_OLD
INPUTS = len(DATA[0][0])
OUTPUTS = len(DATA[0][1])
HEIGHT = INPUTS+1 # not neccessarily correct
COLUMNS = 3  # layers
NODE_RESOLUTION = 99
TRIGGER_AMOUNT = NODE_RESOLUTION*0.6 # n.b. intentionally not flooring

MANUAL_NET = [
    {0: {'in_weights': {}, 'value': None},
     1: {'in_weights': {}, 'value': None},
     2: {'in_weights': {}, 'value': None}},
    {3: {'in_weights': {0: NODE_RESOLUTION*0.5, 1: NODE_RESOLUTION*0.5, 2: 0}, 'value': None}}]


def main():
    print("start")
    run_iterations()
    # run_manual()
    print("end")


def run_iterations():
    most_hits = 0
    print(f"INPUTS {INPUTS}")
    print(f"HEIGHT {HEIGHT}")
    print(f"OUTPUTS {OUTPUTS}")
    for i in range(0, MAX_ITERATIONS):
        local_net = generate_net()

        hits = 0
        example = ""
        for datum in DATA:
            example += f"datum: {datum}\n"
            inputs = [i*NODE_RESOLUTION for i in datum[0]]
            wanted_output = datum[1][0]
            nn_output = int(run_net(local_net, inputs)[0] >= TRIGGER_AMOUNT)
            example += net_to_str(local_net)
            example += f"wanted {wanted_output} and outputs {nn_output}\n"
            if wanted_output == nn_output:
                hits += 1
        if hits > most_hits:
            most_hits = hits
            print("---------")
            print("Best went up: ", most_hits)
            print(example)
        if hits == len(DATA):
            print("IT WORKED", i, "for len", len(DATA))
            print("--------------------------------")

            break
    print(f"stopped at {i+1} out of {MAX_ITERATIONS} iterations")
    print("best was", most_hits)


def run_manual():
    print("MANUAL")

    local_net = MANUAL_NET
    hits = 0
    print_net(local_net)
    for datum in DATA:
        print(f"datum: {datum}")
        inputs = [i*(NODE_RESOLUTION) for i in datum[0]]
        wanted_output = datum[1][0]
        nn_output = int(run_net(inputs)[0] >= TRIGGER_AMOUNT)
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
            # print("rotated_sceen", rotated_screen)
            # print("r_id", r_id)
            # print("c_id", c_id)
            middle = f"V:{node['value']:02}" if node["value"] is not None else f"{nid:02}"

            # print(f"row_index is {row_index} column_index is {column_index}")
            # print(f"rotated_screen is {rotated_screen}")
            while len(rotated_screen[row_index]) < column_index+1 :
                rotated_screen[row_index].append(print_null_val)
            in_weights_conv = ', '.join(f'{key}:{val:02}' for key, val in node['in_weights'].items())
            rotated_screen[row_index][column_index] = f"{in_weights_conv}->[{middle}]"
            # print(f"now rotated_screen is {rotated_screen}")
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
            }
            if column_no != 0:
                in_weights = {}
                in_keys = new_net[column_no - 1].keys()

                no_cuts = len(in_keys) - 1
                this_node_max = randof(NODE_RESOLUTION)
                # doing it with cuts to equally distribute the weight randomness
                cuts = [0] + sorted([this_node_max for _ in range(0, no_cuts)]) + [this_node_max]
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
    for column in net_in_question[1:]:
        last_outputs = []
        for _, node in column.items():
            new_val = 0
            for back_nid, link_weight in node["in_weights"].items():
                new_val += funnel(net_in_question[last_column][back_nid]["value"], link_weight)
            node["value"] = new_val
            last_outputs.append(node["value"])
        last_column += 1
    return last_outputs


if __name__ == '__main__':
    main()
