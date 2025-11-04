import type { ReactNode } from "react";

interface AlertProps {
    children:ReactNode;
    onClose: () => void;
}

export const Alert = ({children, onClose}: AlertProps) => {
  return (
    <>  
      <div className = "alert alert-danger alert-dismissable" >
        <h1>{children}</h1>
        <button type = "button" className = "btn-close" data-bs-dismiss = "alert" aria-label = "Close" onClick = {onClose} ></button>
      </div>
    </>
  )
}

export default Alert
//rafce
//rafce is a shortcut to create a functional component with an export statement