#!/usr/bin/env python

answer = sum([i for i in range(1000) if not (i % 3 and i % 5)])

print(answer)
