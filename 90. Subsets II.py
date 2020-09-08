def subset(nums):
	seen = set([()])
	for n in sorted(nums):
		seen.update([s + (n,) for s in seen])
	return list(map(list, seen))
	
