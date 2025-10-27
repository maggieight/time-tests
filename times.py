import datetime


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    total_seconds = (end_time_s - start_time_s).total_seconds()
    interval_length = (total_seconds - gap_between_intervals_s * (number_of_intervals - 1)) / number_of_intervals

    sec_range = [
        (
            start_time_s + datetime.timedelta(seconds=i * (interval_length + gap_between_intervals_s)),
            start_time_s + datetime.timedelta(seconds=i * (interval_length + gap_between_intervals_s) + interval_length)
        )
        for i in range(number_of_intervals)
    ]

    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            t1_start = datetime.datetime.strptime(start1, "%Y-%m-%d %H:%M:%S")
            t1_end = datetime.datetime.strptime(end1, "%Y-%m-%d %H:%M:%S")
            t2_start = datetime.datetime.strptime(start2, "%Y-%m-%d %H:%M:%S")
            t2_end = datetime.datetime.strptime(end2, "%Y-%m-%d %H:%M:%S")

            low = max(t1_start, t2_start)
            high = min(t1_end, t2_end)

            if low < high:
                overlap_time.append(
                    (low.strftime("%Y-%m-%d %H:%M:%S"), high.strftime("%Y-%m-%d %H:%M:%S"))
                )
    return overlap_time


if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
