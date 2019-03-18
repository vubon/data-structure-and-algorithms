"""
FCFS means  First Come First Serve
"""


def finding_waiting_time(lengths, br, wt):
    """
    :param lengths:
    :param br:
    :param wt:
    :return:
    """
    # first waiting time is 0
    wt[0] = 0

    for i in range(1, lengths):
        wt[i] = br[i - 1] + wt[i - 1]


# Function to calculate turn
# around time
def find_turn_around_time( n, bt, wt, tat):
    # calculating turnaround
    # time by adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]

    # Function to calculate


def find_avg_time(n, bt):
    """
    :param n:
    :param bt:
    :return:
    """
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    # Function to find waiting
    # time of all processes
    finding_waiting_time(n, bt, wt)

    # Function to find turn around
    # time for all processes
    find_turn_around_time(n, bt, wt, tat)

    # Display processes along
    # with all details
    print("Processes Burst time " + " Waiting time " + " Turn around time")

    # Calculate total waiting time
    # and total turn around time
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t\t" + str(bt[i]) + "\t\t\t " + str(wt[i]) + "\t\t\t " + str(tat[i]))

    print("Average waiting time = " +
          str(total_wt / n))
    print("Average turn around time = " +
          str(total_tat / n))


if __name__ == "__main__":
    # process id's
    total_processes = [1, 2, 3, 4, 5]
    # burst time
    burst_time = [21, 10, 30, 15, 25]
    # all processes lengths
    total_lengths = len(total_processes)

    find_avg_time(total_lengths, burst_time)
