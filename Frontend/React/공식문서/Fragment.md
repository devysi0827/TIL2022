# Fragment

사용이유 : React에서 컴포넌트가 여러 엘리먼트를 반환하는 것은 흔한 패턴입니다. Fragments는 DOM에 별도의 노드를 추가하지 않고 여러 자식을 그룹화할 수 있습니다.



ex1). 일반적인 React의 경우

- code

```react
class Table extends React.Component {
  render() {
    return (
      <table>
        <tr>
          <Columns />
        </tr>
      </table>
    );
  }
}
```

```react
class Columns extends React.Component {
  render() {
    return (
      <div>
        <td>Hello</td>
        <td>World</td>
      </div>
    );
  }
}
```

- 출력

```html
<table>
  <tr>
    <div>
      <td>Hello</td>
      <td>World</td>
    </div>
  </tr>
</table>
```





ex2). fragment 사용

- code

```react
class Columns extends React.Component {
  render() {
    return (
      <React.Fragment>
        <td>Hello</td>
        <td>World</td>
      </React.Fragment>
    );
  }
}
```

- 출력

```html
<table>
  <tr>
    <td>Hello</td>
    <td>World</td>
  </tr>
</table>
```

