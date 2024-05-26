#include <iostream>
#include <cstring>
#include <iomanip>
#include "hardware.h"
using namespace std;
HARDWARE_ITEM records[99];
int main() {
    FILE* dbfile = fopen("hardware.dat", "rb");
    if (!dbfile) {
        CreateEmptyDatabase();
    }
    else {
        fread(&records, sizeof(HARDWARE_ITEM), 100, dbfile);
        fclose(dbfile);
    }
    int option = 0;
    while (1) {
        cout << "\nEnter Request\n";
        cout << "1 - Input new tool or update an existing tool\n" << "2 - Delete a tool\n" << "3 - List all tools\n" << "4 - Exit\n" << "? ";
        cin >> option;
        int rec_num;
        switch (option) {

        case 1: //	Input new tool or update an existing tool
            cout << "Enter record number ( 1 to 100, 0 to return to main menu ): " << '\n' << "? ";
            cin >> rec_num;
            if (rec_num < 0 || rec_num > 100)
            {
                cout << "Invalid record number:" << '\n';
                break;
            }
            cout << "Enter tool name: " << '\n' << "? ";
            scanf(" %[^\n]s", records[rec_num - 1].tool_name);
            cout << "Enter quantity: " << '\n' << "? ";
            scanf("%d", &records[rec_num - 1].quantity);
            cout << "Enter cost: " << '\n' << "? ";
            scanf("%f", &records[rec_num - 1].cost);

            records[rec_num - 1].is_active = 1;
            AddUpdateRecord();
            break;

        case 2: 
            cout << "Enter record number ( 1 to 100, 0 to return to main menu ):" << '\n' << "? ";
            cin >> rec_num;
            if (rec_num < 0 || rec_num > 100) {
                cout << "Invalid record number" << '\n';
                break;
            }
            strcpy(records[rec_num - 1].tool_name, "");
            records[rec_num - 1].quantity = 0;
            records[rec_num - 1].cost = 0;
            records[rec_num - 1].is_active = 0;
            AddUpdateRecord();
            break;

        case 3: 
            ListItems();
            break;

        case 4: 
            return 0;
            break;
        }
    }

    return 0;
}