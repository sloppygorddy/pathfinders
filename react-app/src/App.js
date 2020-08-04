import React from "react";
import "./App.css";
import { Board } from "./components/Board";
import { Container, Row, Col } from "react-bootstrap";
import NavBar from "./components/NavBar";

function App() {
  return (
    <Container fluid className="bg-succes">
      <Row>
        <Col>
          <NavBar />
        </Col>
      </Row>
      <Row className="placeholder">
        <Col>
          <h1>placeholder</h1>
        </Col>
      </Row>
      <Row>
        <Col>
          <Board />
        </Col>
      </Row>
    </Container>
  );
}

export default App;
