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
document.addEventListener('DOMContentLoaded', () => {
  // Use querySelector to store the div in a variable.
  let redButton = document.querySelector('#red');
  let greenButton = document.querySelector('#green');
  let blueButton = document.querySelector('#blue');
  let box = document.querySelector('#responseBox');
  let text = document.querySelector('#responceBoxText')
  let clearButton = document.querySelector('#clear')

  // Use addEventListener to respond to a click event.
  redButton.addEventListener('click', e => {
    console.log("You clicked the red button!");
    box.style.backgroundColor = 'red'
    text.innerText += " Red"
  })

  function logText(string)
  {
    console.log(string);
    return
  }

  function clearedF()
  {
    text.style.color = 'black'
    text.innerText = "Cleared!"
  }

  greenButton.addEventListener('click', e => {
    console.log("You clicked the green button!");
    box.style.backgroundColor = 'green'
    text.innerText += " Green"
  })

  blueButton.addEventListener('click', e => {
    console.log("You clicked the blue button!");
    box.style.backgroundColor = 'blue'
    text.innerText += " Blue"
  })

  clearButton.addEventListener('click', e => {
    text.innerText = ""
    box.style.backgroundColor = null
    clearedF()
    setInterval(donothing, 4000)
    text.innerText = ""

  })
})
