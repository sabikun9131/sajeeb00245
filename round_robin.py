from collections import deque

def round_robin_scheduling(processes, time_quantum):
    # Sorting processes by Arrival Time (AT)
    processes.sort(key=lambda x: x['arrival'])
    
    queue = deque()
    time = 0
    completed = 0
    result = []
    total_wt = 0
    total_tat = 0

    while completed < len(processes):
        for process in processes:
            if process['arrival'] <= time and process['pid'] not in [p['pid'] for p in result]:
                queue.append(process)

        if queue:
            current_process = queue.popleft()
            start_time = time
            # Ensure that the end time does not exceed burst time or quantum
            end_time = min(start_time + time_quantum, current_process['arrival'] + current_process['burst'])
            
            current_process['waiting'] = max(0, start_time - current_process['arrival'])
            current_process['turnaround'] = end_time - current_process['arrival']
            current_process['completion'] = end_time

            total_wt += current_process['waiting']
            total_tat += current_process['turnaround']

            # Update time to end time after executing the current process
            time = end_time
            result.append(current_process)

            # If burst time is left, update the process and add it back to the queue
            remaining_burst = current_process['burst'] - (end_time - start_time)
            if remaining_burst > 0:
                current_process['arrival'] = time  # Update the arrival time for the next round
                current_process['burst'] = remaining_burst
                queue.append(current_process)

            completed += 1
        else:
            time += 1  # If no process is available, increase time and check again

    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)

    gantt = [(process['pid'], process['arrival'], process['completion']) for process in result]

    return result, gantt, avg_wt, avg_tat
