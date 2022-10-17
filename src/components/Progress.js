import Spinner from 'react-bootstrap/Spinner';
import Form from 'react-bootstrap/Form'
import React from 'react';

class Progress extends React.Component {
  render(){
    return (
      <Form className="mb-3">
      <Spinner animation="border" role="status">
        <span className="visually-hidden">Loading...</span>
      </Spinner>
      </Form>
    );
  }
}

export default Progress;