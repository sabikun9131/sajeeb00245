# scheduling/fcfs.py

def fcfs_scheduling(processes):
    # Sort by Arrival Time
    processes.sort(key=lambda x: x['arrival'])

    time = 0
    result = []
    gantt_chart = []

    for process in processes:
        pid = process['pid']
        at = process['arrival']
        bt = process['burst']

        if time < at:
            time = at  # CPU is idle

        start = time
        time += bt
        ct = time
        tat = ct - at
        wt = tat - bt

        result.append({
            'pid': pid,
            'arrival': at,
            'burst': bt,
            'completion': ct,
            'turnaround': tat,
            'waiting': wt
        })

        gantt_chart.append((pid, start, ct))

    avg_wt = sum(p['waiting'] for p in result) / len(result)
    avg_tat = sum(p['turnaround'] for p in result) / len(result)

    return result, gantt_chart, avg_wt, avg_tat
