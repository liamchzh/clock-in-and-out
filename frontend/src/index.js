import React from 'react';
import ReactDOM from 'react-dom';
import Amplify from 'aws-amplify';
import { BrowserRouter as Router } from 'react-router-dom';
import './index.css';
import App from './App';

Amplify.configure({
});

ReactDOM.render(
  <Router>
    <App />
  </Router>,
  document.getElementById('root')
);
