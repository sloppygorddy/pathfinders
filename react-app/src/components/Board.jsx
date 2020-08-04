import React, { Component } from "react";
import { Square } from "./Square";
import { Row, Container } from "react-bootstrap";
import Hang from "./Hang";

var cols = [];
var numcols = 30;
for (var j = 0; j < numcols; j++) {
  cols.push(
    <Row className="Rows">
      <Hang className="Rows" />
    </Row>
  );
}

export class Board extends Component {
  // renderSquare = (i) =>{
  //     return(
  //         <Square value = {i}/>
  //     );
  // }

  render() {
    return (
      <Container className="Board bg-dange col-11">
        {/* <Row>
          <Square value={0} />
          <Square value={1} />
          <Square value={2} />
          <Square value={3} />
        </Row>
        <Row>
          <Square value={4} />
          <Square value={5} />
          <Square value={6} />
          <Square value={7} />
        </Row>
        <Row>
          <Square value={8} />
          <Square value={9} />
          <Square value={10} />
          <Square value={11} />
        </Row> */}
        <tbody>{cols}</tbody>
      </Container>
    );
  }
}

export default Board;
