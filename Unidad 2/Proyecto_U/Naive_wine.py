
file2read = open("naive_wine_training_.csv")
file_content = file2read.readlines()

#############################################################################################
dataset = []
for i in file_content:
    dataset.append((i.replace("\n" ,"")).split(","))
headers = dataset[0]
del dataset[0]  # remove headers from dataset
#############################################################################################
##count registers per class
#############################################################################################
probabilities = []
auxiliar = {}
for register_index in range(len(dataset)):
    label = dataset[register_index][-1]
    if label in auxiliar:
        auxiliar[label] += 1
    else:
        auxiliar[label] = 1
probabilities.append(auxiliar)
#############################################################################################
##count registers per attribute
#############################################################################################
for attribute_index in range(len(dataset[0] ) -1):
    auxiliar = {}
    for register_index in range(len(dataset)):
        v_label = dataset[register_index][attribute_index]
        v_class = dataset[register_index][-1]
        if (v_label ,v_class) in auxiliar:
            auxiliar[(v_label ,v_class)] += 1
        else:
            auxiliar[(v_label ,v_class)] = 1
            # print(v_label, "  ", v_class)
    probabilities.append(auxiliar)
#############################################################################################
##calculate probabilities per attribute
#############################################################################################
for index in range(1, len(probabilities)):
    for c in probabilities[index]:  # per attribute
        # print(probabilities[0][c[1]])
        probabilities[index][c] =  probabilities[index][c ] /probabilities[0][c[1]]
    # print(probabilities[0][c])
#############################################################################################
##calculate probabilities per class
#############################################################################################
for c in probabilities[0]:
    probabilities[0][c] = probabilities[0][c ] /len(dataset)
    # print(probabilities[0][c])
#############################################################################################
#############################################################################################
## TESTING
#############################################################################################
file2read = open("naive_wine_test_.csv")
file_content = file2read.readlines()
#############################################################################################
dataset = []
for i in file_content:
    dataset.append((i.replace("\n" ,"")).split(","))
headers = dataset[0]
del dataset[0]  # remove headers from dataset
#############################################################################################

correct_classify = 0

for k in range(len(dataset))  :  # aplica la clasificacion exactamente igual por cada conjunto rgistro k
    register = dataset[k]
    sum = 1
    probabilities_per_class = {}
    for c in probabilities[0]:
        # print(c)
        auxiliar = probabilities[0][c]
        for index in range(1, len(probabilities)):
            if  (register[index -1], c) in probabilities[index]:
                auxiliar *= probabilities[index][(register[index -1], c)]
            else:
                auxiliar = 0  # nullify the product
        sum += auxiliar
        probabilities_per_class[c] = auxiliar

    max = -9999
    c_toAssign = ""
    for p in probabilities_per_class:
        probabilities_per_class[p] = probabilities_per_class[p] /sum
        if probabilities_per_class[p] > max:
            max = probabilities_per_class[p]
            c_toAssign = p
    #############################################################################################

    print("Real Class: ", dataset[k][-1] ,"Assigned Class: ", c_toAssign, " Probability: ", round(max * 100, 4), "%")

    if dataset[k][-1] == c_toAssign:  # checa si la clase real y la clase asignada son iguales
        correct_classify += 1

print("\n\nCorrect Classify: ", correct_classify, " Total Evaluated: ", len(dataset), " Efficiency: ",
      round(correct_classify / len(dataset) * 100, 4), "%")

