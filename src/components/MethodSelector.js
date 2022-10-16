import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Form from 'react-bootstrap/Form'
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';

function MethodSelector() {
  return (
    <Form className="mb-3">
        <Form.Group className="mb-3">
            <Form.Label htmlFor="disabledTextInput">Choose method:</Form.Label>
            <Form.Select aria-label="Default select example">
            <option>Open this select menu</option>
            <option value="1">One</option>
            <option value="2">Two</option>
            <option value="3">Three</option>        
            </Form.Select>
        </Form.Group>
            <Button type="submit">Process</Button>
    </Form>
  );
}

export default MethodSelector;