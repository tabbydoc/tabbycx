import Spinner from 'react-bootstrap/Spinner';
import Form from 'react-bootstrap/Form'

function Progress() {
  return (
    <Form className="mb-3">
    <Spinner animation="border" role="status">
      <span className="visually-hidden">Loading...</span>
    </Spinner>
    </Form>
  );
}

export default Progress;