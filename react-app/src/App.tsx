// import ListGroup from "./components/ListGroup";
// function App() {
//   let items = ["New York", "San Francisco", "Tokyo", "London", "Paris"];  
//   const handleSelectItem = (item: string) => {
//     console.log(item);
//   }
  
//   return (
//     <div>
//       <ListGroup items={items} heading ="Cities" onSelectItem={handleSelectItem}/>
//     </div>
//   );
// }
//
// export default App;

//Children Prop Example
// import Alert from './components/Alert';

// function App() {

//   return (
//     <div>
//       <Alert>
//         Hello <span>World</span>
//       </Alert>
//     </div>
//   );
// }

// export default App;

// import Button from './components/Button';

// function App() {

//   return (
//     <div>
//       <Button {ButtonProps= console.log("click"),"btn btn-primary"}/>
//     </div>
//   );
// }

// export default App;
//my attempt at a button component up

// import Button from './components/Button';

// const onClickHandler = () => {
  
// }

// function App() {

//   return (
//     <div>
//       <Button color="danger" onClick={onClickHandler}>
//         My Button
//       </Button>

//     </div>
//   );
// }

// export default App;

import { useState } from 'react';
import Alert from './components/Alert';
import Button from './components/Button';


function App() {
  const [alertVisible, setAlertVisible] = useState(false);

  return (
    <div>
      {alertVisible && <Alert onClose ={() => setAlertVisible(false)}>
        My Alert
      </Alert>}
      <Button color="primary" onClick={() => setAlertVisible(true)}>
        My Button
      </Button>

    </div>
  );
}

export default App;
