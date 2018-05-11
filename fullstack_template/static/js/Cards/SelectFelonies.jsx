import '../../css/index.css';
import {Card, CardActions, CardHeader, CardTitle, CardText, MenuItem, RadioButton, RadioButtonGroup, RaisedButton, TextField, SelectField} from 'material-ui';
import React from 'react';
import {Row, Col } from 'react-flexbox-grid';

export default class SelectFelonies extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      count: 0, //this will need to be updated via component will mount below from backend
      feloniesArray: [], //this will be populated by arr in componentWillMount
      value: 0
    }
  }

//gets count of felonies entered into previous page - also gets list of all options from backend
  componentWillMount(){
    let arr = [];
    for(let i = 0; i < this.props.previousCount; i++){
      arr.push(0)
    };
    console.log(arr);
    console.log(this.props.previousCount)
    this.setState({
      count: this.props.previousCount,
      feloniesArray: arr
    })
  }

  handleChange = (event) => {this.setState({ value: event.target.value })};

  //This fills feloniesArray with index of felony selected
  handleValue = (i, event, index, value) => {
    let values = this.state.feloniesArray;
    values.splice(i, 1, value);
    this.setState({ feloniesArray: values })
  };

  //submit button
  handleSubmit = () => {
    const data = {
      whichFelonies: feloniesArray //array of selected felonies from dropdown
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
    //mapping list of crimes into menu items for dropdown list
    let itemList = this.props.crimeList;
    itemList = itemList.map((x, i) => {
      return <MenuItem primaryText={x} value={i} key={i}/>
    })
    let selectFields = [];
    for(let i=0; i< this.state.count; i++){
      selectFields.push(
        <Row>
          <SelectField
              value={this.state.feloniesArray[i]}
              key={i}
              onChange={this.handleValue.bind(this, i)}
              maxHeight={500}
              autoWidth={true}
          >
          {itemList}
        </SelectField>
      </Row>
      );
    }
    return(
        <Card>
          <CardText>
            <Row>
              <p><strong>You indicated that your client has {this.state.count} prior felony convictions.</strong></p>
              <p>For each of your client's prior convictions, select the crime, below:
              When you are done, click Continue.</p>
            </Row>
              {selectFields}
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
