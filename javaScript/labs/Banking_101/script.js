// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customer_name;
let balance;
let logged_in = false
let password

function openAccount(name, deposit=0, new_password){
  // Set the value for customer_name equal to name below
  customer_name = name
  balance = deposit
  password = new_password
  logged_in = true
  return `${name} has opened a new account with a balance of $${balance}.`
}

function deposit(value=0){
  if(!logged_in)
    return "User must log in."
  balance += value
  return `${customer_name} has deposited $${value}. ${customer_name}'s total balance is $${balance}.`
}

function withdraw(value=0){
  if(!logged_in)
    return "User must log in."

  if(value > balance)
  {
    return `Sorry, ${customer_name}, you do not have enough money in your account. You need $${value-balance} more dollars.`

  }
  balance -= value
  return `${customer_name} has withdrawn $${value}. ${customer_name} has $${balance} remaining.`
}

function login(name, pass)
{
  if(name === customer_name && password === pass)
  {
    logged_in = true
    return `${name} has logged in.`
  }
  logged_in = false
  return 'Incorrect login'
}

function logout()
{
  logged_in = false
  return `${customer_name} has logged out.`
}

console.log(openAccount("Nonso", 300, "12345"))
console.log(deposit(50))
console.log(withdraw(500))
