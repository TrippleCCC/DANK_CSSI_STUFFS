#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code
import time

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance

    def __str__(self):
        print("Label: {label}\nBalance:{bal}".format(
            label = self.label, bal = self.balance))
        return "Label: {label}\nBalance:{bal}".format(
            label = self.label, bal = self.balance)
    def withdraw(self, amount):
        if(amount > self.balance):
            print("Sorry, you require $" + str(amount-self.balance) + " inorder to withdraw")
            return
        elif(amount < 0):
            print("Sorry, that is an invalid amount.")
        else:
            self.balance -= amount
            print("Transaction Sucessfull! You have ${bal} remaing in you account.".format(bal = self.balance))
            return

    def deposit(self, amount):
        if(amount < 0):
            print("Sorry, that is an invalid amount.")
            return
        else:
            self.balance += amount
            print("Transaction Successfull! You have ${bal} remaingin you account.".format(bal = self.balance))

    def rename(self, new_label):
        if(new_label == ""):
            print("Please provide a valid label.")
            return
        self.label = new_label
        print("Label Sucessfully changed!")
        return

    def transfer(self, dest_account, amount):
        if(amount < 0 or amount > self.balance):
            print("Sorry, invalid transfer.")
            return
        self.balance -= amount
        dest_account.deposit(amount)
        print("Transfer Sucessfull!")
        return

class Transaction(self):
    def __init__(self, time, type, amount, dest_account=None):
        self.time = time
        self.type = type
        self.amount = amount
        self.dest_account = dest_account
