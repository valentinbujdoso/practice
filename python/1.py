def recentItems(logs):
    # Write your code here
    log_dict = {}
    i = 0
    for log in logs:
        log_dict[log] = i
        i -= 1

    return sorted(log_dict, key=log_dict.get)
