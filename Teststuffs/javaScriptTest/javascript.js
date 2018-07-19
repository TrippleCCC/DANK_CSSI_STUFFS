console.log('Hello World!');


const name = 'Charlie'
console.log(`Hello ${name}!`)

const age = 16
console.log(`You are ${age} years Old!`)

if(age >= 18)
{
  console.log("You are old enough to drive a car and vote.")
}
else if(age < 15)
{
  console.log('You are not old enough to drive or vote')
}
else
{
  console.log('You are old enough to drive a car but you are not old enough to vote.')
}






/*
const multiplyBy3 = (x) => x * 3

let n = 0
setInterval(() => {
  n += 1;
  console.log(n);
}, 1000)

*/
function eventHandler ()
{
  console.log("Hello World")
  likeButton.innerText = "Liked!"
}


let likeButton = document.querySelector('.likeButton')
//likeButton.addEventListener('click', )


document.addEventListener("DOMContentLoaded", () => {
  const floatingBox = document.querySelector(".floatingBox");
  let boxTop = 100;
  let boxLeft = 100;
  floatingBox.addEventListener("keydown", (event) => {
    const key = event.key;

    if(key === "ArrowDown")
    {
      boxTop += 5;
    }
    else if(key === "ArrowUp")
    {
      boxTop -= 5;
    }
    else if(key === "ArrowLeft")
    {
      boxLeft -= 5;
    }
    else if(key === "ArrowRight")
    {
      boxLeft += 5;
    }
    else
      return;

    floatingBox.style.top = boxTop + 'px';
    floatingBox.style.left = boxLeft + 'px';
    console.log(event);
  })
}) 

function makeGreetingMessage(name1,name2=null)
{
  if(name2 == null)
  {
    return `Hello ${name}`
  }

  return `Hello ${name1} and ${name2}`
}

function greet(name1="Billy", name2=null)
{
  if(name1[0] !== 'A')
    return
  console.log(makeGreetingMessage(name1,name2))
}
