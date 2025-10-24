import csv as csv
import pandas as pd
class Schikshal:
    def __init__(valk,name,age,rank,power,element,category):
        valk.name=name
        valk.age=age
        valk.rank=rank
        valk.power=power
        valk.element=element
        valk.category=category           #__str__, and any function with the class' self are called methods of the class.
    def __str__(valk):
        return f"valkyrie: {valk.name}, age:{valk.age},rank:{valk.rank},power:{valk.power},element:{valk.element},category:{valk.category}"
    def load(filename='valkyrie.csv'):
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                return [Schikshal(row[0], int(row[1]), row[2], row[3], row[4], row[5]) for row in reader]
        except FileNotFoundError:
            return []
    def save(filename='valkyrie.csv'):
        with open(filename,'w',newline='') as valkyrie:
            valky= csv.writer(valkyrie)
            valky.writerow(['Name', 'Age', 'Rank', 'Power', 'Element', 'Category'])
            for valk in valkyrie_database:
                valky.writerow([valk.name, valk.age, valk.rank, valk.power, valk.element, valk.category])

valkyrie_database = Schikshal.load()
print('**************Valkyrie database*********************')
while True:
    print('What would you like to do?')
    print('-----------------------------------')
    print('1. Add a new Valkyrie')
    print('-----------------------------------')
    print('2. View all Valkyries')
    print('-----------------------------------')
    print('3. Search for a Valkyrie')
    print('-----------------------------------')
    print('4.Exit')
    print('-----------------------------------')
    a= int(input('Enter your choice:'))
    if a==1:
        while True:
            print('Enter the details of the Valkyrie:')
            name=input('Name:').title()
            age=int(input('Age:'))
            rank=input('Rank:').capitalize()
            power=input('power:').capitalize()
            element=input('Element:').capitalize()
            category=input('Category:').capitalize()
            valk_profile=Schikshal(name,age,rank,power,element,category)
            valkyrie_database.append(valk_profile)
            print(f'{name} has been added in the database!')
            c=input('do you want to continue adding new valkyries?')
            if c.lower()=='no':
                break
            elif c.lower()=='yes':
                continue    
            else:
                print('say yes or no')
                break
        print()
    if a==2:
       if valkyrie_database==[]:
            print('No valkyries in the database!')
       else:
            data=[[valk.name, valk.age, valk.rank, valk.power, valk.element, valk.category] for valk in valkyrie_database]
            df=pd.DataFrame(data, columns=['Name', 'Age', 'Rank', 'Power', 'Element', 'Category'])
            print(df)
    elif a==3:
        while True:
            e=input('Enter the name of the valkyrie you want to search for:').title()
            for valk in valkyrie_database:
                if valk.name==e:
                    print(valk)
                else:
                    print(f'Valkyrie profile does not exist')
            f=input('do you want to see any other valkyrie?(say yes or no):')
            if f.lower()=='no':
                break
            elif f.lower()=='yes':
                continue 
            else:
                print('say yes or no')
                break
    elif a==4:
        print('Thank you for using the database')
        break    
    else:
        print('Error!Data breach attempt,breaking database.')
Schikshal.save()
