from math import comb

def min_buckets(arr):
    
    # Time complexity analysis:
    # - Building the frequency dictionary: O(n)
    # - Sorting the array based on frequency and value: O(n log n)
    # - Creating buckets: O(n)
    # Overall time complexity: O(n log n)

    # Step 1: sort the array based on frequency. We use a dict for this
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    sorted_arr = sorted(arr, key=lambda x: (-freq_dict[x], x))

    res = [] # this holds the buckets

    # Step 2: coalese into buckets
    while sorted_arr:
        max_val = sorted_arr[0]
        bucket = []
        # we create the bucket size based on the most frequent element
        while sorted_arr and sorted_arr[0] == max_val:
            bucket.append(sorted_arr.pop(0))
        fill_to = len(bucket) + 1

        # we fill the remainder of the bucket with the smallest elements
        while sorted_arr and len(bucket) < fill_to:
            bucket.append(sorted_arr.pop())
        res.append(bucket)

    # we return the length of the buckets, not the buckets themselves
    print(res)
    return len(res)




    # sort the arrays most elements (max gets pop lefted, min pop righted)

    # sort max elements into the most buckets

def count_threatening_positions(n, m):
    total_placements = comb(n*m, 3)

    # Count positions where a knight threatens another knight
    threatening_positions = 0
    
    # Iterate over all positions on the board
    for row in range(n):
        for col in range(m):
            # Count how many positions are threatened by a knight at (row, col)
            threats = 0
            for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
                if 0 <= row + dr < n and 0 <= col + dc < m:
                    threats += 1
            # For each threatening position, calculate how many ways to place the third knight
            # This is a simplification and doesn't accurately account for overlapping threats or edge/corner reductions
            if threats > 0:
                threatening_positions += comb(n*m - threats - 1, 1)
    
    return total_placements - threatening_positions

if __name__ == "__main__":
    # arr = [1, 2, 2, 3, 4]
    # arr = [5, 1, 2, 2, 3, 4] # 3
    # res = min_buckets(arr)
    # print(res)
    n, m = 7, 7
    threatening_positions = count_threatening_positions(n, m)
    print(threatening_positions)



    
