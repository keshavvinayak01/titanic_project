# -*- coding: cp1252 -*-
import numpy as np
import pandas as pd
import seaborn as snb
import matplotlib.pyplot as plt
titanic = pd.read_csv( "C:\\Users\\Keshav Vinayak Jha\\Desktop\\Programs\\UdacityResources\\titanic_data.csv")
#sololearn


#total survived number
'''
titanic_a = titanic.groupby('Survived').groups
a = titanic_a.keys() == 1
print"{} people survived out of {} people".format(len(titanic_a[a]),len(titanic))
'''


#hierarchy of population
'''
first = titanic['Pclass'] == 1
second = titanic['Pclass'] == 2
third = titanic['Pclass'] == 3
sizes = [len(titanic[first]),len(titanic[second]),len(titanic[third])]
labels = ['first class','second class','third class']
explode = (0.1,0.1,0.1)
f,ax1 = plt.subplots()
ax1.pie(sizes,explode = explode,labels = labels,autopct = '%1.1f%%',shadow = True,startangle = 90)
ax1.axis('equal')
plt.show()



rich_and_alive =  titanic['Survived'] == 1
poor_and_alive = rich_and_alive & third
rich_and_alive = first & rich_and_alive

raa = float(len(titanic[rich_and_alive]))/float(len(titanic[first]))
paa = float(len(titanic[poor_and_alive]))/float(len(titanic[third]))
print "{}% of rich people survived \n{}% of poor people survived".format(raa*100,paa*100)

'''

#male and female survival rates
'''
male = titanic['Sex']== 'male'
female = titanic['Sex']== 'female'
survived = titanic['Survived'] == 1
maleS = male & survived
femaleS = female & survived
ms = float(len(titanic[maleS]))/float(len(titanic[male]))
fms = float(len(titanic[femaleS]))/float(len(titanic[female]))
print "{}% of all males survived(out of {} males) \n{}% of all females survived(out of {} females)".format(ms*100,len(titanic[male]),fms*100,len(titanic[female]))
'''

#cabin number hiearchy and survival rates
'''
def checkCabin(cabin):
    a = len(cabin)
    
    n = 0
    for i in xrange(0,a,3):
        n += 1
    cabin_no = cabin[0]
    n = str(n)
    return n + cabin_no
survived = titanic['Survived'] == 1
titanic = titanic.fillna('0')
Aclass = 0
Bclass = 0
Cclass = 0
Dclass = 0
Eclass = 0
Fclass = 0
Gclass = 0

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0

for i in xrange(len(titanic)):
    k = checkCabin(titanic.ix[i]['Cabin'])
    if(k == '0'):
        continue
    if(k[1] == 'A'):
        if(titanic.ix[i]['Survived'] == 1):
            A += 1*int(k[0])
        Aclass += int(k[0])

    elif(k[1] == 'B'):
        Bclass += int(k[0])
        if(titanic.ix[i]['Survived'] == 1):
            B += 1*int(k[0])  

    elif(k[1] == 'C'):
        Cclass += int(k[0])
        if(titanic.ix[i]['Survived'] == 1):
            C += 1*int(k[0])

    elif(k[1] == 'D'):
        Dclass += int(k[0])
        if(titanic.ix[i]['Survived'] == 1):
            D += 1*int(k[0])

    elif(k[1] == 'E'):
        Eclass += int(k[0])
        if(titanic.ix[i]['Survived'] == 1):
            E += 1*int(k[0])

    elif(k[1] == 'F'):
        Fclass += int(k[0])
        if(titanic.ix[i]['Survived'] == 1):
            F += 1*int(k[0])

    elif(k[1] == 'G'):
        Gclass += int(k[0])
        if(titanic.ix[i]['Survived'] == 1):
            G += 1*int(k[0])


total = (Aclass + Bclass + Cclass + Dclass + Eclass + Fclass + Gclass)/100.00
sizes = [Aclass/total,Bclass/total,Cclass/total,Dclass/total,Eclass/total,Fclass/total,Gclass/total]
explode = [0.2,0.1,0,0,0,0,0]
labels = ['A-class Cabins','B-class Cabins','C-class Cabins','D-class Cabins','E-class Cabins','F-class Cabins','G-class Cabins']

#plotting cabin occupancy rates
f,ax1 = plt.subplots()
ax1.pie(sizes,explode = explode,labels = labels,autopct = '%1.1f%%',shadow = True,startangle = 90)
ax1.axis('equal')
q = plt.figure(1)
q.show()


AS = 100*float(A)/float(Aclass)
BS = 100*float(B)/float(Bclass)
CS = 100*float(C)/float(Cclass)
DS = 100*float(D)/float(Dclass)
ES = 100*float(E)/float(Eclass)
FS = 100*float(F)/float(Fclass)
GS = 100*float(G)/float(Gclass)

#plotting cabin's survival rates
objects = ('A-class', 'B-class', 'C-class', 'D-class', 'E-class', 'F-class','G-class')
y_pos = np.arange(len(objects))
percentage = [AS,BS,CS,DS,ES,FS,GS]
g = plt.figure(2)
plt.bar(y_pos,percentage, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Survial Percentage')
plt.title('Cabin Classes')
g.show()
raw_input()
plt.close()
'''

#Survival rate of men and women with spouse/children compared to single women and men
'''
women = titanic['Sex'] == 'female'
adult= titanic['Age'] > 18
single = titanic['Parch'] == 0
notsingle = titanic['Parch']> 0
survived = titanic['Survived'] == 1
print "\n\n\t\t\t\t\t\tObservations done for adults\n\n"
print "total women with spouses/siblings/children : {} \ntotal women without spouses/children/siblings : {}".format(len(titanic[women&adult&notsingle]),len(titanic[women&adult&single]))

perTogether = 100*float(len(titanic[women&adult&notsingle&survived]))/float(len(titanic[women&adult&notsingle]))
perSingle = 100*float(len(titanic[women&adult&survived&single]))/float(len(titanic[women&adult&single]))
print "total women with spouses/siblings/children who survived {}, total women without spouses/siblings/children who survived : {} \nSurvival percentage of women with spouses/siblings/children : {}%, Survival percentage of women without spouses/siblings/children : {}%".format(len(titanic[women&adult&notsingle&survived]),len(titanic[women&adult&single&survived]),perTogether,perSingle)
print "\nthis observation shows that women as a whole were equally likely to survive regardless of whether they had family or not. doing the same observation for men...\n\n"

men = titanic['Sex'] == 'male'

print "total men with spouses/siblings/children : {} \ntotal men without spouses/children/siblings : {}".format(len(titanic[men&adult&notsingle]),len(titanic[men&adult&single]))

perTogetherM = 100*float(len(titanic[men&adult&notsingle&survived]))/float(len(titanic[men&adult&notsingle]))
perSingleM = 100*float(len(titanic[men&adult&survived&single]))/float(len(titanic[men&adult&single]))
print "total men with spouses/siblings/children who survived {}, total men without spouses/siblings/children who survived : {} \nSurvival percentage of men with spouses/siblings/children : {}%, Survival percentage of men without spouses/siblings/children : {}%".format(len(titanic[men&adult&notsingle&survived]),len(titanic[men&adult&single&survived]),perTogetherM,perSingleM)
print "\nthis observation shows that men as a whole were equally likely to survive regardless of whether they had family or not\nAnd also that women were more likely to survive than men in the given relational states "


'''
#How many children were present(<18 years),, and what percentage survived, also which age group of children survived with the highest percentage?
'''
children = titanic['Age'] < 18

survived = titanic['Survived'] == 1
titanic_children = titanic[children]
less_three = 0
less_six = 0
less_nine = 0
less_twelve = 0
less_fifteen = 0
less_eighteen = 0

less_threeS = 0
less_sixS = 0
less_nineS = 0
less_twelveS = 0
less_fifteenS= 0
less_eighteenS = 0

for i in titanic_children.index:
    age = titanic.ix[i]['Age']
    if(age > 18):
        continue
    elif(age < 3):
        if(titanic.ix[i]['Survived'] == 1):
            less_threeS += 1
        less_three += 1
    elif(age < 6):
        if(titanic.ix[i]['Survived'] == 1):
            less_sixS += 1
        less_six += 1
    elif(age < 9):
        if(titanic.ix[i]['Survived'] == 1):
            less_nineS += 1
        less_nine += 1
    elif(age < 12):
        if(titanic.ix[i]['Survived'] == 1):
            less_twelveS += 1
        less_twelve += 1
    elif(age < 15):
        if(titanic.ix[i]['Survived'] == 1):
            less_fifteenS += 1
        less_fifteen += 1
    elif(age < 18):
        if(titanic.ix[i]['Survived'] == 1):
            less_eighteenS += 1
        less_eighteen += 1


print('\n\nchildren less than the age of 3: {}\nchildren less than the age of 6: {}\nchildren less than the age of 9: {}\nchildren less than the age of 12: {}\nchildren less than the age of 15: {}\nchildren less than the age of 18: {}\n').format(less_three,less_six,less_nine,less_twelve,less_fifteen,less_eighteen)            

print('\n\nSurvived children less than the age of 3: {}\nSurvived children less than the age of 6: {}\nSurvived children less than the age of 9: {}\nSurvived children less than the age of 12: {}\nSurvived children less than the age of 15: {}\nSurvived children less than the age of 18: {}\n').format(less_threeS,less_sixS,less_nineS,less_twelveS,less_fifteenS,less_eighteenS)            
'''
#Survival rate of adults vs children
'''
adults = titanic['Age'] >= 18
children = titanic['Age'] < 18
survived = titanic['Survived'] == 1
pera = 100*float(len(titanic[adults&survived]))/float(len(titanic[adults]))
perc = 100*float(len(titanic[children&survived]))/float(len(titanic[children]))
print 'total children : {} \ntotal survived children : {} \npercentage of survived children : {:.2f}%.\n\n\ntotal adults : {} \ntotal survived adults : {} \npercentage of survived adults : {:.2f}%'.format(len(titanic[children]),len(titanic[children&survived]),perc,len(titanic[adults]),len(titanic[adults&survived]),pera)
'''
