import React, { useState } from 'react';
import { cities, categories } from './data.js';
import {  subcategories } from './subcategories';

function MyCondition(props) {
    const [newData, setNewData] = useState(null);

    const handleNewData = () => {
        // generate new data here
        props.onData(newData);
    }


  const [inputValues, setInputValues] = useState({ city: '', category: '', sub_category: '', name: '', condition_1: '', condition_2: '', condition_3: '' });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setInputValues({ ...inputValues, [name]: value });
  }

  const handleCategoryChange = (event) => {
    const { value } = event.target;
    setInputValues({ ...inputValues, category: value, subcategory: '' });
  }

  const handleSubcategoryChange = (event) => {
    const { value } = event.target;
    setInputValues({ ...inputValues, subcategory: value });
  }

  return (
    <div>
    <div className = "select">
        {/* <input type="text" name="name" placeholder="название" value={inputValues.name.toLowerCase()} onChange={handleInputChange} /> */}
        <select name="city" value={inputValues.city} onChange={handleInputChange}>
        <option value="">Select a city</option>
        {cities.map(city => <option key={city} value={city.toLowerCase()}>{city}</option>)}
        </select>
    <select name="category" value={inputValues.category} onChange={handleCategoryChange}>
        <option value="">Select a category</option>
        {categories.map((category, index) => (
          <option key={index} value={category.toLowerCase()}>{category}</option>
        ))}
      </select>
      <div>
      <input name="subcategory"
        type="text"
        placeholder="подкатегория"
        value={inputValues.subcategory}
        onChange={handleInputChange}
        list="words"
      />
      <datalist id="words">
        {subcategories.map((word) => (
          <option key={word} value={word.toLowerCase()} />
        ))}
      </datalist>
    </div>

      {/* <select name="subcategory" value={inputValues.subcategory} onChange={handleSubcategoryChange}>
        <option value="">Select a subcategory</option>
        {subcategories[inputValues.category]?.map((subcategory, index) => (
          <option key={index} value={subcategory}>{subcategory}</option>
        ))}
      </select> */}


        {/* 
        <select name="category" value={inputValues.category} onChange={handleInputChange}>
        <option value="">Select a category</option>
        {categories.map(category => <option key={category} value={category}>{category}</option>)}
        </select> */}
      {/* <input type="text" name="city" placeholder="город" value={inputValues.city} onChange={handleInputChange} /> */}
      {/* <input type="text" name="category" placeholder="категория" value={inputValues.category} onChange={handleInputChange} /> */}
      {/* <input type="text" name="sub_category"  placeholder="подкатегория" value={inputValues.sub_category} onChange={handleInputChange} /> */}
      
      {/* <input type="text" name="name"  value={inputValues.name} onChange={handleInputChange} />
      <input type="text" name="condition_1" value={inputValues.condition_1} onChange={handleInputChange} />
      <input type="text" name="condition_2" value={inputValues.condi tion_2} onChange={handleInputChange} />
      <input type="text" name="condition_3" value={inputValues.condition_3} onChange={handleInputChange} /> */}
 
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
        // window.location.reload(false)
      }
      
      
      } >Сгенерировать Карту</button><br/>
      <button onClick={handleNewData}>Generate Data</button>
     
    </div>
    <div className='select'>
    <a  href = "voronoi_generated.html" download > Загрузить карту</a>
    </div>
    
    </div>
    
  );
}

export default MyCondition;