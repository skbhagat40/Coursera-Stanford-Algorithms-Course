Knockout js - MVVM Library ( Model View View Model).
ko.
Key parts - viewmodel binding, observables. ko.observable(), ko.dependentobservable() // Keeps track of value updation.

templating // update based re-rendering.

Example script.

// dependend observable, array of observables, // Twitter visiblity, no need to add onClick binding, since, view model.

// can define and bind to templates, with view model data.

Pretty much similar to what Angular Does.

```
<html>
  <head>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/knockout/3.3.0/knockout-min.js"
      type="text/javascript"
    ></script>
  </head>
    <body>
        <input data-bind = "value: firstName" />
        <p data-bind =  "text: firstName"></p>
    </body>
  <script>
      function ViewModel(){
          this.firstName = ko.observable('Enter Your Name');
      }
      ko.applyBindings(new ViewModel())
  </script>
</html>;


```
