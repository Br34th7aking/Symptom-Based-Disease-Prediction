# generate all the symptoms from the csv file

with open('Training.csv', 'r') as infile:

    data = infile.readlines()

outfile = open('all_symptoms.txt', 'w')

outfile.write(str(data[0].split(',')[:-1]))

outfile.close()

symptoms = data[0].split(',')[:-1]


disease_and_symptom = {}

for i in range(1,len(data)):
    v = data[i].rstrip().split(',')
    disease = v[-1]
    disease_and_symptom[disease] = []
    for k in range(len(v)-1):
        if v[k] == '1':
            disease_and_symptom[disease].append(symptoms[k])

outfile = open('disease_and_symptom.txt', 'w')
outfile.write(str(disease_and_symptom))
outfile.close()

# print(possible_diseases)
