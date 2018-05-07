import '../../css/index.css';
import {Card, CardActions, CardHeader, CardTitle, CardText, RaisedButton} from 'material-ui';
import React from 'react';

export default class Welcome extends React.Component {
  render () {
    return(
        <Card>
          <CardHeader
            title="Welcome"
          />
          <CardText>
            This application is designed to calculate release dates of individuals sentenced under Louisiana law.
            The application first determines whether an individual is eligible for early release based on good time and/or parole.
            It then calculates individuals’ good time release dates, parole eligibility dates, and the last possible day they can be released. The release date calculation process only covers cases with an offense date that is later than November 1, 2017.
          </CardText>
          <CardActions>
            <RaisedButton
              primary={true}
              label="Let's Begin"
              onClick={this.props.next}
            />
          </CardActions>
        </Card>
    )
  }
}
