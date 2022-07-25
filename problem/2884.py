def show_time(hour, minute):
    if hour == 0:
        if minute < 45:
            hour += 24
            minute += 60
            return print(hour - 1, minute - 45)
        else:
            return print(hour, minute - 45)
    else:
        if minute < 45:
            minute += 60
            return print(hour - 1, minute - 45)
        else:
            return print(hour, minute - 45)


h, m = map(int, input().split())
show_time(h, m)
