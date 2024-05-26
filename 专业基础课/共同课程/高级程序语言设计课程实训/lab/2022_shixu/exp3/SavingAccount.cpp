#include "Account.h"
#include <iostream>
SavingsAccount::SavingsAccount(double initialBalance, double rate)
    : Account(initialBalance)
{
    if (rate >= 0.0)
        interestRate = rate;
    else
    {
        interestRate = 0.0;
        std::cout << "Warning: Interest rate cannot be negative.It was set to 0.0." << std::endl;
    }
    interestRate = rate;
}
double SavingsAccount::calculateInterest()
{
    return getBalance() * interestRate;
}