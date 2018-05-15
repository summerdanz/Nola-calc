import '../../css/index.css';
import {Card, CardActions, CardHeader, CardTitle, CardText, MenuItem,
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

export default class CurrentCharge extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      value: 0,
      radioValue: "No",
      yearValue: 0,
      monthValue: 0
    }
  }

  //form change/selection handling
  handleSelectChange = (event, index, value) => this.setState({value});
  handleRadioChange = event => {this.setState({ radioValue: event.target.value }) };
  handleYearsChange = event => {this.setState({ yearValue: event.target.value }) };
  handleMonthsChange = event => {this.setState({ monthValue: event.target.value }) };

  handleSubmit = () => {
    //data collected from form
    const data = {
      crimeSelected: this.state.value, //returns array # (0-x)
      isHabitualOffender: this.state.radioValue, //returns yes or no
      sentenceYear: this.state.yearValue, //returns number >=0
      sentenceMonth: this.state.monthValue //returns number 0<= x <=12
    }
    //sends data to backend
    const origin = window.location.origin;
    var url =  origin + '/currentcharge'
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
    let items = this.props.crimeList;
    items = items.map((x, i) => {
      return <MenuItem primaryText={x} value={i} key={i}/>
    })

    return(
        <Card style={style.cardStyle}>
          <CardText>
              <Row>
                <p><strong>Next, please tell us about the crime your client is charged with:</strong></p>
              </Row>
              <Row>
                <SelectField
                    value={this.state.value}
                    onChange={this.handleSelectChange}
                    maxHeight={500}
                    autoWidth={true}
                >
                {items}
              </SelectField>
            </Row>
            <Row>
                <p>Note: if your client is charged with a crime that is not listed, please select the option "a crime not included in this list" (at the bottom of the drop-down menu).</p>
            </Row>
            <Row>
              <p><strong>Will the individual be sentenced under the habitual offender statute?</strong></p>
            </Row>
            <Row>
              <RadioButtonGroup
                  name="habitualOffender"
                  defaultSelected="No"
                  onChange={this.handleRadioChange}
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
                <p><strong> What sentence will your client be given? Please enter the length of the sentence in years and/or months: </strong></p>
            </Row>
            <Row>
                <p>Example A:  For 7.5 years, enter 7 years and 6 months</p>
            </Row>
            <Row>
                <p>Example B: For 8 months, enter 0 years and 8 months</p>
            </Row>
            <Row>
              <TextField
                  id="years"
                  floatingLabelText="Years"
                  value={this.state.yearValue}
                  onChange={this.handleYearsChange}
                  type="number"
                  min={0}
                  style={style.textFieldStyle}
              />
              <TextField
                  id="months"
                  floatingLabelText="Months"
                  value={this.state.monthValue}
                  onChange={this.handleMonthsChange}
                  type="number"
                  min={0}
                  max={12}
                  style={style.textFieldStyle}
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
