import React, { useState, useEffect } from 'react';

import ozone1 from './styles/assets/ozone1.png';
import ozone2 from './styles/assets/ozone2.png';
import ozone3 from './styles/assets/ozone3.png';
import ozone4 from './styles/assets/ozone4.png';

import cfc1 from './styles/assets/cfc1.png';
import cfc2 from './styles/assets/cfc2.png';

import uv from './styles/assets/uv.png';

import './styles/DecreaseOzone.css';

const DecreaseOzone = ({ onChoice }) => {
    const [showOzone, setShowOzone] = useState(true); // State to toggle between small and big algae
    const [showNextButton, setShowNextButton] = useState(false); // State to show the next button
    useEffect(() => {
        const timer = setTimeout(() => {
            setShowOzone(false);
        }, 8000);

        // Set a timer to show the next button 1 second after the big algae appears
        const nextButtonTimer = setTimeout(() => {
            setShowNextButton(true);
        }, 4000);

        return () => {
            clearTimeout(timer);
            clearTimeout(nextButtonTimer);
        };
    }, []);

    return (
        <div className="ozone-container">
            <h2>Decrease Ozone Level</h2>
            <p>Your action has decreased ozone levels.</p>
            {/* You can add more details or actions related to this scenario */}
            {showOzone && (
                <img
                    src={ozone1}
                    alt="ozone"
                    width="120vw"
                    className={`ozone1 ${showOzone ? 'visible' : ''}`} // Add visible class based on state
                />
            )}
            {showOzone && (
                <img
                    src={ozone2}
                    alt="ozone"
                    width="120vw"
                    className={`ozone2 ${showOzone ? 'visible' : ''}`} // Add visible class based on state
                />
            )}
            {showOzone && (
                <img
                    src={ozone3}
                    alt="ozone"
                    width="120vw"
                    className={`ozone3 ${showOzone ? 'visible' : ''}`} // Add visible class based on state
                />
            )}
            {showOzone && (
                <img
                    src={ozone4}
                    alt="ozone"
                    width="120vw"
                    className={`ozone4 ${showOzone ? 'visible' : ''}`} // Add visible class based on state
                />
            )}
            {/*CFCs*/}
            {(
                <img
                    src={cfc1}
                    alt="cfc"
                    width="120vw"
                    className={'cfc1'} // Add visible class based on state
                />
            )}
            {(
                <img
                    src={cfc2}
                    alt="cfc"
                    width="120vw"
                    className={'cfc2'} // Add visible class based on state
                />
            )}
            {/* Next button */}
            {showNextButton && (
                <button className="next-button" onClick={() => onChoice("startingMenu")}>
                    Next
                </button>
            )}
            {/* UV rays smh */}
            {(
                <img
                    src={uv}
                    alt="uv"
                    width="120vw"
                    className={'uv1'} // Add visible class based on state
                />
            )}
            {(
                <img
                    src={uv}
                    alt="uv"
                    width="120vw"
                    className={'uv2'} // Add visible class based on state
                />
            )}
            {(
                <img
                    src={uv}
                    alt="uv"
                    width="120vw"
                    className={'uv3'} // Add visible class based on state
                />
            )}
            {(
                <img
                    src={uv}
                    alt="uv"
                    width="120vw"
                    className={'uv4'} // Add visible class based on state
                />
            )}
        </div>
    );
};

export default DecreaseOzone;