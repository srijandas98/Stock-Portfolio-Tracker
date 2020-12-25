import pandas as pd
import pandas_datareader as pdr
from time import sleep  # to periodically get the prices

symbols = "AMZN GOOG NFLX FB GLD SPY".split()  # for listing different companies
options="Track Default List, Show List, Add to Default, Edit Default List, Add New List, Quit".split(",")

#print(symbols)
def get_prices(symbols):
    print(symbols.sort())
    return pdr.get_quote_yahoo(symbols)['price']  # live stock data for finance from yahoo about apple inc

def show_default(symbols):
    symbols.sort()
    return symbols

def edit_default(symbols):
    print("Select symbol to Delete: ")
    for i in range(1,len(symbols)+1):
        print("{} - {}".format(i,symbols[i-1]))
    remove=symbols.pop(int(input())-1)
    print("{} is Removed".format(remove))



def add_to_default(symbols):
    print("Enter symbols to Add: ")
    symbol=input().upper()
    while symbol!="":
        symbols.append(symbol)
        symbol=input("Enter symbol to add: Hit ENTER to Quit!")


def add_list():
    new_list=[]
    print("Enter symbol to add: ")
    symbol= input().upper()
    while symbol!="":
        new_list.append(symbol)
        symbol= input("Enter a symbol to add or enter: ")
    while True:
        print(get_prices(new_list))
        print("Press Ctrl+C to quit!")



def main():
    run_program=True
    while run_program:
        print("Choose an option: ")
        for i in range(len(options) + 1):
            print("{} - {}".format(i,options[i-1]))
        choice=int(input())

        if choice==1:
            while True:
                print(get_prices(symbols))
                print("Press Ctrl+C to quit!")
                sleep(5)                # sleep for 5 seconds
        elif choice==2:
            print(show_default(symbols))

        elif choice==3:
            add_to_default(symbols)

        elif choice==4:
            edit_default(symbols)

        elif choice==5:
            add_list()
        elif choice==6:
            run_program=False




if __name__ == "__main__":
    main()
