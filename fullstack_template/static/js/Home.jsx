import AppBarTop from './AppBar';
import {Card, CardActions, CardHeader, CardTitle, CardText, Checkbox, LinearProgress, Paper, RaisedButton} from 'material-ui';
import React from 'react';
import {Grid, Row, Col } from 'react-flexbox-grid';
import {grey300} from 'material-ui/styles/colors';

//each "form" page is separated into different components
import Welcome from './Cards/Welcome';
import Disclaimer from './Cards/Disclaimer';
import Relationship from './Cards/Relationship';
import CurrentCharge from './Cards/CurrentCharge';
import PreviousFelonies from './Cards/PreviousFelonies';
import SelectFelonies from './Cards/SelectFelonies';
import Dates from './Cards/Dates';
import Results from './Cards/Results';

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
      crimeList: [],
      PreviousFeloniesCount: 0
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
  //array of cards
components = [Welcome, Disclaimer, Relationship, CurrentCharge, PreviousFelonies, SelectFelonies, Dates, Results];

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

  liftPreviousCount = (count) => {
    this.setState({
      PreviousFeloniesCount: count
    })
  }

  startOver = () => {
    this.setState({
      cardDisplay: 0
    })
  }

  render () {
    let ComponentCard = this.components[this.state.cardDisplay];

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
                <ComponentCard
                  crimeList={this.state.crimeList}
                  next={this.handleNext}
                  previous={this.handlePrevious}
                  previousCountFunction={this.liftPreviousCount}
                  previousCount={this.state.PreviousFeloniesCount}
                  startOver={this.startOver}
                  />
              </Paper>
          </Col>
        </Row>
    </Grid>
    </div>
  )}
}
