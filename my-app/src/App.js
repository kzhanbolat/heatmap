import React from 'react';
import './App.css';
import Maphtml from './component/maphtml'
import MyCondition from './component/button'
import Myquery from './component/button_2'










function App() {
  return (
    <div className="App">
  {/* <div>
    <div>
      <label for="input-field">City:</label>
      <input type="text" id="input-field" name="input-field"></input>
      <button type="submit">Submit</button>
    </div>
    <div>
      <label for="input-field">Category:</label>
      <input type="text" id="input-field" name="input-field"></input>
      <button type="submit">Submit</button>
    </div>
    <div>
      <label for="input-field">Subcategory:</label>
      <input type="text" id="input-field" name="input-field"></input>
      <button type="submit">Submit</button>
    </div>
    <div>
      <label for="input-field">Condition 1:</label>
      <input type="text" id="input-field" name="input-field"></input>
      <button type="submit">Submit</button>
    </div>
    <div>
      <label for="input-field">Condition 2:</label>
      <input type="text" id="input-field" name="input-field"></input>
      <button type="submit">Submit</button>
    </div>
  </div> */}
      <MyCondition/>
      <Myquery/>
      <Maphtml/>
      <header className="App-header">
      
	    
      </header>
    </div>
  );
}

export default App;
