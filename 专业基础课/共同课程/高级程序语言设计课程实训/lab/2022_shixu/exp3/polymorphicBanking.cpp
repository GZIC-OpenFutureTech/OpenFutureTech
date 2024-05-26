#include <iostream>
#include <iomanip>
#include <vector>
#include "Account.cpp"
#include "SavingAccount.cpp"
#include "CheckingAccount.cpp"
using namespace std;
int main()
{
    vector<Account*> accounts(4);

    // init 
    accounts[0] = new SavingsAccount(89, 0.06);
    accounts[1] = new CheckingAccount(190.0, 2.0);
    accounts[2] = new SavingsAccount(100.0, 0.015);
    accounts[3] = new CheckingAccount(300.0, 0.5);

    for (int i = 1; i <= accounts.size(); i++) {
        // output balance
        cout << "Account " << i << " balance: " << accounts[i]->getBalance() << '\n';

        // debit
        double withdrawalAmount = 0.0;
        cout << "Enter an amount to withdraw from Account " << i << ": ";
        cin >> withdrawalAmount;
        accounts[i]->debit(withdrawalAmount);

        // credit
        double depositAmount = 0.0;
        cout << "Enter an amount to deposit into Account " << i << ": ";
        cin >> depositAmount;
        accounts[i]->credit(depositAmount);

        // downcast pointer
        SavingsAccount* savingsAccountPtr = dynamic_cast<SavingsAccount*>(accounts[i]);

        // if it is a SavingsAccount, calculate and add interest
        if (savingsAccountPtr != 0) {
            double interestEarned = savingsAccountPtr->calculateInterest();
            cout << "Adding " << interestEarned << " interest to Account " << i << " (a SavingsAccount)" << '\n';
            savingsAccountPtr->credit(interestEarned);
        }

        // update and output new balance
        cout << "Updated Account " << i << " balance: " << accounts[i]->getBalance() << '\n';
    }
}
