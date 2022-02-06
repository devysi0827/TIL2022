# react styled


### 설치

```
# with npm
npm install --save styled-components
npm i -D @types/styled-components
```



### 사용하는 이유

- 더 쉬운 유지관리를 위해서(코드가 매우 짧아진다)



### code example1

- 무식하게 사용

  ```tsx
  import React from 'react';
  import styled from 'styled-components';
  
  
  const Button = styled.button`
    display: inline-block;
    color: palevioletred;
    font-size: 1em;
    margin: 1em;
    padding: 0.25em 1em;
    border: 2px solid palevioletred;
    border-radius: 3px;
    display: block;
  `;
  
  const TomatoButton = styled(Button)`
    color: tomato;
    border-color: tomato;
    font-size: 10em
  `;
  
  function App() {
    return (
      <div className="App">
        <button>kkkk</button>
        <Button>1111</Button>
        <TomatoButton>1234</TomatoButton>
      </div>
    );
  }
  
  export default App;
  ```
  

### code example2

- 분할 사용

  - App.tsx

  ```tsx
  import React from 'react';
  import { Button, TomatoButton } from './Theme.js'
  function App() {
    
    return (
      <div className="App">
  
        <button>kkkk</button>
        <Button>1111</Button>
        <TomatoButton>1234</TomatoButton>
      </div>
    );
  }
  
  export default App;
  
  ```

  - Theme.js

  ```js
  import React from 'react';
  import styled from 'styled-components';
  
  export const Button = styled.button`
    display: inline-block;
    color: palevioletred;
    font-size: 1em;
    margin: 1em;
    padding: 0.25em 1em;
    border: 2px solid palevioletred;
    border-radius: 3px;
    display: block;
  `;
  
  export const TomatoButton = styled(Button)`
    color: tomato;
    border-color: tomato;
    font-size: 5em
  `;
  
  
  ```

  
