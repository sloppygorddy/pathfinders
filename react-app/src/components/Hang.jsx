import React, { Component } from "react";
import Square from "./Square";

var rows = [];
var numrows = 60;
for (var i = 0; i < numrows; i++) {
  rows.push(<Square />);
}

export class Hang extends Component {
  render() {
    return <tbody>{rows}</tbody>;
  }
}

export default Hang;
