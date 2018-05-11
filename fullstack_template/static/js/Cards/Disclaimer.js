import '../../css/index.css';
import axios from 'axios';
import {Card, CardActions, CardHeader, CardTitle, CardText, Checkbox, RaisedButton} from 'material-ui';
import React from 'react';

export default class Disclaimer extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      checked: false,
    }
  }
  updateCheck = () => {
    this.setState({
      checked: !this.state.checked
    })
  }
  handleSubmit = () => {
    const data = {
      isDisclaimerChecked: this.state.checked //returns true or false
    }
    const origin = window.location.origin;
    var url =  origin + '/disclaimer'
   $.ajax({
     url: url,
     dataType: 'json',
     type: 'POST',
     data: JSON.stringify(data),
     contentType: 'application/json; charset=utf-8',
     success: function(){
       this.props.next()
     }.bind(this),
     error: function(xhr, status, err){
       console.log(err);
     }.bind(this)
   });
  }

  render () {
    const data = {
      disclaimerChecked: this.state.checked
    }
    return(
        <Card>
          <CardHeader
            title="Disclaimer"
          />
          <CardText>
              <p>Important: Please note that this application does not provide legal services or legal advice.
              Your use of this application does not form an attorney-client relationship with any party.</p>
              <Checkbox
                  label="I understand and accept the terms above."
                  checked={this.state.checked}
                  onCheck={this.updateCheck}
              />
          </CardText>
          <CardActions>
            <RaisedButton
              label="Back"
              onClick={this.props.previous}
            />
            <RaisedButton
              label="Continue"
              primary={true}
              onClick={this.handleSubmit}
              disabled={!this.state.checked}
            />
          </CardActions>
        </Card>
    )
  }
}
