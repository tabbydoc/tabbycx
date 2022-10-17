import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Navigation from './Navigation';
import OutputTable from './OutputTable';
import MethodSelector from './MethodSelector';
import Progress from './Progress';
import ProcessButton from './ProcessButton';
import Badge from 'react-bootstrap/Badge'

import {Row, Col} from 'react-bootstrap'


import './../App.css';
import FileSelector from './FileSelector';

class TableClassifier extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            isFileUploaded: false,
            method: 0,
            isNotProcessButtonAvaliable: true
        }
    }

    handleUpload = (isNotAvaliable) => {
        this.setState({isNotProcessButtonAvaliable: isNotAvaliable})
        console.log(this.state.isNotProcessButtonAvaliable)
    }

    render() {
        return (    
            <Container>
                <Row>
                    <Navigation></Navigation>
                </Row>
                <br></br>
                <Row>
                    <FileSelector onUpload={this.handleUpload}>                        
                    </FileSelector>
                </Row>
                <Row>
                    <MethodSelector></MethodSelector>
                </Row>
                <ProcessButton 
                    isProcessButtonAvaliable = {this.state.isProcessButtonAvaliable}
                >                    
                </ProcessButton>
                <Row>
                    <Progress></Progress>
                </Row>      
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
}

export default TableClassifier;