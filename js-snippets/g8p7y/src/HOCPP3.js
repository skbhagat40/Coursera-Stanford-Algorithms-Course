import React, { useState } from "react";
// this for state abstraction

export function PP3(WrappedComponent) {
  return function (props) {
    const [name, setName] = useState("");
    const newProp = {
      name: {
        value: name,
        onChange: setName
      }
    };
    return <WrappedComponent {...newProp} />;
  };
}
