import AppBarTop from './AppBar';
import {Card, CardActions, CardHeader, CardTitle, CardText, Checkbox, LinearProgress, Paper, RaisedButton} from 'material-ui';
import React from 'react';
import {Grid, Row, Col } from 'react-flexbox-grid';
import {grey300} from 'material-ui/styles/colors';

//each "form" page is separated into different components
import Welcome from './Cards/Welcome';
import Disclaimer from './Cards/Disclaimer';
import Relationship from './Cards/Relationship';
import AttorneyCrimeInfo from './Cards/AttorneyCrimeInfo';
import PreviousFelonies from './Cards/PreviousFelonies';
import SelectFelonies from './Cards/SelectFelonies';

const style = {
  paperStyle: {
    width: '90vw',
    display: 'inline-block',
    margin: 20,
    backgroundColor: grey300
  }
};

//main page
export default class Home extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      cardDisplay: 0,
      crimeList: []
    }
  }

  componentWillMount(){
    //gets list of all crimes from backend
    fetch('http://localhost:5000/list', {
      method: 'GET',
      mode:'no-cors',
      dataType: 'json'
    })
      .then(r => r.json())
      .then(r => {
        this.setState({
          crimeList: r.results
        })
      })
      .catch(err => console.log(err))
  }
  //array of quesitons - probably want to change this depending on how backend is written
components = [
        {name: Welcome},
        {name: Disclaimer},
        {name: Relationship},
        {name: AttorneyCrimeInfo},
        {name: PreviousFelonies},
        {name: SelectFelonies}
    ];

  //changes which question is being displayed (goes to next)
  handleNext = (data) => {
    let count = this.state.cardDisplay;
    count++;
    this.setState({
      cardDisplay: count
    })
  }

  //changes which question is being displayed (goes to previous)
  handlePrevious = () => {
    let count = this.state.cardDisplay;
    count--;
    this.setState({
      cardDisplay: count
    })
  }

  render () {
    let ComponentCard = this.components[this.state.cardDisplay].name;

    //only display back button after first question
    let backButton = '';
    if(this.state.cardDisplay > 0){
      backButton =   <RaisedButton
                        label="Back"
                        onClick={this.handlePrevious}
                      />
    }
    return(
    <div>
      <AppBarTop />
      <Grid fluid>
        <Row>
          <LinearProgress
            mode="determinate"
            value={this.state.cardDisplay}
            max={7}
            />
        </Row>
        <Row>
          <Col xs style={style.column}>
              <Paper style={style.paperStyle} zDepth={3}>
                <ComponentCard crimeList={this.state.crimeList} next={this.handleNext} previous={this.handlePrevious}/>
              </Paper>
          </Col>
        </Row>
    </Grid>
    </div>
  )}
}
