While updating the state, don't pass by reference use destructring.
eg.
```
question = {
  id: 1,
  options: [{ id: 2, order: 3}, {....}]
}
updatedOptions = question?.options // don't do it. state change will not be triggered.
updatedOptions = {...question.options} // this is better. as it's a new reference, and there will be state change triggered.
```
# Min date validation.
