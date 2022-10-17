import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Form from 'react-bootstrap/Form'
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import React, { useState } from 'react';

class MethodSelector extends React.Component {
  render() {
    return (
      <Form className="mb-3">
          <Form.Group className="mb-3">
              <Form.Label htmlFor="disabledTextInput">Choose method:</Form.Label>
              <Form.Select 
                aria-label="Default select example"
                onChange={(e) => this.props.onChangeMethod(e.target.value)}
              >
              <option>Open this select menu</option>
              <option value="1">Yoshida</option>
              <option value="2">Jung</option>
              <option value="3">Embley</option> 
              <option value="4">Nishida</option>
              <option value="5">Our method</option>
              </Form.Select>
          </Form.Group>
      </Form>
    );
  }
}

export default MethodSelector;