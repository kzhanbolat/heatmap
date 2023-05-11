import React from 'react';
import './App.css';
import Maphtml from './component/maphtml'
import MyCondition from './component/button'
import Myquery from './component/button_2'
import { useState } from 'react';










function App() {
  const [data, setData] = useState(null);

  const handleData = (newData) => {
    setData(newData);
  }
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
  
      <MyCondition onData={handleData}/>
      {/* <Myquery/> */}
      <Maphtml data={data}/>
      <header className="App-header">
      
	    
      </header>
    </div>
  );
}

export default App;
