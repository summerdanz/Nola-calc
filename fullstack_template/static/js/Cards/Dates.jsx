import '../../css/index.css';
import {Card, CardActions, CardHeader, CardTitle, CardText, DatePicker, MenuItem,
  RadioButton, RadioButtonGroup, RaisedButton, SelectField, TextField } from 'material-ui';
import React from 'react';
import {Row, Col } from 'react-flexbox-grid';


const style = {
  cardStyle: {
    margin: 20
  },
  textFieldStyle: {
    marginRight: 20
  }
};

export default class Dates extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      arrestDate: null,
      releaseValue: false,
      releaseDate: null,
      convictDate: null
    }
  }

  //form change/selection handling
  handleArrestDate = (event, date) => {this.setState({arrestDate: date})}
  handleReleaseChange = event => {this.setState({ releaseValue: event.target.value }) };
  handleReleaseDate = (event, date) => {this.setState({ releaseDate: date }) };
  handleConvictDate = (event, date) => {this.setState({ convictDate: date }) };

  handleSubmit = () => {
    //data collected from form
    const data = {
      arrestDate: this.state.arrestDate,
      releaseValue: this.state.releaseValue,
      releaseDate: this.state.releaseDate,
      convictDate: this.state.convictDate
    }
    //sends data to backend
    const origin = window.location.origin;
    var url =  origin + '/dates'
     $.ajax({
       url: url,
       dataType: 'json',
       type: 'POST',
       data: JSON.stringify(data),
       contentType: 'application/json; charset=utf-8',
       success: function(response){
         this.props.next()
       }.bind(this),
       error: function(xhr, status, err){
         console.log(err);
       }.bind(this)
     });
  }

  render () {

    return(
        <Card style={style.cardStyle}>
          <CardText>
              <Row>
                <p><strong>Further, please answer these questions that help us calculate how much time your client has spent in custody so far:</strong></p>
              </Row>
              <Row>
                <p><strong>When was your client arrested?</strong></p>
                <DatePicker
                  hintText='Click to enter date'
                  openToYearSelection={true}
                  value= {this.state.arrestDate}
                  onChange={this.handleArrestDate}
                  />
            </Row>
            <Row>
              <p><strong>Has your client been released after being arrested, either on bail or on his or her own recognizance?</strong></p>
            </Row>
            <Row>
              <RadioButtonGroup
                  name="released"
                  defaultSelected="false"
                  onChange={this.handleReleaseChange}
                  >
                  <RadioButton
                    value="true"
                    label="Yes"
                  />
                  <RadioButton
                    value="false"
                    label="No"
                  />
                </RadioButtonGroup>
            </Row>
            <Row>
              <p><strong>What was the date at which your client was released from pre-trial detention?</strong></p>
              <DatePicker
                hintText='Click to enter date'
                openToYearSelection={true}
                value= {this.state.releaseDate}
                onChange={this.handleReleaseDate}
                />
          </Row>
          <Row>
            <p>(Note: If your client was arrested but not released again before the date at which he or she will be convicted, please enter the date at which your client will be convicted as the date of release after the arrest in question.)</p>
          </Row>
          <Row>
            <p><strong>When will your client be convicted?</strong></p>
            <DatePicker
              hintText='Click to enter date'
              openToYearSelection={true}
              value= {this.state.convictDate}
              onChange={this.handleConvictDate}
              />
          </Row>
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
