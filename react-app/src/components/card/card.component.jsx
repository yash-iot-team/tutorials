import React from 'react';

import './card.styles.css';


export const Card  = props =>{
    console.log(props); 
    return (
        <div className='card-container'>
        <img alt='' src={`https://robohash.org/${props.monster.id}?set=set2&size=180x180`} />
            <h1>{props.monster.name}</h1>
            <p>{props.monster.email}</p>
        </div>
    );
};

