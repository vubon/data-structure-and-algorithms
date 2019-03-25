agent_one = []
agent_two = []
agent_three = []
total_agents = 3
task_num = [1, 2, 3]
quantum_time = 2

new_task = [1, 2, 3, 4]


def initial_disturbed(tasks, agent):
    """
    :param tasks:
    :param agent:
    :return:
    """
    if agent == len(tasks):
        for item in tasks:
            agent_one.append(item)
            agent_two.append(item)
            agent_three.append(item)
