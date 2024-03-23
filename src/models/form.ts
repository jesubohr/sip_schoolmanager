import type { InputField, Method, SubmitAction } from "@/types"

interface FormProps {
  method?: Method
  action?: string
  inputs?: InputField[]
  onSubmit?: SubmitAction
}
export class Form {
  #method: Method
  #action: string
  #inputs: InputField[]
  #onSubmit: SubmitAction

  constructor({
    method = "POST",
    action = "",
    inputs = [],
    onSubmit = () => {}
  }: FormProps) {
    this.#method = method
    this.#action = action
    this.#inputs = inputs
    this.#onSubmit = onSubmit
  }

  get method() {
    return this.#method
  }

  get action() {
    return this.#action
  }

  get inputs() {
    return this.#inputs
  }

  submit() {
    this.#onSubmit(this)
  }
}
