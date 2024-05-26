#include "Account.h"
#include <iostream>
CheckingAccount::CheckingAccount(double initialBalance, double fee)
    : Account(initialBalance)
{
    if (fee >= 0.0)
        transactionFee = fee;
    else
    {
        transactionFee = 0.0;
        std::cout << "Warning: Transaction fee cannot be negative.It was set to 0.0." << std::endl;
    }
}
void CheckingAccount::credit(double amount)
{
    Account::credit(amount);
    Account::debit(transactionFee);
}
bool CheckingAccount::debit(double amount)
{
    if (Account::debit(amount))
    {
        Account::debit(transactionFee);
        return true;
    }
    else
        return false;
}