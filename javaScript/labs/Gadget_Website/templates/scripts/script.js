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

console.log('Running page script')

const title = document.querySelector('.title')
const images = document.querySelectorAll('img')
const img1 = images[0]
const img2 = images[1]
const img3 = images[2]

function changeTitleText(event){
  if(title.innerText == "One Wheel")
  {
    title.innerText = 'The All Terrain Skateboard'
  }
  else
  {
    title.innerText = 'One Wheel'
  }
}

function alterImage(event){
  if(event.type === 'mouseover')
    event.target.style.borderRadius = '100px'
  else
    event.target.style.borderRadius = '50px'
}

title.addEventListener('click', () => {changeTitleText()})
img2.addEventListener('mouseover', (event) =>{alterImage(event)}, false)
img2.addEventListener('mouseout', (event) =>{alterImage(event)})
img3.addEventListener('mouseover', (event) =>{alterImage(event)})
img3.addEventListener('mouseout', (event) =>{alterImage(event)})
