import React from "react";

export function PP(WrappedComponent) {
  return function (props) {
    const newProps = { name: "Shailesh" };
    return (
      <div>
        I am a wrapper
        <WrappedComponent {...props} {...newProps} />;
      </div>
    );
  };
}
