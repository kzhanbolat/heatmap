import React from 'react';
// import map from '../images/voronoi_generated.html' {map}
const Maphtml = (props) => {
    return (
      <div >
      <iframe  title="My Map" src="voronoi_generated.html"  width="100%" height="800px"  ></iframe>
      {/* {props.data && <div>{props.data}</div>}  */}
    </div>
    );
  };
  
  export default Maphtml;



  

 