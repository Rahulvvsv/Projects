import React, { Component } from 'react';
import './App.css';
import Anyname from './Person/Person.js'
class App extends Component {
  state  = {
    persons : [
      {name:"Yuno",age:16},
      {name:"Yami",age:29},
      {name:"Asta",age:15}
    ]
  };
  switchNameHandler = ( ) => {
    //console.log('was clicked!');
    // dont do this this.state.persons[0].name = "Julius";
    this.setState({
      persons : [
        {name:"julius",age:30},
        {name:"Merolena",age:29},
        {name:"Asta",age:15}
      ]
    })
  };
  render() {
    return (
      <div className="App">
        <h1>Hi, I am a  react developer , just kidding</h1>
        <button onClick={this.switchNameHandler}>Switch Name</button>
      <Anyname  
      name={this.state.persons[0].name} 
      age={this.state.persons[0].age}
      />
      <Anyname  
      name={this.state.persons[1].name} 
      age={this.state.persons[1].age}
      click ={this.switchNameHandler}/>
      <Anyname  
      name={this.state.persons[2].name} 
      age={this.state.persons[2].age}/>
      <Anyname  
      name={this.state.persons[0].name}
      age={this.state.persons[0].age}>Hello children how ya doing</Anyname>
      </div>
    );
  }
}

export default App;
