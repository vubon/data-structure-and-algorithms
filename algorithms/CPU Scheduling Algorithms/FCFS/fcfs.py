"""
FCFS means  First Come First Serve
"""


def finding_waiting_time(processes, lengths, br, wt):
    """
    :param processes:
    :param lengths:
    :param br:
    :param wt:
    :return:
    """
    # first waiting time is 0
    wt[0] = 0

    for i in range(1, lengths):
        wt[i] = br[i - 1] + wt[i - 1]


total_processes = [1,2,3,4,5]
burst_time = [21, 10, 30, 15, 25]
total_lengths = len(total_processes)
print(finding_waiting_time(total_processes, total_lengths, burst_time,))
