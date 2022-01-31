import React from 'react';

import './card.styles.css';


export const CardList  = props =>{
    console.log(props); 
    return (
        <div>
            <h1>{props.monster.name}</h1>
        </div>
    );
};

