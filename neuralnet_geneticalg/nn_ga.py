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

INPUTS = 2
OUTPUTS = 2
LAYERS = 1  # middle layers
HEIGHT = INPUTS
neural_network = {}

def main():
    print("making nn")
    nid = 2
    for layer in range(0, LAYERS):
        for row in range(0, HEIGHT):
            neural_network[nid] = {
                "in": 12,
                "outs": {
                    4: 11,
                }
            }
            nid += 1

    print("print nn")
    for nid, node in neural_network.items():
        print(f"{node['in']}->{nid}->{node['outs']}\n")


if __name__ == '__main__':
    main()
