// Example usage
import {useFrom} from 'react-hook-form'

function DemoForm(){
  const {register, formValues} = useForm();
  const handleSubmit = (values) => { console.log('form values', values); };
  return (
    <form onSubmit={handleSubmit(formValues)}>
      <input type="text" name="name" ref={register}/>
    </form>
  )
}

/* 
Internal Working of react-hook-form,
1. We can pass funtions to ref.
so, register is a function which looks like this,

function register(ref){
  const {name,type,value} = ref;
  filedsAndValues.current[name] = value;
  addEventListener(ref, handleFieldChange);
}

// now they mantain a ref for storing all form values, which looks like this - 

const fieldsAndValues = React.useRef({});

// handleFieldChange = single function to handle change of all fields.

1. Updates the field values.
2. Async implementation returns a Promise.
3. Takes care of validation.

*/
