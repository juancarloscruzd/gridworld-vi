class PDDLDomain:
    def __init__(self):
        self.predicates = []
        self.actions = []
        self.goal = []

class PDDLAction:
    def __init__(self, name, parameters, preconditions, effects):
        self.name = name
        self.parameters = parameters
        self.preconditions = preconditions
        self.effects = effects

def parse_pddl_domain(file_path):
    domain = PDDLDomain()
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_action = None
        for line in lines:
            print(line)
            tokens = line.strip().split()
            if tokens:
                if tokens[0] == 'states':
                    current_predicates = parse_predicates(tokens[1:])
                    domain.predicates.extend(current_predicates)
                elif tokens[0] == 'action':
                    current_action = PDDLAction(tokens[1], [], [], [])
                elif tokens[0] == ':parameters':
                    current_action.parameters = parse_parameters(tokens[1:])
                elif tokens[0] == ':precondition':
                    current_action.preconditions = parse_conditions(tokens[1:])
                elif tokens[0] == ':effect':
                    current_action.effects = parse_effects(tokens[1:])
                    domain.actions.append(current_action)
                elif tokens[0] == 'goal':
                    domain.goal = parse_conditions(tokens[1:])
    return domain

def parse_predicates(tokens):
    predicates = []
    current_predicate = ''
    for token in tokens:
        if '(' in token:
            current_predicate = token[1:]
        elif ')' in token:
            predicates.append(current_predicate)
            current_predicate = ''
        else:
            predicates.append(current_predicate + ' ' + token)
    return predicates

def parse_parameters(tokens):
    parameters = []
    current_parameter = ''
    for token in tokens:
        if '?' in token:
            current_parameter = token[1:]
        else:
            parameters.append((current_parameter, token))
            current_parameter = ''
    return parameters

def parse_conditions(tokens):
    conditions = []
    current_condition = ''
    for token in tokens:
        if '(' in token:
            current_condition = token[1:]
        elif ')' in token:
            conditions.append(current_condition)
            current_condition = ''
        else:
            conditions.append(current_condition + ' ' + token)
    return conditions

def parse_effects(tokens):
    effects = []
    current_effect = ''
    for token in tokens:
        if '(' in token:
            current_effect = token[1:]
        elif ')' in token:
            effects.append(current_effect)
            current_effect = ''
        else:
            effects.append(current_effect + ' ' + token)
    return effects

# Usage example
domain_file = './PruebasGrid/FixedGoalInitialState/navigation_1.net'
print(domain_file)
domain = parse_pddl_domain(domain_file)

# Accessing parsed data
print('Predicates:', domain.predicates)
for action in domain.actions:
    print('Action:', action.name)
    print('Parameters:', action.parameters)
    print('Preconditions:', action.preconditions)
    print('Effects:', action.effects)
print('Goal:', domain.goal)