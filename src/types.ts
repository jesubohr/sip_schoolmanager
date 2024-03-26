export interface InputField {
  type: string
  id: string
  name: string
  label?: string
  value?: string
  placeholder?: string
  required: boolean
  validators: InputValidator[]
}
export type InputValidator = (value: string) => {
  isValid: boolean
  message: string
}
export type SubmitAction<T> = (...args: T[]) => void
export type Method = "GET" | "POST" | "PUT" | "DELETE"
