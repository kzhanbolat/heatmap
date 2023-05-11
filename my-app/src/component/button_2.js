import React, { useState } from 'react';

function Myquery() {
  const [inputValues, setInputValues] = useState({condition_1: '', condition_2: '', condition_3: '', condition_4: '' });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setInputValues({ ...inputValues, [name]: value });
  }

  return (
    <div>
      <input type="text" name="condition_1" placeholder="ваши условия" value={inputValues.condition_1} onChange={handleInputChange} />
      <input type="text" name="condition_2" placeholder="ваши условия" value={inputValues.condition_2} onChange={handleInputChange} />
      <input type="text" name="condition_3" placeholder="ваши условия" alue={inputValues.condition_3} onChange={handleInputChange} />
      <input type="text" name="condition_3" placeholder="ваши условия" value={inputValues.condition_4} onChange={handleInputChange} />

      <button onClick={() => {
        fetch('/query', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(inputValues)
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
      }}>Submit Query</button>
    </div>
  );
}

export default Myquery;