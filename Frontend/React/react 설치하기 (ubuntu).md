# ubuntu in react

### node 및 npm 설치

```
# Using Ubuntu node install
curl -sL https://deb.nodesource.com/setup_15.x | sudo -E bash -

# Update
sudo apt-get install -y nodejs
## 업데이트를 하지 않는다면, react가 실행되지 않을 수 있다.

# version
node -v
npm -v
```



### react 설치

```js
// install react
npm install -g create-react-app

// create react
// v1. 기본 js파일
create-react-app my-app
// v2. tsx파일
create-react-app my-app --template typescript

// start react
cd my-app
npm start
```



### 참고문서

개인블로그,  node 설치 : https://blog.dalso.org/article/ubuntu-node-js-install

react 공식문서, 설치 : https://reactjs-kr.firebaseapp.com/docs/installation.html

react 공식문서, tsx 버전 app : https://ko.reactjs.org/docs/static-type-checking.html#typescript