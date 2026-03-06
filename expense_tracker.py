expenses=[]

try:
    file=open('expenses.txt','r')
    for line in file:
        parts=line.strip().split(',')

        if len(parts)!=3:
            continue

        date=parts[0]
        item=parts[1]
        amount=float(parts[2])
        expenses.append([date,item,amount])
    file.close()
except FileNotFoundError:
    pass


while True:
    print('\nExpense Tracker:')
    print('1.Add expense')
    print('2.View expenses')
    print('3.Total spent')
    print('4.Search by item:')
    print('5.Exit')

    choice=input('Choose an option:')

    if choice=='1':
        date=input('Enter date:')
        item=input('Enter item:')
        amount=float(input('Enter amount:'))

        expenses.append([date,item,amount])

        file=open('expenses.txt','a')
        file.write(f'{date},{item},{amount}\n')
        file.close()

        print('Expense added.')
    elif choice=='2':
        print('\nYour Expenses:')
        for expense in expenses:
            print(expense[0],expense[1],expense[2])
    elif choice=='3':
        total=0
        for expense in expenses:
            total+=expense[2]

        print('Total spent:',total)
    elif choice=='4':
        search_item=input('Enter item to search:')

        for e in expenses:
            if e[1]==search_item:
                print(e[0],e[1],e[2])
    elif choice=='5':
        print('Goodbye')
        break
    else:
        print('Invalid option.')









