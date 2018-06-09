def Kadane(Arr):
    local_start = start = end = tot_sum = 0
    # defalt setting
    # max_sum, min_start, min_end
    for i in range(1, len(Arr)):
        if Arr[i - 1] + Arr[i] < Arr[i]:
            local_start = i
        else:
            Arr[i] = Arr[i - 1] + Arr[i]
        if Arr[i] > tot_sum:
            tot_sum = Arr[i]
            start = local_start
            end = i
    end += 1 # conventional python end point
    return {
        'interval': '[' + str(start) + ', ' + str(end) + ')',
        'sum': tot_sum, 0: (start, end), 1: tot_sum
    }
