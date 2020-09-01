import React from "react";
import "./styles.css";
import { PP } from "./HOCPP1";
import { PP2 } from "./HOCPP2";
import { render } from "react-dom";
import { PP3 } from "./HOCPP3";

function WrappedComponent({ age, name }) {
  return (
    <div>
      Age is {age}
      Name is {name}
    </div>
  );
}

class WrappedClass extends React.Component {
  render() {
    return <div>I am wrapped</div>;
  }
}

function WrappedControlled({ value, onChange }) {
  return <input type="text" value={value} onChange={onChange} />;
}

export default function App() {
  const Enhanced = PP(WrappedComponent);
  const Enhanced2 = PP2(WrappedClass);
  const Enhanced3 = PP3(WrappedControlled);
  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
      <Enhanced age={23} />
      <Enhanced2 />
      <Enhanced3 />
    </div>
  );
}
