"""
A child is running up a staircase with n steps, and can hop either 1 step,
2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

Bonus solve this problem in better than O(3^N) time.
"""

# O(3^n)
def step(steps):
    if steps < -1:
        return 0
    if steps == 0:
        return 1
    else:
        return step(steps-1) + step(steps-2) + step(steps-3)

# better
def otherSteps(steps, ways_at_every_step):
    if steps < -1:
        return 0
    if steps == 0:
        return 1
    elif ways_at_every_step[steps] > -1:
        return ways_at_every_step[steps]
    else:
        ways_at_every_step[steps] = otherSteps(steps-1, ways_at_every_step) +\
                                    otherSteps(steps-2, ways_at_every_step) + otherSteps(steps-3, ways_at_every_step)
        return ways_at_every_step[steps]

print(otherSteps(900, [-1]*901))
