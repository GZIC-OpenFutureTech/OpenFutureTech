#include <iostream>
#include "Account.h"
using namespace std;

int main()
{
    // create account
    cout << "set account1 100$" << endl;
    Account account1(100.0);
    cout << "finish" << endl;
    // account creadit test
    cout << "add 150$" << endl;
    account1.credit(150.0);
    cout << "account1 balance is: $" << account1.getBalance() << endl;
    // bound test 
    cout << "Out of bound test:" << endl;
    // in the bound
    cout << "debit 300$" << endl;
    account1.debit(300.0);
    cout << "account1 balance is: $" << account1.getBalance() << endl;
    cout << "In bound test" << endl;
    account1.credit(500.0);
    cout << "account1 balance: $" << account1.getBalance() << endl;
    // init saving account
    cout << "saving account test,create account2 with 125$ and 0.1 rate" << endl;
    SavingAccount account2(125.0, 0.1);
    cout << "credit 25$" << endl;
    account2.credit(25.0);
    cout << "account2 balance: $" << account2.getBalance() << endl;
    cout << "account2 interest: $" << account2.calculateInterest() <<endl;
    account2.credit(account2.calculateInterest());
    cout << "account2 balance: $" << account2.getBalance() << endl;
    // init checking account
    cout << "checking account test, create account3 with 200$ fee 5$" << endl;
    CheckingAccount account3(200.0, 5.0);
    // test checking account
    cout << "credit 100$" << endl;
    account3.checking_credit(100.0);
    cout << "account3 balance: $" << account3.getBalance() << endl;
    // error test
    cout << "error test, debit 400$" << endl;
    cout << account3.checking_debit(400.0) <<endl;
    cout << "account3 balance: $" << account3.getBalance() << endl;
    //test fee
    cout << "test fee, credit 100$ and then debit 20$" << endl;
    account3.checking_credit(100);
    account3.checking_debit(20);
    cout << "account3 balance: $" << account3.getBalance() << endl;
    return 0;
}