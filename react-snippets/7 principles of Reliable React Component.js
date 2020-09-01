Principles of reliable react component - 

1. *SRP* - Single Responsiblity Principle. Think SRP in terms of people. Close coupling between related things and loose coupling between unrelated things.

A component should have only one responsiblity and only one reason to change it.

Case Study - 

WeatherForm - Implements both weather and form components. Change in Form breakes the display. Better to split the components.

Fetching and rendering logic. - Api calls - componentDidMount - // unrelated logics together. It has two reasons to change. Container/Presentation component like structure.

HOCs helps us implement SRP. PP(Props Proxy). API + compose

PersistanceForm - HOC - with Persistence (HOC with parametres).


2. *Encapsulation* Tightly Coupled Vs Loosely coupled.

Component should hide it's internal working and should expose well defined props. 

Case Study - Not passing the complete this reference but the handleChange Method.

3. *Composition* - Builds on the SRP priniple.

Usecase - 

4. *Resuable* - SRP

5. Pure / Almost Pure - Using compose and HOC + redux saga.
  purification form global variable - *defaultprops* = makes it easier to test also.
  purification from network requests - saga + insert lifecycle hooks + compose.

6. Meaning 
  Naming should be consistent and the code should be readable.
