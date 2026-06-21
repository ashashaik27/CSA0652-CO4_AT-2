def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


documents = [
    "AI",
    "Algorithms",
    "Binary Search",
    "Data Structures",
    "Machine Learning",
    "Python",
    "Search Engine"
]

documents.sort()

query = "Python"

result = binary_search(documents, query)

if result != -1:
    print("Document Found at Index:", result)
else:
    print("Document Not Found")
