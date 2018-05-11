import '../../css/index.css';
import {Card, CardActions, CardHeader, CardTitle, CardText, MenuItem, RadioButton, RadioButtonGroup, RaisedButton, TextField, SelectField} from 'material-ui';
import React from 'react';
import {Row, Col } from 'react-flexbox-grid';

export default class PreviousFelonies extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      value: false,
      count: 0
    }
  }

  //form controls
  handleChange = event => {this.setState({ value: event.target.value })};
  handleCountChange = event => {this.setState({ count: event.target.value })};

  //submit button
  handleSubmit = () => {
    const data = {
      convictedBefore: this.state.value, //returns true or false
      convictionCount: this.state.count //returns number
    }
    //send data to flask here
    const origin = window.location.origin;
    var url =  origin + '/PreviousFelonies'
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
    //mapping list of crimes into menu items for dropdown list
    let itemList = this.props.crimeList;
    itemList = itemList.map((x, i) => {
      return <MenuItem primaryText={x.text} value={i} key={i}/>
    })
    return(
        <Card>
          <CardText>
            <Row>
              <p>Has your client been convicted before of other felonies?</p>
            </Row>
            <Row>
              <RadioButtonGroup
                name=""
                defaultSelected="No"
                onChange={this.handleChange}
                >
                <RadioButton
                  value="Yes"
                  label="Yes"
                />
                <RadioButton
                  value="No"
                  label="No"
                />
              </RadioButtonGroup>
            </Row>
            <Row>
                <p> How many prior felony convictions does your client have?</p>
            </Row>
            <Row>
              <TextField
                  id="priors"
                  value={this.state.count}
                  onChange={this.handleCountChange}
                  type="number"
                  min={0}
              />
          </Row>
          <Row>
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
