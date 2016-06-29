# merge_sort.py


def merge_sort(list):
    if len(list) > 1:
        mean = len(list) // 2
        lefthand = list[:mean]
        righthand = list[mean:]

        merge_sort(lefthand)
        merge_sort(righthand)

        i = 0
        j = 0
        k = 0

        # проходим по основному списку, пока i или j не упрутся в длину соотв, подсписков
        while i < len(lefthand) and j < len(righthand):
            if lefthand[i] < righthand[j]:
                list[k] = lefthand[i]
                i += 1
            else:
                list[k] = righthand[j]
                j += 1
            k += 1

        # при необходимости доходим до конца левого списка
        while i < len(lefthand):
            list[k] = lefthand[i]
            i += 1
            k += 1

        # при необходимости доходим до конца правого списка
        while j < len(righthand):
            list[k] = righthand[j]
            j += 1
            k += 1

test_list = [57, 94, 15, 82, 62, 38, 39, 47, 52, 20, 2, 96]
merge_sort(test_list)
print(test_list)
