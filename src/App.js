import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Navigation from './components/Navigation';
import OutputTable from './components/OutputTable';
import MethodSelector from './components/MethodSelector';
import Progress from './components/Progress';
import Badge from 'react-bootstrap/Badge'

import {Row, Col} from 'react-bootstrap'


import './App.css';
import FileSelector from './components/FileSelector';

function App(props) {
  return (    
    <Container>
      <Row>
        <Navigation></Navigation>
      </Row>
      <br></br>
      <Row>
        <FileSelector></FileSelector>
      </Row>
      <Row>
        <MethodSelector></MethodSelector>
      </Row>
      <Row><Progress></Progress></Row>      
      <Row>
        <OutputTable></OutputTable>
      </Row>
      <Row>
        <div>
          <Badge bg="primary">Data</Badge>{' '}
          <Badge bg="success">Metadata</Badge>{' '}
        </div>
      </Row>
    </Container>
  );
}

export default App;