# react styled


### 설치

```
# with npm
npm install --save styled-components
npm i -D @types/styled-components
```

- vscode 같은 경우 styled에서 자동완성이 안되기 때문에, vscode-styled-components를 설치해주면 좋다.



### 사용하는 이유

- 더 쉬운 유지관리를 위해서(본문의 코드가 매우 짧아진다)



### 확장을 통한 재사용

```tsx
const Button = styled.button`
  display: inline-block;
  color: green;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid green;
  border-radius: 3px;
  display: block;
`;

const TomatoButton = styled(Button)`
  color: tomato;
  border-color: tomato;
  font-size: 10em
`;

----------------------------------------------------------------------------------

function App() {
  return (
    <div className="App">
      <button> html tag 버튼</button>
      <Button>우리가 디자인한 버튼</Button>
      <TomatoButton>확장한 버튼 </TomatoButton>
    </div>
  );
}
    
```

- 위 코드의 Button처럼 기존 html 태그를 받아서 css를 만들고 새로운 컴포넌트 처럼 사용이 가능하다.

- 하지만 매 번 비슷한 내용을 새로 만들 수 없으므로 styled(`component이름`)을 통해서 확장을 통해 수정을 할 수 있다. 실제로 TomamoButton은 그렇게 확장을 하여 색과 크기를 수정한 케이스이다.

  ![react styled](/home/seil/Desktop/TIL2022/Frontend/React/react styled.assets/react styled-16448034606871.png)



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

  
