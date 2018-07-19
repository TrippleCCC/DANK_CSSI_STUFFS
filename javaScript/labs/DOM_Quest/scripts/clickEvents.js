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

console.log("Running Click Events Script");

const box1 = document.querySelector("#box1")
const box2 = document.querySelector("#box2")
const box3 = document.querySelector("#box3")

function changeColor(event){
  if(event.target.id === "box1")
  {
    box2.style.color = box1.style.color
    box3.style.color = box1.style.color
  }
  else if(event.target.id === "box2")
  {
    box1.style.color = box2.style.color
    box3.style.color = box2.style.color
  }
  else if(event.target.id === "box3")
  {
    box1.style.color = box3.style.color
    box2.style.color = box3.style.color
  }
}

box1.addEventListener('click', function(){changeColor(event)})
box2.addEventListener('click', changeColor)
box3.addEventListener('click', changeColor)
