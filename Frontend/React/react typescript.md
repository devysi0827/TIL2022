# react typescript

### 사용이유

- JS에서 오류로 판단하지 않거나, 예상과 다른 행동을 하는 구문 오류를 편하게 수정하기 위해서 사용
- JS의 모든 기능과 호환가능하여 기존방식대로 사용하면 된다. 



### 간단한 원리

- 프로그램을 실행시키지 않으면서 코드의 오류를 검출하는 것을 _정적 검사_라고 합니다. 어떤 것이 오류인지와 어떤 것이 연산 되는 값에 기인하지 않음을 정하는 것이 정적 *타입* 검사입니다.

- _정적 타입 검사자_인 TypeScript는 프로그램을 실행시키기 전에 _값의 종류_를 기반으로 프로그램의 오류를 찾습니다. 



### interface

- 객체의 행태를 명시적으로 나태내기 위해서 사용

  - ts 코드

  ```tsx
  interface Person {
    firstName: string;
    lastName: string;
  }
   
  function greeter(person: Person) {
    return "Hello, " + person.firstName + " " + person.lastName;
  }
   
  let user = { firstName: "Jane", lastName: "User" };
   
  document.body.textContent = greeter(user);
  ```

  - js 코드

  ```js
  var Student = /** @class */ (function () {
      function Student(firstName, middleInitial, lastName) {
          this.firstName = firstName;
          this.middleInitial = middleInitial;
          this.lastName = lastName;
          this.fullName = firstName + " " + middleInitial + " " + lastName;
      }
      return Student;
  }());
  function greeter(person) {
      return "Hello, " + person.firstName + " " + person.lastName;
  }
  var user = new Student("Jane", "M.", "User");
  document.body.textContent = greeter(user);
  ```



### 참고문서

https://www.typescriptlang.org/ko/docs/handbook/typescript-from-scratch.html