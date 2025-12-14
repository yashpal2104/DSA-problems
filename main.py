
from __future__ import annotations

from collections import defaultdict
from typing import Iterable, List


def total_fruit_bruteforce(fruits: List[int]) -> int:
	"""Brute force: longest subarray with at most 2 distinct values.

	Time: O(n^2), Space: O(1) extra (distinct set size <= 3 during scan).
	"""

	n = len(fruits)
	best = 0

	for i in range(n):
		types = set()
		for j in range(i, n):
			types.add(fruits[j])
			if len(types) > 2:
				break
			best = max(best, j - i + 1)

	return best


def total_fruit_optimal(fruits: List[int]) -> int:
	"""Optimal sliding window: longest subarray with at most 2 distinct values.

	Time: O(n), Space: O(1) extra (map holds <= 2 keys after shrinking).
	"""

	count: dict[int, int] = defaultdict(int)
	best = 0
	l = 0

	for r, fruit in enumerate(fruits):
		count[fruit] += 1

		while len(count) > 2:
			left_fruit = fruits[l]
			count[left_fruit] -= 1
			if count[left_fruit] == 0:
				del count[left_fruit]
			l += 1

		best = max(best, r - l + 1)

	return best


def _parse_ints(line: str) -> List[int]:
	line = line.strip()
	if not line:
		return []
	return [int(x) for x in line.split()]


def solve() -> None:
	"""CLI:

	Input format (simple):
	  One line with space-separated integers representing fruit types.

	Output:
	  Two lines:
		brute=<answer>
		optimal=<answer>
	"""

	import sys

	data = sys.stdin.read().strip().splitlines()
	if not data:
		return

	fruits = _parse_ints(data[0])
	brute = total_fruit_bruteforce(fruits)
	optimal = total_fruit_optimal(fruits)

	sys.stdout.write(f"brute={brute}\n")
	sys.stdout.write(f"optimal={optimal}\n")


def _self_test() -> None:
	cases = [
		([], 0),
		([1], 1),
		([1, 2, 1], 3),
		([0, 1, 2, 2], 3),
		([1, 2, 3, 2, 2], 4),
		([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),
	]

	for fruits, expected in cases:
		b = total_fruit_bruteforce(fruits)
		o = total_fruit_optimal(fruits)
		assert b == expected, (fruits, b, expected)
		assert o == expected, (fruits, o, expected)


if __name__ == "__main__":
	# Run a quick sanity check, then proceed to solve.
	_self_test()
	solve()

