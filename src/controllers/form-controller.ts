import type { InputField } from "@/types"
import { type Form } from "@/models/form"
import { FormRender } from "@/render/form-render"
import { FormRepository } from "@/repository/form-repository"

type InputToValidate = Required<
  Pick<InputField, "name" | "id" | "value" | "validators">
>
export class FormController {
  #formRender = {} as FormRender
  #formRepository: FormRepository

  constructor() {
    this.#formRepository = new FormRepository()
  }

  async submitForm(form: Form) {
    this.#formRender = new FormRender(form)

    const inputValues = this.#getInputsWithValue(form)
    if (!this.#validateInputValue(inputValues)) return

    const groupByName = Object.groupBy(inputValues, (input) => input.name)
    const formData = Object.entries(groupByName).reduce((acc, [key, value]) => {
      acc[key] = value?.map((input) => input.value)[0] ?? ""
      return acc
    }, {} as Record<string, string>)

    try {
      const response = await this.#formRepository.sendData(
        form.action,
        formData
      )
      this.#formRender.setStatus(response.success, response.message)
    } catch (error) {
      this.#formRender.setStatus(false, error as string)
    }
  }

  #validateInputValue(inputs: InputToValidate[]) {
    const invalidInputs = [] as { id: string; message: string }[]
    inputs.map(input => input.validators.map(validator => {
      const { isValid, message } = validator(input.value, input.name)
      if (!isValid) invalidInputs.push({ id: input.id, message })
    }))

    if (invalidInputs.length) {
      invalidInputs.forEach(({ id, message }) => {
        this.#formRender.setError(id, message)
      })
      return false
    }

    return true
  }

  #getInputsWithValue(form: Form) {
    const formInputs = form.inputs
    const inputValues = [] as InputToValidate[]
    for (const input of formInputs) {
      const inputVal = (document.querySelector(`#${input.id}`) as HTMLInputElement).value ?? ""
      inputValues.push({
        id: input.id,
        name: input.name,
        value: inputVal,
        validators: input.validators
      })
    }
    return inputValues
  }
}
