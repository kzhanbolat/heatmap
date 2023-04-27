import React, { useState } from 'react';

function MyCondition() {
  const [inputValues, setInputValues] = useState({ city: '', category: '', sub_category: '', name: '', condition_1: '', condition_2: '', condition_3: '' });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setInputValues({ ...inputValues, [name]: value });
  }

  return (
    <div>
      <input type="text" name="city" placeholder="город" value={inputValues.city} onChange={handleInputChange} />
      <input type="text" name="category" value={inputValues.category} onChange={handleInputChange} />
      <input type="text" name="sub_category" value={inputValues.sub_category} onChange={handleInputChange} />
      <input type="text" name="name" value={inputValues.name} onChange={handleInputChange} />
      <input type="text" name="condition_1" value={inputValues.condition_1} onChange={handleInputChange} />
      <input type="text" name="condition_2" value={inputValues.condition_2} onChange={handleInputChange} />
      <input type="text" name="condition_3" value={inputValues.condition_3} onChange={handleInputChange} />

      <button onClick={() => {
        fetch('http://127.0.0.1:8000/city', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Credentials" : true,
            "Access-Control-Allow-Origin" : "*"
          },
          body: JSON.stringify(inputValues)
        })
        .then(response => console.log(response))
        .catch(error => console.error(error));

      }}>Submit conditions</button>
    </div>
  );
}

export default MyCondition;