def find_waiting_time(process_number, bt, qt):
    """
    :param process_number:
    :param bt:
    :param qt:
    :return:
    """
    rt = [0] * process_number

    for item in range(process_number):
        rt[item] = bt[item]

    current_time = 0
    waiting_time_list = [0] * process_number

    while 1:
        done = True

        for item in range(process_number):
            if rt[item] > 0:
                done = False
                if rt[item] > qt:
                    current_time += qt
                    rt[item] -= qt
                else:
                    current_time = current_time + rt[item]
                    waiting_time_list[item] = current_time - bt[item]
                    rt[item] = 0
        if done:
            break

    return waiting_time_list


def find_turn_around_time(process_number, bt, wt):
    """
    :param process_number:
    :param bt:
    :param wt:
    :return:
    """
    turn_around_time = [0] * process_number
    for item in range(process_number):
        turn_around_time[item] = bt[item] + wt[item]
    return turn_around_time


if __name__ == "__main__":
    # Process id's
    processes_ids = [1, 2, 3]
    process_num = len(processes_ids)

    # Burst time of all processes
    burst_time = [10, 5, 8]

    # Time quantum
    quantum_time = 3

    waiting_time = find_waiting_time(process_num, burst_time, quantum_time)
    tat = find_turn_around_time(process_num, burst_time, waiting_time)

    print("Process Number     Turn Around Time     Waiting Time")
    for num in range(process_num):
        print(num + 1, "\t\t\t\t\t ", tat[num], '\t\t\t\t\t', waiting_time[num])

    print("Average waiting time(AWT) is %.5f" % (sum(waiting_time) / process_num))
    print("Average turn around time(ATAT) is %.5f" % (sum(tat) / process_num))
