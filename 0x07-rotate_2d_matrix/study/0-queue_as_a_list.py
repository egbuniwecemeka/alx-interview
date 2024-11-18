#!/usr/bin/env python3
"""A simple script for  using Queues as Lists"""

from collections import deque


queue = deque(['Nigeria', 'Lagos'])
queue.append('Luxembourg')  # append to end of list
queue.append('France')
queue.append('UK')
queue.popleft() # removes outermost left item (first)
queue.popleft()
print(f'{queue}')
