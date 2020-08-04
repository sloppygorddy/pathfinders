import React, { Component } from "react";
import { Navbar, Nav, Form, Button, FormControl, Image } from "react-bootstrap";

export class NavBar extends Component {
  render() {
    return (
      <Navbar className=" NavBar bg-primary" variant="dark" fixed="top">
        <Navbar.Brand href="#home">Pathfinder</Navbar.Brand>
        <Form className="ml-auto" inline>
          <FormControl type="text" placeholder="Search" className="mr-sm-2" />
          <Button className="form-button">Search</Button>
        </Form>
        <Nav className="ml-auto">
          <Nav.Link href="#username">UserName</Nav.Link>
          <Nav.Link href="#picture">
            <Image
              className="float-right"
              style={{ width: 30, height: "auto" }}
              src="https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80"
              roundedCircle
            />
          </Nav.Link>
        </Nav>
      </Navbar>
    );
  }
}

export default NavBar;
