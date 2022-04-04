# React Typescript

### Js VS Ts

- Js는 동적 타입의 인터프리터 언어로 런타임에서 오류를 발견
- Ts는 정적 타입의 컴파일 언어이며 Ts Compiler 또는 바벨(Babel)을 통해 자바스크립트 코드로 변환
- Ts는 코드 작성 단계에서 타입을 체크해 오류를 확인할 수 있고 미리 타입을 결정하기 때문에 실행 속도가 매우 빠르나 코드 작성 시 매번 타입을 결정해야 하기 때문에 번거롭고 코드량이 증가하며 컴파일 시간이 오래 걸림.
- Ts는 ES6(ECMAScript 6)에서 새롭게 사용된 문법을 포함하고 있으며 클래스, 인터페이스, 상속, 모듈 등과 같은 객체 지향 프로그래밍 패턴
- Ts는 Js의 SuperSet으로 모든 .js는 .ts로



### 장점

1. 높은 수준의 코드 탐색과 디버깅
2. 자바스크립트 호환
3. 강력한 생태계
4. 점진적 전환 가능

유지보수가 중요한 장기 프로젝트일수록 타입스크립트의 이점이 부각될 것입니다.



### 기본 문법

- 기본타입 : Boolean, Number, String, Object, Array, Tuple, Enum, Any, Void, Null, Undefined, Never

```typescript
let str: string = 'hi';
let num: number = 100;

let arr: Array = [1, 2, 3];
let arr2: number[] = [1, 2, 3];

let obj: object = {};
let obj2: { name: string, age: number} = {
 name: 'hoho',
 age: 22
};

function add(a: number, b: number): number {
return a+b;
}
//옵셔널 파라미터
function log(a: string, b?: string, c?: string) {
 console.log(a);
}
```

- 추가타입 : Js에는 없지만 Ts는 있음.

  - Tuple: 배열의 타입 순서와 배열 길이를 지정할 수 있는 타입입니다.
  -  Enum: Number 또는 String 값 집합에 고정된 이름을 부여할 수 있는 타입입니다. 값의 종류가 일정한 범위로 정해져 있는 경우에 유용합니다. 기본적으로 0부터 시작하며 값은 1씩 증가합니다.
  - Any: 모든 데이터 타입을 허용합니다.
  -  Void: 변수에는 undefined와 null만 할당하고 함수에는 리턴 값을 설정할 수 없는 타입입니다.
  -  Never: 특정 값이 절대 발생할 수 없을 때 사용합니다.

- 인터페이스: 인터페이스는 타입을 정의한 규칙을 의미합니다.

  - 기본

  ```tsx
  interface User {
   age: number;
   name: string;
  }
  
  var person: User = {
   age: 30,
   name: 'aa'
  }
  
  function getUser(user: User) {
   console.log(user);
  }
  ```

  - 응용

  ```tsx
  interface StringArray {
   [index: number]: string;
  }
  
  var arr2: StringArray = ['a', 'b', 'c'];
  arr[0] = 10 //Error;
  
  interface StringRegexDictionary {
   [key: string]: RegExp // RegExp : 정규표현식
  }
  
  var obj: StringRegexDictionary = {
   cssFile: /\.css$/,
   jsFile: 'a' //Error
  }
  
  obj['cssFile'] = /\.css$/;
  obj['jsFile'] = 'a' //Error
  
  interface Person{
   name: string;
   age: number;
  }
  
  interface User extends Person{
   language: string;
  }
  ```

  - 연산자

  ```tsx
  // Union(or)
  function askSomeone(someone: Developer2 | Person) {
   console.log(someone);
  }
  
  // Intersection(and)
  function askSomeone(someone: Developer & Person) {
   console.log(someone);
  }
  ```

  - 제네릭 `모르겠`

  ```tsx
  function logText <T> (text: T):T {
   return text;
  }
  
  logText<string>('aa');
  logText<number>(100);
  ```



### 타입 응용

- 타입 추론 : Ts가 코드를 해석하면서, Ts의 변수와  충돌 시 에러를 반환하거나 Union타입으로 Best Common Type을 정의함.
- 타입 단언 : 타입스크립트가 해석하는 것보다 개발자가 확실한 목적을 가지고 타입을 지정하는 것을 의미합니다. 
- 타입 호환 : 타입이 특정 타입과 잘 호환되는 지를 의미합니다.



### 참고문서

https://www.samsungsds.com/kr/insights/TypeScript.html
