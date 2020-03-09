/*
We will look at various types of scopes in javascript along with examples.
Scope -
    defined for a variable.
    it is the area in the code where the variable exists.
Why Scope -
    To limit access to the code.
Types of Scope -
    1. Global Scope
    2. Local Scope
1. Global scope -
    variables defined outside of function with var.
    They are available at the level and below where they are defined.
Example
*/
console.log(a);
var a = 'hello world';
console.log(a);
// We get the following output -
// undefined
// hello world

// if defined using let we will get error

// console.log(b); We get ReferenceError.
let b = 'foo';
console.log(b);

// Local scope - variables defined inside function. can't be accessed outside.
function Demo() {
    var f_var = "hi there";
    console.log(f_var);
}

Demo();
// console.log(f_var); We get ReferenceError

// However, inner functions can access outer function variables. Example

function f() {
    var foo = 10;

    function f1() {
        console.log(foo); // prints 10.
        foo = 20;
    }
    console.log('foo in parent', foo);
    f1();
    console.log('foo in parent after execution', foo);
}

f();

// context is different from scope. context refers to the value of this.
// generally the value of this is the window object except for classes and constructor functions.

console.log(this, 'top level this'); // prints {}
function f1() {
    console.log(this); // prints Object Global etc..
}

f1();

// let's see this in classes.

class DemoClass {
    constructor() {
        console.log(this, 'this in class'); // prints DemoClass {} this in class.
    }
}

d = new DemoClass();

// let's see using constructor functions.

function f2() {
    var f = this;
    console.log(this); // prints f2 {}. behaves like a class. class based functions.
}

ex = new f2();
console.log(ex.f, ex.this); // these two are undefined.

// Execution context - refers to the scope.
// each function execution pushes it's scope into the execution context stack and gets popped off when the function
// execution completes.

// concept of closures in js.
// the ability of inner function to remember outer function variables even when the function is returned.
// similar to proc binding in ruby.
// example

function create_multiplier(n) {
    return function multiply_by(v) {
        n += 1;
        return n * v;
    }
}

multiplier_of_2 = create_multiplier(2);
console.log(multiplier_of_2(9)); // prints 18.
console.assert(multiplier_of_2(14) === 28); // works!.


/*
Modules and IIFE.
Since there are no concept of public and private in js, we can use closures to create private vars and methods.
 */

function module() {
    let private_var = 5;
    function public_method() {
        console.log(private_var);
    }
    return public_method
}

public_method = module();
public_method.call(this);
console.log(public_method.private_var); // prints undefined.

/*
Lexical scopes -
Inner function has access to parent functions vars.
Works same as global scoping.

blocked scoping -
let and const have blocked scopes.
 */

/*
altering the scope using bind, call and apply.
call and apply invoke the function also.
 */

/*
Working of scopes.
1. creation of variable object.
2. creation of scope chain.
3. setting value of context(this).
 */