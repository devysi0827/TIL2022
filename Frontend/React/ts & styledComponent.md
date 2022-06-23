# typeScript && styledComponent props

```react
const QuizP = styled.div`
	font-weight: ${props => props.weight || '900'};
`
```

```react
 <QuizP weight="800">{quizData.quizTitle}</QuizP>
```



- 다음과 같이 props 구문을 이용하여서 값을 지정하거나 기본값으로 css를 매길 수 있다.