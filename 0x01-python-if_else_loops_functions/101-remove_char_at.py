#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        remove = str[:n] + str[n + 1:]
        return (remove)
    else:
        return (str)
