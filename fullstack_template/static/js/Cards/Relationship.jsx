import '../../css/index.css';
import {Card, CardActions, CardHeader, CardTitle, CardText, RadioButton, RadioButtonGroup, RaisedButton} from 'material-ui';
import React from 'react';

export default class Relationship extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      value: 'relative',
    }
  }
  handleChange = event => {
    this.setState({ value: event.target.value });
  };
  handleSubmit = () => {
    const data = {
      relation: this.state.value
    }
    //send data to flask here


    //handles change to next question - this will need to be asynchronous once backend post completes
    this.props.next();
  }
  render () {
    return(
        <Card>
          <CardText>
              <p>To start, please tell us why you are using this application:</p>
              <RadioButtonGroup
                name="q1"
                defaultSelected="relative"
                onChange={this.handleChange}
                >
                <RadioButton
                  value="relative"
                  label="I am a relative, partner or friend of an individual currently in prison."
                />
                <RadioButton
                  value="attorney"
                  label="I am an attorney assisting a client who has not yet been convicted."
                />
              </RadioButtonGroup>
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
            />
          </CardActions>
        </Card>
    )
  }
}
