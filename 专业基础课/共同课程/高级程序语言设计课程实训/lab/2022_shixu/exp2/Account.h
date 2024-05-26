#pragma once

//general account
class Account{
    public:
        Account(double);
        void credit(double);
        bool debit(double);
        double getBalance();

    private:
        double balance;
};

//checking account
class CheckingAccount : public Account{
    public:
        CheckingAccount(double, double);
        void checking_credit(double);
        bool checking_debit(double);

    private:
        double transaction_Fee;
};

//saving account
class SavingAccount : public Account{
    public:
        SavingAccount(double, double);
        double calculateInterest();

    private:
        double interest_Rate;
};
