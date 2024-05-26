#pragma once
using namespace std;
struct HARDWARE_ITEM {
    int record_num = 0;
    char tool_name[100];
    int quantity = 0;
    float cost = 0.0;
    bool is_active = 0;
};

void CreateEmptyDatabase(void);

void AddUpdateRecord();

void ListItems();