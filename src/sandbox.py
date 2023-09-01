
def sort_coll(coll, pred):
    i = 0
    while i < len(coll)-1:
        candidate_idx = -1
        candidate = coll[i]

        j = i + 1
        while j < len(coll):
            if pred(coll[j], candidate):
                candidate_idx = j
                candidate = coll[j]

            j += 1
        else:
            if candidate_idx != -1:
                coll[i], coll[candidate_idx] = coll[candidate_idx], coll[i]

        i += 1


def pred(elem1, elem2):
    return elem1[1] < elem2[1]


sortable = [("data", 5),
            ("hello", 6),
            ("world", 1),
            ("python", 8),
            ("C++", 54)]

sort_coll(sortable, pred)
print(sortable)





def scoped_func(arg1, arg2):
    ret = arg1 + arg2
    print(ret)


scoped_func(5, 6)

print(arg1)