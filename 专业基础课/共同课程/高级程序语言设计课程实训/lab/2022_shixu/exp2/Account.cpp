#include <iostream>
#include "Account.h"

Account::Account(double initial_balance) {
    if (initial_balance >= 0)
        balance = initial_balance;
    else {
        balance = 0.0;
        std::cout << "Initial balance cannot be negative." << std::endl;
    }
}
void Account::credit(double add_balance) {
    balance = balance + add_balance;
}S
bool Account::debit(double div_balance)
{
    if (div_balance > balance) {
        std::cout << "Debit amount exceeded account balance." << std::endl;
        return false;
    }
    else {
        balance = balance - div_balance;
        return true;
    }
}
double Account::getBalance() {
    return balance;
}

CheckingAccount::CheckingAccount(double initial_Balance, double fee) :Account(initial_Balance) {
    if (fee >= 0.0)	transaction_Fee = fee;
    else {
        transaction_Fee = 0.0;
        std::cout << "Warning: Transaction fee cannot be negative.It was set to 0.0." << std::endl;
    }
}
void CheckingAccount::checking_credit(double amount) {
    Account::credit(amount);
    Account::debit(transaction_Fee);
}
bool CheckingAccount::checking_debit(double amount)
{
    if (Account::debit(amount))
    {
        Account::debit(transaction_Fee);
        return true;
    }
    else
        return false;
}

SavingAccount::SavingAccount(double initial_Balance, double saving_rate) :Account(initial_Balance) {
    if (saving_rate >= 0.0) 
        interest_Rate = saving_rate;
    else {
        interest_Rate = 0.0;
        std::cout << "Interest rate cannot be negative." << std::endl;
    }
    interest_Rate = saving_rate;
}
double SavingAccount::calculateInterest() {
    return getBalance() * interest_Rate;
}
