#pragma once
class Account
{
public:
    Account(double);
    virtual void credit(double);
    virtual bool debit(double);
    void setBalance(double);
    double getBalance();

private:
    double balance;
};
class CheckingAccount : public Account
{
public:
    CheckingAccount(double, double);
    virtual void credit(double);
    virtual bool debit(double);

private:
    double transactionFee;
};
#include "Account.h"
class SavingsAccount : public Account
{
public:
    SavingsAccount(double, double);
    double calculateInterest();

private:
    double interestRate;
};