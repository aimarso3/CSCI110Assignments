def to_secs(hours, minutes, seconds):
    ...     if minutes < 0 or seconds < 0:
...         return -1  # Return -1 for invalid input
...     total_seconds = (hours * 3600) + (minutes * 60) + seconds
...     return total_seconds
... 
... # Test cases
... def test(actual, expected):
...     if actual == expected:
...         print("Pass")
...     else:
...         print("Fail")
... 
... test(to_secs(2, 30, 10), 9010)
... test(to_secs(2, 0, 0), 7200)
... test(to_secs(0, 2, 0), 120)
... test(to_secs(0, 0, 42), 42)
... test(to_secs(0, -10, 10), -1)
