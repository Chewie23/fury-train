#!/usr/bin/env python
# -*- coding: utf-8 -*

import sqlite3 as lite
import datetime
import collections #OrderedDict()
import prettytable
import sys #sys.exit()

#TODO
#Clean up comments
#   Make a notes.txt for my own benefit
#   And leave the pertinent comments in the code
#Let the code cool and edit it as necessary
#Unit Testing will NOT be helpful here, as unfortunate as that sounds

class Budget_App(object):
    def __init__(self):
        self.months = collections.OrderedDict([
        ("jan", "01"), ("feb", "02"), ("mar", "03"), 
        ("apr", "04"), ("may", "05"), ("jun", "06"),  
        ("jul", "07"), ("aug", "08"), ("sep", "09"),
        ("oct", "10"), ("nov", "11"), ("dec", "12")
        ])
        self.db_file = 'test.db'
        self.table   = "Date_Table"

    def db_connection(self):
        return lite.connect(self.db_file)

    def print_table(self, cur, table):
        #Tutorial found here: http://gothos.info/2013/02/creating-reports-with-sqlite-python-and-prettytable-2/
        #Keeping this very general!
        #Grabbing the EVERYTHING (created when table was made)
        #Format string, via python!
        cur.execute('SELECT * FROM {}'.format(table))

        #Grabbing column names and putting them in a list
        col_names = [cn[0] for cn in cur.description]

        #Getting all the delicious row data and putting them in a list
        rows = cur.fetchall()

        tabl = prettytable.PrettyTable(col_names)
        tabl.align[col_names[1]] = "l" #That is an "L"
        tabl.align[col_names[2]] = "r"
        #More info here: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
        #Just Ctrl+F "align"

        tabl.padding_width = 1
        for row in rows:
            tabl.add_row(row)

        print (tabl)


    def delete_row(self, cur, table):
        warning = """************WARNING************
Are you sure you want to delete a row? It is permanent!
(Default choice is N)
Y/N > """
        usr_input = raw_input(warning)
        choices = ["y", "Y", "Yes", "yes"]
        while usr_input in choices:
            prompt = """Please enter the ID of the row: """
            try:
                self.ID = int(raw_input(prompt))
            except ValueError:
                print "Please enter a valid ID! Printing table..."
                self.print_table(cur, table)
            else:
                cur.execute("DELETE FROM {} WHERE id=?".format(table), (self.ID,))
                usr_input = "N"

    def get_item_desc(self):
        prompt = """Please enter a three word item description: """
        while 1:
            item_desc = raw_input(prompt)
            if len(item_desc.split()) > 3:
                print "The item description is too long!"
            elif len(item_desc.split()) == 0: 
                print "Please enter an item description!"
            else:
                return item_desc

    def get_price(self):
        prompt = """Please enter price of item: """
        while 1:
            try:
                item_price = float(raw_input(prompt))
            except ValueError:
                print "That isn't a valid price!"
            else:
                return item_price

    def get_item_n_price(self):
        item_n_price = [self.get_item_desc(), self.get_price()]
        return item_n_price

    def insert_new_value(self, cur, table, item_desc, val):
        #Cannot use placeholders (the "?" symbol) with table or column names
        #CAN do string formatting: 
        #http://stackoverflow.com/questions/8841488/pysqlite-placeholder-substitution-for-column-or-table-names

        #Getting column names!
        cur.execute('SELECT * FROM {}'.format(table))
        col_names = [cn[0] for cn in cur.description]

        #Oh man. Okay. So this is string formatting to the extreme
        #Basically going through the col_names list and NOT including col_names[0]
        #Which is "id", which will auto-increment!
        cur.execute(
                "INSERT INTO {}({}, {}, {}) VALUES(?, ?, ?)".format
                (table, col_names[1], col_names[2], col_names[3]),
                (str(datetime.date.today()), item_desc, val)
                )

    def usr_month(self):
        prompt = """Please enter month you wish to see
(Use the three letter abbreviation. Ex. Jan, Mar, Jul)
> """
        return raw_input(prompt)

    def print_specific_monthly_sum(self, cur, table):
        month_sum = self.get_specific_month_sum(cur, table)
        print "Month: {}  Sum: ${}".format(month_sum[0], month_sum[1])

    def get_specific_month_sum(self, cur, table):
        expense_sum = 0

        #Should I put "Date" and "Expense" in variables?
        cur.execute("SELECT {}, {} FROM {}".format("Date", "Expense", table))

        #Will grab all rows
        rows = cur.fetchall()

        usr_month = self.usr_month().lower()

        for n in rows:
            #Kind of clunky, but works
            #Indexing tuple string to find month
            if (n[0][5] + n[0][6] == self.months[usr_month]):
                expense_sum += n[1]

        return [self.months[usr_month], expense_sum]

    def get_all_months(self, cur, table):
        expense = collections.OrderedDict()
        cur.execute("SELECT {}, {} FROM {}".format("Date", "Expense", table))

        #Will grab all rows
        rows = cur.fetchall()

        for n in rows:
            for key in self.months:
                if (n[0][5] + n[0][6] == self.months[key]):
                    if self.months[key] in expense:
                        expense[self.months[key]] += n[1]
                    else:
                        expense[self.months[key]] = n[1]
        for key in expense:
            print "Month: {}  Sum: ${}".format(key, expense[key])



    def create_table(self, cur, table):
        cur.execute(
            "CREATE TABLE IF NOT EXISTS {}"
            "(id INTEGER PRIMARY KEY AUTOINCREMENT, Date TEXT, Purchased TEXT, Expense FLOAT)"
            .format(table)
            )

    def main_menu(self):
        prompt = """
Please enter the selection number or press Q to quit
1. Print Table
2. Add Entry
3. Delete Entry
4. Get Monthly Sum
>  """
        with self.db_connection() as conn:
            self.cur = conn.cursor()
            self.create_table(self.cur, self.table)
            while 1:
                usr_input = raw_input(prompt)
                choices = ["1", "2", "3", "4", "q", "Q"]
                if usr_input not in choices:
                    print "Please enter a valid selection"
                    continue
                elif usr_input == "q" or usr_input == "Q":
                    print "Goodbye!"
                    sys.exit()
                elif usr_input == "1":
                    self.print_table(self.cur, self.table)
                elif usr_input == "2":
                    self.item_n_price = self.get_item_n_price()
                    self.insert_new_value(self.cur, self.table,
                            self.item_n_price[0], self.item_n_price[1])
                elif usr_input == "3":
                    self.delete_row(self.cur, self.table)
                elif usr_input == "4":
                    month_choice = """Do you want to see a specific month or
all the months?
S/A > """
                    usr_in = raw_input(month_choice)
                    if usr_in[:1].lower() == "s":
                        self.print_specific_monthly_sum(self.cur, self.table)
                    elif usr_in[:1].lower() == "a":
                        self.get_all_months(self.cur, self.table)
                conn.commit() #Needed to commit changes!


budget = Budget_App()
budget.main_menu()
