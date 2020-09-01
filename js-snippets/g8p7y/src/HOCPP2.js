import React from "react";

// Also this uses some properties of closures.
// To demonstrate refs using HOCs for functional
// components.
export function PP2(WrappedComponent) {
  return function (props) {
    const refh = (el) => console.log("i am reff", el);
    return <WrappedComponent ref={refh} />;
  };
}
