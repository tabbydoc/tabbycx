import React from 'react';
import Table from 'react-bootstrap/Table';

class OutputTable extends React.Component {
  render(){
    return (
      <Table striped bordered hover >
        <thead>
          <tr>
            <th className='bg-success'>First Name</th>
            <th className='bg-success'>Last Name</th>
            <th className='bg-success'>Username</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className='bg-primary'>Mark</td>
            <td className='bg-primary'>Otto</td>
            <td className='bg-primary'>@mdo</td>
          </tr>
          <tr>
            <td className='bg-primary'>Jacob</td>
            <td className='bg-primary'>Thornton</td>
            <td className='bg-primary'>@fat</td>
          </tr>
          <tr>
            <td className='bg-primary'>Larry the Bird</td>
            <td className='bg-primary'>Harry</td>
            <td className='bg-primary'>@twitter</td>
          </tr>
        </tbody>
      </Table>
    );
  }
}

export default OutputTable;