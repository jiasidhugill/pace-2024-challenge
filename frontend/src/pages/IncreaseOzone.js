import React, { useState, useEffect } from 'react';

import ozone01 from './styles/assets/ozone1.png';
import ozone02 from './styles/assets/ozone2.png';
import ozone03 from './styles/assets/ozone3.png';
import ozone04 from './styles/assets/ozone4.png';

import uv_ray from './styles/assets/uv.png';

import './styles/IncreaseOzone.css';

const IncreaseOzone = ({ onChoice }) => {
    const [showOzone] = useState(true); // State to toggle between small and big algae
    const [showNextButton, setShowNextButton] = useState(false); // State to show the next button
    useEffect(() => {

        // Set a timer to show the next button 1 second after the big algae appears
        const nextButtonTimer = setTimeout(() => {
            setShowNextButton(true);
        }, 4000);

        return () => {
            clearTimeout(nextButtonTimer);
        };
    }, []);

    return (
        <div className="ozone-container">
            <h2>Increase Ozone Level</h2>
            <p>Your action has increased ozone levels.</p>
            {/* You can add more details or actions related to this scenario */}
            {showOzone && (
                <img
                    src={ozone01}
                    alt="ozone"
                    width="120vw"
                    className={`ozone01 ${showOzone ? 'visible' : ''}`} // Add visible class based on state
                />
            )}
            {showOzone && (
                <img
                    src={ozone02}
                    alt="ozone"
                    width="120vw"
                    className={`ozone02 visible`} // Add visible class based on state
                />
            )}
            {showOzone && (
                <img
                    src={ozone03}
                    alt="ozone"
                    width="120vw"
                    className={`ozone03 ${showOzone ? 'visible' : ''}`} // Add visible class based on state
                />
            )}
            {showOzone && (
                <img
                    src={ozone04}
                    alt="ozone"
                    width="120vw"
                    className={`ozone04 visible`} // Add visible class based on state
                />
            )}
            {(
                <img
                    src={uv_ray}
                    alt="uv"
                    width="120vw"
                    className={'uv01'} // Add visible class based on state
                />
            )}
            {(
                <img
                    src={uv_ray}
                    alt="uv"
                    width="120vw"
                    className={'uv02'} // Add visible class based on state
                />
            )}
            {(
                <img
                    src={uv_ray}
                    alt="uv"
                    width="120vw"
                    className={'uv03'} // Add visible class based on state
                />
            )}
            {(
                <img
                    src={uv_ray}
                    alt="uv"
                    width="120vw"
                    className={'uv04'} // Add visible class based on state
                />
            )}
            {/* Next button */}
            {showNextButton && (
                <button className="next-button" onClick={() => onChoice("startingMenu")}>
                    Next
                </button>
            )}
        </div>
    );
};

export default IncreaseOzone;