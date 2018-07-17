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

// Task 1
let dogName1 = "Steve";
let dogType1 = "beagle";

console.log(`I will walk ${dogName1} today at 12:00 pm.`)


let dogName2 = "Joe";
let dogType2 = "bulldog";

if(dogType2 === "corgi")
  console.log(`I will walk ${dogName2} today at 12:00 pm`)
else
  console.log(`I will walk ${dogName2} today at 1:00 pm`)


let dogName = "Lola";
let dogType = "poodle";

if(dogType === "corgi" || dogType === "beagle")
  console.log(`I will walk ${dogName} today at 12:00 pm`)
else if(dogType === "bulldog")
  console.log(`I will walk ${dogName} today at 1:00 pm`)
else
  console.log(`I will walk ${dogName} today at 2:00 pm`)


let fave = false
let time = null

dogType = dogType.toLowerCase()

if(dogType === "corgi" || dogType === "beagle")
  time = '12:00 pm'
else if(dogType === "bulldog")
  time = '1:00 pm'
else
  time = '2:00 pm'

FavNames = []
