def turn_off(mask, i): return mask - (1 << i)
def turn_off2(mask, i): return mask & ~(1 << i)
def turn_on(mask,i): return mask | (1<<i)
def is_on(mask,i): return mask & (1<<i)
def flip(mask, i): return mask ^ (1<<i)
def allSelected(mask, n): return mask == ((1 << n) - 1)
