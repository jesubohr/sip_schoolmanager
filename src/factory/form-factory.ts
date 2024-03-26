import type { InputField, Method, SubmitAction } from "@/types"
import { Form } from "@/models/form"

interface FormProps {
  method: Method
  action: string
  inputs: InputField[]
  onSubmit: SubmitAction<Form>
}
export class FormFactory {
  constructor() {}

  buildForm({ method, action, inputs, onSubmit }: FormProps) {
    return new Form({
      method: method,
      action: action,
      inputs: inputs,
      onSubmit: onSubmit
    })
  }
}
