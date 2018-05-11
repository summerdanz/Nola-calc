import '../../css/index.css';
import {Card, CardActions, CardHeader, CardTitle, CardText, RadioButton, RadioButtonGroup, RaisedButton} from 'material-ui';
import React from 'react';

export default class Results extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      goodTimeReleaseDate: null,
      earlyRelease: null,
      paroleEligibilityDate: null,
      paroleEligibility: null,
      lastReleaseDate: null
    }
  }
  componentWillMount(){
    //gets list of all crimes from backend
    fetch('http://localhost:5000/results', {
      method: 'GET',
      mode:'no-cors',
      dataType: 'json'
    })
      .then(r => r.json())
      .then(r => {
        this.setState({
          goodTimeReleaseDate: r.goodTimeReleaseDate,
          earlyRelease: r.earlyRelease,
          paroleEligibilityDate: r.paroleEligibilityDate,
          paroleEligibility: r.paroleEligibility,
          lastReleaseDate: r.lastReleaseDate

        })
      })
      .catch(err => console.log(err))
  }

  render () {
    return(
        <Card>
          <CardText>
            <h1>Conclusion</h1>

            <p>Based on your inputs, we have determined the following:</p>

            <p>Good Time Release Date: {this.state.goodTimeReleaseDate}</p>

            <p>Based on your inputs, {this.state.earlyRelease}.</p>

            <p>Parole Eligible Date: {this.state.paroleEligibilityDate}</p>

            <p>Based on your inputs, {this.state.paroleEligibility} </p>

            <p>Last Possible Release Date: {this.state.lastReleaseDate} </p>

            <p>Note: These conclusions and calculations are based on the information that you have provided about facts known around the time of conviction. However, there may be additional factors that can affect when an individual is eligible for release. For example, individuals may work time off their sentences by participating in DOC programs while incarcerated. Also, there are special requirements that some sex offender registrants have to meet before being released on good time or parole.</p>
        </CardText>
          <CardActions>
            <RaisedButton
              label="Start Over"
              primary={true}
              onClick={this.props.startOver}
            />
          </CardActions>
        </Card>
    )
  }
}
