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

    const formData = Object.groupBy(inputValues, (input) => input.name)
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
    return inputs.every((input) => {
      return input.validators.every((validator) => {
        const { isValid, message } = validator(input.value)
        if (!isValid) this.#formRender.setError(input.id, message)
        return isValid
      })
    })
  }

  #getInputsWithValue(form: Form) {
    const formInputs = form.inputs
    const inputsNodes = document.querySelectorAll(".fields-container input")
    const inputs = Array.from(inputsNodes) as HTMLInputElement[]
    return inputs.map((input, index) => {
      return {
        id: input.id,
        name: input.name,
        value: input.value,
        validators: formInputs[index].validators
      }
    })
  }
}
