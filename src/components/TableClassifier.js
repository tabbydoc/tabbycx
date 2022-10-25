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
            isNotProcessButtonAvaliable: true,
            fileName: ""
        }
    }

    handleUpload = (isNotAvaliable, fName, event) => {
        this.setState({isNotProcessButtonAvaliable: isNotAvaliable})
        this.setState({fileName: fName})
        event.preventDefault();
        const data = new FormData();
        data.append('file', 
                        event.target.files[0],
                        this.state.fileName);
        fetch("http://127.0.0.1:8000/uploadfile", {
             method: 'POST',
             headers: {
                 'Accept': 'application/json',
             },
             body: data
        }).then((response) =>  {
           return response.text();
        })
    }

    handleSelectMethod = (m) => {
        this.setState({method: m})
    }

    render() {
        return (    
            <Container>
                <Row>
                    <Navigation></Navigation>
                </Row>
                <br>
                </br>
                <Row>
                    <MethodSelector
                        onChangeMethod = {this.handleSelectMethod}
                    >
                    </MethodSelector>
                </Row>
                <Row>
                    <FileSelector onUpload={this.handleUpload}>                        
                    </FileSelector>
                </Row>
                {/*<ProcessButton 
                    isProcessButtonAvaliable = {this.state.isNotProcessButtonAvaliable}
                >                    
                </ProcessButton>
                <br>
                </br>
                <br>
                </br>
                <Row>
                    <Progress></Progress>
                </Row> */}     
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