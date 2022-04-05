# Index.html, Index.js, App.js

### Index.html

- 브라우저 화면 
-  `id=root`부분에 `App.js` 파일을 연결시켜서 원하는 화면을 렌더링 시킴

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
    <title>React App</title>
    <style id="mycss">
      p {
        /* color : red */
      }
    </style>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  </body>
</html>

```



### Index.js

- index.js는 연결역할을 수행( pacakge.json에 이 시작점 역활이 표시)
- `document.getElementById('root')` 부분을 통해서 Index.html 부분에 App.js를 호출

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import TestApp from './TestApp';
import reportWebVitals from './reportWebVitals';
import {
  RecoilRoot,
} from 'recoil';

//브라우저에 컴포넌트를 보여줌
ReactDOM.render(
  //param1 - 화면에 보여줘야되는 렌더링할 컴포넌트
  <React.StrictMode>
    <RecoilRoot>
      <App />
      <TestApp/>
    </RecoilRoot>
  </React.StrictMode>,
    
	//param2 - 컴포넌트를 어디다 그려줄건지. index.html 파일에서 ID가 root인 엘리먼트를 찾아 뿌려줌
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

```

- package.json

```tsx
{
  "name": "hello-world",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```



### App.js

- React에 보여주고자 하는 실제 내용
- 내부 컴포넌트들이 바뀌면서 완성되는 것

```js
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

//Class 형태로 만들어진 컴포넌트는 꼭 render 함수 있어야하며 render 함수 내부에서 JSX 코드를 return 해주어야함.
class App extends Component {

  //render 함수
  render() {
  
    return (
    
      //JSX
      <div>리액트는 처음이지?</div>
    );
  }
}
export default App; //현 컴포넌트를 다른 곳에서 불러와 사용할 수 있도록 내보내기를 해줌.
```





### 참고내용

https://mjn5027.tistory.com/21
