#include <iostream>
#include "Account.h"


int main()
{
    // init account
    Account account1(50.0);

    // test account
    // normal test
    account1.credit(25.0);
    std::cout << "account1 balance: $" << account1.getBalance() << std::endl;

    // bound test 
    // out of bound
    std::cout << "Out of bound test" << std::endl;
    // in the bound
    account1.credit(26.0);
    std::cout << "In bound test" << std::endl;

    account1.credit(25.0);
    // error test
    account1.debit(100.0);
    std::cout << "account1 balance: $" << account1.getBalance() << std::endl;

    // init savings account


    SavingsAccount account2(25.0, 0.1);
    // test savings account
    account2.credit(25.0);
    std::cout << "account2 balance: $" << account2.getBalance() << std::endl;
    // error test
    std::cout << "account2 interest: $" << account2.calculateInterest() << std::endl;
    account2.credit(account2.calculateInterest());
    std::cout << "account2 balance: $" << account2.getBalance() << std::endl;


    // init checking account
    CheckingAccount account3(110.0, 1.0);
    // test checking account
    account3.credit(25.0);
    std::cout << "account3 balance: $" << account3.getBalance() << std::endl;
    // error test
    std::cout << "error test" << std::endl;
    std::cout << account3.debit(110.0) << std::endl;
    // bound test
    std::cout << "bound test" << std::endl;
    std::cout << account3.debit(109.0) << std::endl;
    std::cout << "account3 balance: $" << account3.getBalance() << std::endl;
    return 0;
}