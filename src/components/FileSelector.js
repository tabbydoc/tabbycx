import { render } from '@testing-library/react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import React, { useState } from 'react';


class FileSelector extends React.Component {

    render(){
        return (
            <Form.Group controlId="formFile" className="mb-3">
                <Form.Label>Choose file to table classification (*.html):</Form.Label>
                <Form.Control type="file" onChange={(e) => this.props.onUpload(false, e.target.files[0].name, e)}/>
            </Form.Group>
        )
    }
} 

export default FileSelector;