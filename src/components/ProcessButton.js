import Button from 'react-bootstrap/Button';
import React, { useState } from 'react';

class ProcessButton extends React.Component {
    render(){
        return(
            <Button 
                type="submit" 
                disabled={this.props.isProcessButtonAvaliable}
            >
                Process
            </Button>
        )
    }
}

export default ProcessButton;