import Form from 'react-bootstrap/Form';

function FileSelector() {
    return (
        <Form.Group controlId="formFile" className="mb-3">
            <Form.Label>Choose file to table classification (*.html):</Form.Label>
            <Form.Control type="file" />
        </Form.Group>
    )
} 

export default FileSelector;