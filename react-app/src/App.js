import React from 'react';
import './App.css';
import { CardList } from './components/card-list/card-list.component';

class App extends React.Component {

  constructor() {
    super()

    this.state = {
      message : 'Welcome to react tutorials',
      monsters: []
    }
  }

  componentDidMount() {
    console.log(this.state)
    fetch('https://jsonplaceholder.typicode.com/users')
    .then(res => res.json())
    .then(users => {this.setState({monsters:users})})
  }

  render()  {
    return (
    <div className="App">
          <p>{this.state.message}</p>
          <h3>Hello, Bharath</h3>
          <button onClick={() => this.setState({message:'button is clicked'})}>Click here</button>
          <CardList name="Bharath" role='Operator' monsters={this.state.monsters}/>
    </div>
    );
  }
}




export default App;
