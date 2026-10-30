// variable scope
var globalVar = "I am a global variable";

function myFunction() {
    var localVar = "I am a local variable";
    console.log(globalVar); // Accessible
    console.log(localVar);  // Accessible
}

myFunction();

console.log(globalVar); // Accessible
// console.log(localVar); // Uncaught ReferenceError: localVar is not defined

// code block scope
if (true) {
    let blockVar = "I am a block-scoped variable";
    console.log(blockVar); // Accessible
}

console.log(blockVar); // Uncaught ReferenceError: blockVar is not defined