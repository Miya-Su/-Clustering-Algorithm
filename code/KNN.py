def getKnn(data,point,k):
    length = len(data)
    distance = []
    for index,y in enumerate(data):
            dist = EuclideanDist(point, y)
            distance.append([dist, index])

    QuickSort(distance,0,length-1)
    # print(distance)
    return distance[k][-1]

def getKnearests(data,point,k):
    length = len(data)
    distance = []
    for index,y in enumerate(data):
            dist = EuclideanDist(point, y)
            distance.append([dist, index])

    QuickSort(distance,0,length-1)
    return distance[1:k]

def QuickSort(arr,firstIndex,lastIndex):
    if firstIndex < lastIndex:
        divIndex = Partition(arr, firstIndex, lastIndex)

        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr, divIndex + 1, lastIndex)
    else:
        return

def Partition(arr, firstIndex, lastIndex):
    i = firstIndex - 1
    for j in range(firstIndex, lastIndex):
        if arr[j][0] <= arr[lastIndex][0]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[lastIndex] = arr[lastIndex], arr[i + 1]
    return i

def EuclideanDist(p1,p2):
    demesion = len(p1)
    sum = 0
    for i in range(0,demesion):
        sum += pow(p1[i] - p2[i],2)
    return float(pow(sum,0.5))
#
# if __name__ == '__main__':
#     X = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [10, 1], [11, 1], [12, 1], [13, 1], [16, 1],[17, 1], [18, 1], [19, 1], [20, 1], [25, 1], [26, 1]]
#     print(getKnn(X,[0,0],0))