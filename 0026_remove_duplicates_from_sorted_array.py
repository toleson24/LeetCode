# import time

def removeDuplicates(nums: list[int]) -> int:
	k: int = 0
	l: int = len(nums)

	if l < 1:
		return k

	output: list[int] = []
	for n in nums:
		if n not in output:
			output.append(n)
			k += 1

	# print(f'Output: {output}')

	l = len(output)
	for i, _ in enumerate(nums):
		if i < l:
			nums[i] = output[i]
		else:
			nums[i] = "_"

	print(f'Updated nums: {nums}')
	print(f'Unique: {k}')

	return k


def main():
	nums1: list[int] = [1, 1, 2]
	nums2: list[int] = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

	removeDuplicates(nums1)
	removeDuplicates(nums2)


if __name__ == "__main__":
	main()

