# react-router-dom

- 용도

  ```
  웹 라우터기능을 쉽게 수행하기 위해서
  ```

cf1). routing이란?

*라우팅*은 애플리케이션 엔드 포인트(URI)의 정의, 그리고 URI가 클라이언트 요청에 응답하는 방식을 말합니다. 

cf2). web router를 사용하는 이유

1. page의 history를 이용하여 별도의 탐색없이 이전 웹 상태를 가져오기 위해서

2. SPA 웹 페이지에서, 전체 HTML이 아닌 필요한 component만 로딩하므로 자원(로딩시간 등)을 아끼기 위해서 ( History mode덕에 가능하다. 이 원리는 다시 SPA의 개념으로 돌아가면 알 수 있다. )

3. `<a>`와 달리 페이지의 불필요한 렌더링을 막고 새로고침없이 페이지를 불러오기 위해서

4. nested route(중첩 루트)를 사용하게 해줌

   +). 1과 2의 개념을 합치면 하나의 웹페이지에서  각 순간의 정확한 상태를 기록하고 새로고침 없이 불러올 수 있다는 것이 된다. 이는 뒤로가기를 할 경우 사용자가 새로고침 없이 아주 편리하게 웹을 탐색할 수 있게 만들어준다.  

- 설치

  ```
  npm i react-router-dom
  ```

- React Router Components
  - BrowserRouter : HTML5 history API를 사용하여 URL과 UI를 동기화하고 그 상태를 유지시킴
  - Link : HTML `<a>`태그와 같은 기능, 다른 경로에 대한 링크를 생성하고 이동시킴
  - Route : 해당 URL과 일치하는 컴포넌트의 UI를 렌더링한다.
  - Routes : 기존의 switch의 변경된 이름으로, route들을 관리하고 해당하는 Route를 보여주는 역활을 한다
  
- Code

	- App.js
	
	```js
	import { render } from "react-dom"
	import {
	  BrowserRouter,
	  Routes,
	  Route
	} from "react-router-dom";
	import { Link} from "react-router-dom";
	import './App.css';
	import Expenses from "./Expenses";
	import Invoices from "./invoices";
	import Invoicesmain from "./invoicemain";
	import Outlets from "./Outlets";
	
	function App() {
	  const rootElement = document.getElementById("root");
	  // Commentary1
	  render(  
	    <BrowserRouter>
	      <Routes>
	        <Route path="/" element={<App />} />
	        <Route path="expenses" element={<Expenses />} />
	        // Commentary2
	        <Route path="invoices" element={<Invoices />} >
	          <Route path="" element={<Invoicesmain />} />
	          <Route path="outlets" element={<Outlets />} />
	        </Route>
			// Commentary3
	        <Route
	          path="*"
	          element={
	            <main style={{ padding: "1rem" }}>
	              <p>There's nothing here!</p>
	            </main>
	          }
	        />
	      </Routes>
	    </BrowserRouter>,
	    rootElement
	  );
	
	  return (
	    <div className="App">
	        <Link to="/invoices">Invoices</Link> |{" "}
	        <Link to="/expenses">Expenses</Link>
	    </div>
	  );
	}
	
	export default App;
	```
	
	- 코드해설
	  1. BrowserRouter, Routes, Route를 이용하여 routing을 적용하였다.
	  2. Outlet기능을 이용하여 children처럼 관리가 가능하다. 
	  3. 없는 페이지일 경우 `*`을 이용하여 이 페이지로 보낼 수 있다.
	
	
	
	- invoices.js
	
	```js
	import React from 'react';
	import { Outlet,Link } from 'react-router-dom';
	
	function invoices() {
	  return <div>
	       <h1>invoice</h1>
	       <Link to="outlets">outlets</Link>
	       <Outlet/>
	  </div>;
	}
	
	export default invoices;
	```
	
	

- react outlet image

  - invoices_main

    ![react-router-dom](/Users/yoonseil/Desktop/TIL2022/Frontend/React/images/react-router-dom.png)

  - invoices_outlets

![react-router-dom1](/Users/yoonseil/Desktop/TIL2022/Frontend/React/images/react-router-dom1.png)

### 참고문서

- express router의 정의 : https://expressjs.com/ko/guide/routing.html
- 왜 router를 써야하는가? 스택오버플로 답변 : https://stackoverflow.com/questions/39636411/what-is-routing-why-is-routing-needed-in-single-page-web-apps/43130149

- react-router 요소들에 대한 설명 : https://www.geeksforgeeks.org/reactjs-router/
- react-router 공식문서 사용법 : https://reactrouter.com/docs/en/v6/getting-started/overview

- react-router 공식문서 개념 : https://reactrouter.com/docs/en/v6/getting-started/concepts
- outlet 코드 예시: https://www.youtube.com/watch?v=CHHXeHVK-8U