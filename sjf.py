# scheduling/sjf.py

def sjf_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: (x['arrival'], x['burst']))  # Sort by arrival time, then burst

    time = 0
    completed = 0
    gantt_chart = []
    result = []

    is_completed = [False] * n
    avg_tat = 0
    avg_wt = 0

    while completed != n:
        idx = -1
        min_bt = float('inf')

        for i in range(n):
            if processes[i]['arrival'] <= time and not is_completed[i]:
                if processes[i]['burst'] < min_bt:
                    min_bt = processes[i]['burst']
                    idx = i

        if idx != -1:
            start = time
            time += processes[idx]['burst']
            end = time

            tat = time - processes[idx]['arrival']
            wt = tat - processes[idx]['burst']

            result.append({
                'pid': processes[idx]['pid'],
                'arrival': processes[idx]['arrival'],
                'burst': processes[idx]['burst'],
                'completion': time,
                'turnaround': tat,
                'waiting': wt
            })

            gantt_chart.append((processes[idx]['pid'], start, end))

            avg_tat += tat
            avg_wt += wt
            is_completed[idx] = True
            completed += 1
        else:
            time += 1  # Idle time

    avg_tat /= n
    avg_wt /= n

    return result, gantt_chart, avg_wt, avg_tat
