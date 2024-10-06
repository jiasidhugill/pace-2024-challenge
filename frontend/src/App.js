import React, { useState } from 'react';
import HomeScreen from './pages/HomeScreen';
import StartingMenu from './pages/StartingMenu';  // The next scene to transition to
import IncreaseOzone from './pages/IncreaseOzone';  // The next scene to transition to
import DecreaseOzone from './pages/DecreaseOzone';  // The next scene to transition to
import './App.css';  // Import your new CSS for transitions

const App = () => {
    const [currentScene, setCurrentScene] = useState('homeScreen');  // State to track the current scene
    // const [fade, setFade] = useState('fade-in');  // State for fade-in/fade-out transitions
    const handleSceneChange = () => {
        setCurrentScene('startingMenu');  // Change to StartingMenu scene
    };

    const handleStartingScreenChange = () => {
        setCurrentScene('DecreaseOzone');  // Change to Increase Phytoplankton scene
    };

    return (
        <div>
            {currentScene === 'homeScreen' && <HomeScreen onChoice={handleSceneChange} />}

            {currentScene === 'startingMenu' && <StartingMenu onChoice={handleStartingScreenChange} />}

            {currentScene === 'IncreaseOzone' && <IncreaseOzone onChoice={handleSceneChange} />}

            {currentScene === 'DecreaseOzone' && <DecreaseOzone onChoice={handleSceneChange} />}
        </div>
    );
};


export default App;
