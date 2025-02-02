# Day 7: The Treachery of Whales

from santas_little_helpers import *
from statistics import median, mean

fuel_linear = lambda candidate, positions: sum(abs(position-candidate) for position in positions)
sum_series = lambda x: x * (1 + x)/2 # this is sum of range(1,x+1)
fuel_incremental = lambda candidate, positions: sum(sum_series(abs(position-candidate)) for position in positions)


def find_fuel(crab_data):
     constant_pos, incremental_pos = (median(crab_data), int(mean(crab_data)))
     party_1 = fuel_linear(constant_pos, crab_data)
     party_2 = fuel_incremental(incremental_pos, crab_data)
     return int(party_1), int(party_2)


crab_data = get_input('inputs/07.txt', True,',')

print_solutions(*find_fuel(crab_data))
