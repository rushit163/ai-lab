colors = ['Red', 'Green', 'Blue']

states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

neighbors = {}
neighbors['WA'] = ['NT', 'SA']
neighbors['NT'] = ['WA', 'SA', 'Q']
neighbors['SA'] = ['WA', 'NT', 'Q', 'NSW', 'V']
neighbors['Q'] = ['NT', 'SA', 'NSW']
neighbors['NSW'] = ['SA', 'Q', 'V']
neighbors['V'] = ['SA', 'NSW']
neighbors['T'] = []

colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print (colors_of_states)


main()

