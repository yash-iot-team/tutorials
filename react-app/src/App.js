import React, { Component } from 'react';
import './App.css';

class App extends Component {

  constructor() {
    super()

    this.state = {
      message : 'Welcome to react tutorials',
      monsters: []
    }
  }

  componentDidMount() {
    fetch('https://jsonplaceholder.typicode.com/users')
    .then(res => res.json())
    .then(users => {this.setState({monsters:users})});
  }

  render()  {
    return (
    <div className="App">
        <p>{this.state.message}</p>
        <button onClick={() => this.setState({message:'button is clicked'})}>Click here</button>
        {this.state.monsters.map(monster => (
          <h1 key={monster.id}>{monster.name}</h1>
        ))}
    </div>
    );
  }
}

export default App;
