import React, { useEffect, useState } from 'react';

import './App.css';

function App() {
  const [imageSrc, setImageSrc] = useState('');

  useEffect(() => {
    const fetchImage = async () => {
      const response = await fetch('pace');
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      console.log(url);
      setImageSrc(url);
    };

    fetchImage();
  }, []);

  return (
    <div>
      {imageSrc ? (
        <img src={imageSrc} alt="Generated Plot" />
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.js</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         Learn React
  //       </a>
  //       <img src="/pace.png" alt="my plot"></img>
  //     </header>
  //   </div>
  // );
}

export default App;
