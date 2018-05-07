import '../../css/index.css';
import {Card, CardActions, CardHeader, CardTitle, CardText, MenuItem, RadioButton, RadioButtonGroup, RaisedButton, TextField, SelectField} from 'material-ui';
import React from 'react';
import {Row, Col } from 'react-flexbox-grid';

export default class SelectFelonies extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      count: 2, //this will need to be updated via component will mount below from backend
      feloniesArray: [0, 0], //will need to populate this with # of 0's depending on count
      value: 0
    }
  }

//SUMMER - need to uncomment this and link to backend to grab number of felonies entered in PreviousFelonies.jsx
  // componentWillMount(){
  //   //gets list of all crimes from backend
  //   fetch('http://localhost:5000/?????', { //will need to put the route you need here - send count from PreviousFelonies.jsx
  //     method: 'GET',
  //     mode:'no-cors',
  //     dataType: 'json'
  //   })
  //     .then(r => r.json())
  //     .then(r => {
  //       this.setState({
  //         count: r
  //       })
  //     })
  //     .catch(err => console.log(err))
  // }

  //form controls
  handleChange = event => {this.setState({ value: event.target.value })};

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
    //send data to flask here


    //handles change to next question - this will need to be asynchronous once backend post completes
    this.props.next();
  }

  render () {
    //mapping list of crimes into menu items for dropdown list
    let itemList = this.props.crimeList;
    itemList = itemList.map((x, i) => {
      return <MenuItem primaryText={x.text} value={i} key={i}/>
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
