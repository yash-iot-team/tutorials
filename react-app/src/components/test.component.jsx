import React from 'react';

/* export const Test = props =>{
    console.log(props);

    return(
        <div>
            {props.monsters.map(monster => (
                <h1 key={monster.id}>{monster.name}</h1>
                ))}
        </div>
    );
}; */


class Test extends React.Component {
    constructor() {
        super()
    
        this.state = {
          role: 'operator',
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

        return(
                <div>test</div>
        )    

      }
}

export default Test;