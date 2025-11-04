// interface ButtonProps {
//     onClick:string;
//     buttonType:string;
// }


// const Button = ({OnClick,buttonType}:ButtonProps)=> {
//   return (
//     <button className={buttonType} onclick = {OnClick}>
//       Click Me
//     </button>
//   );
// }

// export default Button;
//my terrible attempt at a button component ↑

// import React from 'react'
// import Alert from './Alert';
// import { useState } from "react";

// interface ButtonProps {
//     children: string;
//     color?: "primary" | "secondary" | "success" | "danger" | "warning" | "info" | "light" | "dark";
//     onClick: () => void;
// }



// const Button = ({children, onClick, color = "primary"}:ButtonProps) => {
//   return (
//     <>
//       <button className ={"btn btn-"+color} onClick = {onClick}>{children}</button>
//       <Alert showToggle="hide">
//         This is an alert message!
//       </Alert>
//     </>
//   )
// }

// export default Button

import React from 'react'
import Alert from './Alert';

interface ButtonProps {
    children: string;
    color?: "primary" | "secondary" | "success" | "danger" | "warning" | "info" | "light" | "dark";
    onClick: () => void;
}



const Button = ({children, onClick, color = "primary"}:ButtonProps) => {
  return (
    <>
      <button className ={"btn btn-"+color} onClick = {onClick}>{children}</button>
    </>
  )
}

export default Button