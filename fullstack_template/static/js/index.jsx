import Home from "./Home";
import React from "react";
import ReactDOM from "react-dom";
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import customMuiTheme from './muiTheme';

const App = () => (
  <MuiThemeProvider muiTheme={getMuiTheme(customMuiTheme)}>
    <Home />
  </MuiThemeProvider>
);

ReactDOM.render(<App />, document.getElementById("content"));
